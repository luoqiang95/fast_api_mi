from fastapi import APIRouter
from starlette.requests import Request
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse

front_api = APIRouter(tags=["前端页面"], prefix="/front")

templates = Jinja2Templates(directory="templates")


@front_api.get("/index")
async def index(request: Request):
    return templates.TemplateResponse("/index/login.html", {"request": request})


@front_api.get("/table")
async def table(request: Request):
    return RedirectResponse("/front/index")
