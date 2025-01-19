import hashlib

from fastapi import APIRouter, Request, status
from fastapi.responses import RedirectResponse
from ..db.db import db


router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/one")
def one_url():
    return "one"


@router.get("two")
def two_url():
    return "two"


@router.get("/{short_code}")
def redirecter(request: Request, short_code: str):
    short_code = short_code
    print(short_code)
    check_url = db.check_url((short_code,str(request.url),))
    if check_url:
        url = str(check_url[0][0]).split("/")
        del url[3]
        url = "/".join(url)
        return RedirectResponse(url)
    return "No one url found"


@router.get("/create_url/{short_code_value}")
def url(request: Request, short_code_value: str):
    gotten_url = "/" + str(request.url)[21:].split("/")[2]
    original_url = str(request.url)
    urls = (
        short_code_value,
        original_url,
    )
    check_url = db.check_url(urls)

    if check_url:
        print(check_url[0])
        db.increas_click_by_one(urls)
        print("clicks")

        return "Such URL is already exists"
    elif gotten_url in [route.path for route in router.routes]:

        short_code = str(hashlib.sha256(original_url.encode("utf-8")).hexdigest()[:8])

        db.insert_data(urls)
        return "URL inserted successfully!"
    else:
        return "Invalid URL"
