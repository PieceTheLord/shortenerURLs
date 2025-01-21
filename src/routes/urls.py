import hashlib

from fastapi import APIRouter, Request, status
from fastapi.responses import RedirectResponse
from ..db.Db import db
from ..utils.url_formatter import url_formatter
from ..app import *
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
    # formating the URL to have a URL without '/create_url' part
    original_url = url_formatter(str(request.url))
    # Check if there's already exists the path in the database
    if db.check_url([None, original_url]):
        # Redirect the user by the URL
        return RedirectResponse(original_url)

    # Generate hash
    short_code = hashlib.sha256(str(request.url).encode("utf-8")).hexdigest()[:8]
    data = ( # Convert the data in a var for convience
        short_code,
        original_url,
    )
    # Check if the URL exists
    if original_url[21:] in [route.path for route in app.routes]:
        try:
            db.insert_data(data)
            return RedirectResponse(original_url)
        except Exception as e:
            return Exception(e)


@router.get("/{short_code_value}")
def url(request: Request, short_code_value: str):
    # Delete the 'http://localhost:8000' part
    gotten_url = "/" + str(request.url)[21:] 
    original_url = str(request.url)
    urls = (short_code_value, original_url)
    check_url = db.check_url(urls)
    # Check if there's a URL in the database, otherwise it's not exist
    if check_url:
        return RedirectResponse(check_url[0][0])
    else:
        return "Invalid URL"
