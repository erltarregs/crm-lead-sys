# from sqlalchemy.orm import Session
from app.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import hash_password


async def get_users(db: AsyncSession):
	result = await db.execute(select(User))
	return result.scalars().all()

async def get_user_by_email(db: AsyncSession, email: str):
	result = await db.execute (select(User).where(User.email == email))
	return result.scalar_one_or_none()

async def create_user(db: AsyncSession, user: UserCreate):
	# print("DEBUG PASSWORD TYPE:", type(user.password))
	# print("DEBUG PASSWORD VALUE:", user.password)
	db_user = User(
		email = user.email,
		full_name = user.full_name,
		hashed_password = hash_password(user.password)
		)

	db.add(db_user)
	await db.commit()
	await db.refresh(db_user)

	return db_user
	# print(type(user.password), user.password)

async def update_user(db: AsyncSession, db_user: User, user_update: UserUpdate,):
	for field, value in user_update.dict(exclude_unset=True).items():
		setattr(db_user, field, value)

	await db.commit()
	await db.refresh(db_user)
	return db_user