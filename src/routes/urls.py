import hashlib

from fastapi import APIRouter, Request, status
from fastapi.responses import RedirectResponse
from ..db.Db import db
from ..utils.url_formatter import url_formatter

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/one")
def one_url(request: Request):
    return "one"


@router.get("/two")
def two_url(request: Request):
    return "two"


@router.get("/create_url/{short_code}")
def create_url(request: Request, short_code: str):

    original_url = url_formatter(str(request.url))
    
    if db.check_url([None, original_url]):
        return RedirectResponse(original_url)

    short_code = hashlib.sha256(str(request.url).encode("utf-8")).hexdigest()[:8]
    data = (
        short_code,
        original_url,
    )

    if original_url[21:] in [route.path for route in router.routes]:
        try:
            db.insert_data(data)
            return RedirectResponse(original_url)
        except Exception as e:
            return Exception(e)


@router.get("/{short_code_value}")
def url(request: Request, short_code_value: str):
    gotten_url = "/" + str(request.url)[21:]
    original_url = str(request.url)
    urls = (short_code_value, original_url)
    check_url = db.check_url(urls)

    if check_url:
        return RedirectResponse(check_url[0][0])
    else:
        return "Invalid URL"
