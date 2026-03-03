from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL
from app.models import user

engine = create_async_engine(
	DATABASE_URL,
	echo = True, # connect_args={"autocommit": False},
)

AsyncSessionLocal = sessionmaker(
	engine,
	class_ = AsyncSession,
	expire_on_commit = False
)