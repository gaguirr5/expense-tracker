from fastapi import FastAPI
from database import engine, Base
from sqlalchemy import text
from auth import router as auth_router
import models  # noqa: F401 — imported for its side effect: registers User with Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth_router)


@app.get("/")
def read_root():
    return {"message": "Expense Tracker API"}


@app.get("/db-check")
def db_check():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"database": "connected", "result": result.scalar()}
