from app.db.session import AsyncSessionLocal
from jose import jwt, JWTError
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import SECRET_KEY, ALGORITHM, oauth2_scheme
from app.crud.user import get_user_by_email


async def get_db():
	async with AsyncSessionLocal() as session:
		yield session

async def get_current_user(token: str = Depends(oauth2_scheme),	db: AsyncSession=Depends(get_db),
	):
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
		email: str = payload.get("sub")
		if email is None:
			raise HTTPException(status_code=401, detail="Invalid token")
	except JWTError:
		raise HTTPException(status_code=401, detail="Invalid token")

	user = await get_user_by_email(db, email)
	if user is None:
		raise HTTPException(status_code=401, detail="User not found")

	return user
