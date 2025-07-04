from fastapi import APIRouter, Form, Depends, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from authx import AuthXConfig, AuthX
from typing import List

from app.db.controller import auth, get_all_projects, create_project


config = AuthXConfig()
config.JWT_SECRET_KEY = "123"
config.JWT_ACCESS_COOKIE_NAME = "access_token"
config.JWT_TOKEN_LOCATION = ['cookies']

security = AuthX(config=config)


router = APIRouter(prefix="")

templates = Jinja2Templates(directory="app/templates")

@router.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse(request, "login.html")

@router.post("/login", response_class=RedirectResponse)
async def auth(username = Form(), password = Form()):
    if auth(username, password):
        token = security.create_access_token(uid="1")
        response = RedirectResponse("/admin-panel", 302)
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
    return response

@router.get("/admin-panel", response_class=HTMLResponse, dependencies=[Depends(security.access_token_required)])
async def admin_panel(request: Request):
    context = {
        "projects": [prj.to_dict() for prj in get_all_projects]
    }
    return templates.TemplateResponse(request, "admin-panel.html", context)

@router.get("/projects/create", response_class=HTMLResponse, dependencies=[Depends(security.access_token_required)])
async def create_project_view(request: Request):
    return templates.TemplateResponse(request, "project-create.html")

@router.post("/projects/create", response_class=RedirectResponse, dependencies=[Depends(security.access_token_required)])
async def create_project(
        images: List[UploadFile]=File(...),
        title=Form(),
        client=Form(),
        category=Form(),
        date=Form(),
        project_url=Form(),
        subtitle=Form(),
        description=Form()
):
    await create_project(images, title, client, category, date, project_url, subtitle, description)
    return RedirectResponse("/admin-panel", 302)


