from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount(
    "/frontend",
    StaticFiles(directory="frontend"),
    name="frontend"
)

templates = Jinja2Templates(directory="frontend")

@app.get("/")
async def root():
    return {"message": "Testing test"}


@app.get("/index/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# @app.get("/video", response_class=HTMLResponse)
# async def video(request: Request):
#     return templates.TemplateResponse(
#         request=request,
#         name="index.html"
#     )