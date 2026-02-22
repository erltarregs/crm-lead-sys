from fastapi import FastAPI
from sqlalchemy import text
from app.db.session import engine

app = FastAPI()

@app.get("/")
def root():
	return {"message": "CRM API running"}

@app.get("/health/db")
async def test_db():
	async with engine.begin() as conn:
		await conn.execute(text("SELECT 1"))
	return {"database": "connected"}
