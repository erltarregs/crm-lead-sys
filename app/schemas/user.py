from pydantic import BaseModel, EmailStr
from datetime import datetime
from uuid import UUID
from typing import Optional

class UserCreate(BaseModel):
	email: EmailStr
	full_name: str | None = None
	password: str

class UserRead(BaseModel):
	id: UUID
	email: EmailStr
	full_name: str | None = None

	class Config:
		from_attributes = True

class UserBase(BaseModel):
	email: EmailStr
	full_name: str | None = None

class UserLogin(BaseModel):
	email: EmailStr
	password: str

class UserResponse(UserBase):
	id: str
	is_active: bool
	is_admin: bool
	created_at: datetime

	class Config:
		from_attributes = True

class UserUpdate(BaseModel):
	full_name: Optional[str] = None
	class Config:
		from_attributes = True

