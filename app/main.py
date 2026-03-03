from fastapi import FastAPI
from sqlalchemy import text
from app.db.session import engine
from app.api.routes import users
from app.api.routes import auth


app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
def root():
	return {"message": "CRM API running"}

@app.get("/health/db")
async def test_db():
	async with engine.begin() as conn:
		await conn.execute(text("SELECT 1"))
	return {"database": "connected"}
# ################
@app.get("/about")
def about():
	page = {
		"name"		: "techntunesstudio",
		"age"		: 0,
		"message"	: "This is the about page"
	}
	notif = (page["message"] + " by " + page["name"] + ".")
	return notif
