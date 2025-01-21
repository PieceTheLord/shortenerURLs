def url_formatter(url: str):
    "delete the '/create_url' from the original URL"

    url = url.split("/")
    del url[3]
    return "/".join(url)