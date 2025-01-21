from fastapi import FastAPI, Request
from .db.Db import db
from .routes import router


app = FastAPI()


@app.middleware("http")
async def handle_reqs(request: Request, call_next):
    original_url = str(request.url)
    # if there's a URL in the database, increase the counter by one
    if db.check_url([None, original_url]):
        db.increase_click_by_one([None, original_url])
    # Generate the response, then return it
    res = await call_next(request)
    return res

# Include routes
app.include_router(router)
