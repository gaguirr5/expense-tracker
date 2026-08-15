from fastapi import FastAPI
from database import engine, Base
from sqlalchemy import text
import models

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Expense Tracker API"}


@app.get("/db-check")
def db_check():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"database": "connected", "result": result.scalar()}
