from fastapi import FastAPI, Request
from .db.Db import db
from .routes import router


app = FastAPI()


@app.middleware("http")
async def handle_reqs(request: Request, call_next):
    original_url = str(request.url)
    print(original_url)
    if db.check_url([None, original_url]):
        db.increase_click_by_one([None, original_url])
    res = await call_next(request)
    return res


app.include_router(router)
