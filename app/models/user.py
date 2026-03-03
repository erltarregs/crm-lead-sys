from sqlalchemy import String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
import uuid

from app.db.base import Base


class User(Base):
	__tablename__ = "users"

	id: Mapped[str] = mapped_column(
		String,
		primary_key = True,
		default = lambda: str(uuid.uuid4())
		)

	email: Mapped[str] = mapped_column(
		String,
		unique = True,
		index = True,
		nullable = False
		)

	hashed_password: Mapped[str] = mapped_column(
		String,
		nullable = False
		)

	full_name: Mapped[str] = mapped_column(
		String,
		nullable = True
		)

	is_active: Mapped[bool] = mapped_column(
		Boolean,
		default = True
		)

	is_admin: Mapped[bool] = mapped_column(
		Boolean,
		default = False
		)

	created_at: Mapped[datetime] = mapped_column(
		DateTime,
		default = datetime.utcnow
		)
	