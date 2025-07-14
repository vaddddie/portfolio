from authx import RequestToken
from fastapi import APIRouter, Form, Depends, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from typing import List

from app.auth import auth_config, security
from app.db.controller import auth, get_all_projects, create_project


router = APIRouter(prefix="")

templates = Jinja2Templates(directory="app/templates")

@router.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse(request, "login.html")

@router.post("/login")
async def authentication(username = Form(), password = Form()):
    if auth(username, password):
        token = security.create_access_token(uid="1")
        response = RedirectResponse("/admin-panel", 302)
        csrf_token = "123123"
        response.set_cookie(auth_config.JWT_ACCESS_COOKIE_NAME, token)
        response.set_cookie(key=auth_config.JWT_ACCESS_CSRF_COOKIE_NAME, value=csrf_token, httponly=False)
        return response
    return HTTPException(status_code=400, detail="Incorrect username or password")

@router.get("/admin-panel", response_class=HTMLResponse)
async def admin_panel(request: Request, token: RequestToken = Depends(security.get_token_from_request())):
    try:
        security.verify_token(token)
        context = {
            "projects": [prj.to_dict() for prj in get_all_projects()]
        }
        return templates.TemplateResponse(request, "admin-panel.html", context)
    except Exception as e:
        raise HTTPException(401, detail={"message": str(e)}) from e

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


