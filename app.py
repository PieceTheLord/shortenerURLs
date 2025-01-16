from fastapi import FastAPI
from .db.db import db

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/db")
async def dburl():
    db.Cquery("Create table if not exists db(id integer primary key)")
    data = db.Rquery("select * from information_schema.tables where table_name='db'")
    print(data)
    return {
        "data": data 
    }
