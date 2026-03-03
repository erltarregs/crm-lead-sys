from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate, UserRead
from app.crud.user import create_user, get_users, get_user_by_email
from app.api.deps import get_db, get_current_user
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import verify_password, create_access_token
from app.models.user import User

router = APIRouter()

@router.post("/users", response_model = UserRead)
async def create(user: UserCreate, db: AsyncSession = Depends(get_db)):
	return await create_user(
		db,
		email = user.email,
		full_name = user.full_name,
		hashed_password = user.password
		)

@router.get("/users", response_model = list[UserRead])
# async def list_users(db: Session = Depends(get_db)):
# async def list_users(db: AsyncSession = Depends(get_db)):
async def list_users(db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user),):
	return await get_users(db)


@router.post("/login")
async def login(
	form_data: OAuth2PasswordRequestForm = Depends(),
	db: AsyncSession = Depends(get_db),
	):
	user = await get_user_by_email(db, form_data.username)

	if not user:
		raise HTTPException(status_code = 400, detail = "Invalid credentials")

	if not verify_password(form_data.password, user.hashed_password):
		raise HTTPException(status_code = 400, detail = "Invalid credentials")

	access_token = create_access_token({"sub": user.email})

	return {"access_token": access_token, "token_type": "bearer" }
