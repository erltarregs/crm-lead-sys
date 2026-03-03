from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.schemas.user import UserCreate, UserResponse
from app.crud.user import create_user, get_user_by_email

router = APIRouter()

@router.post("/register", response_model = UserResponse)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
	existing_user = await get_user_by_email(db, user.email)

	if existing_user:
		raise HTTPException(status_code = 400, detail="The email is already registered.")
	return await create_user(db, user)