from authx import RequestToken
from fastapi import APIRouter, Form, Depends, UploadFile, File, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from typing import List

from app.auth import auth_config, security
from app.db.controller import auth, get_all_projects, create_project
from app.form.loginForm import LoginData


router = APIRouter(prefix="")

templates = Jinja2Templates(directory="app/templates")

get_token_dep = security.get_token_from_request(type="access", optional=False)

@router.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse(request, "login.html")

@router.post("/login")
# async def authentication(username = Form(), password = Form()):
async def authentication(request: Request):
    form = await request.form()
    login_data = LoginData(**form)
    
    if auth(login_data.username, login_data.password):
        token = security.create_access_token(uid=login_data.username)
        response = RedirectResponse("/admin-panel", status.HTTP_303_SEE_OTHER)
        response.set_cookie(auth_config.JWT_ACCESS_COOKIE_NAME, token)
        return response
    return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect username or password")

@router.get("/admin-panel", response_class=HTMLResponse, dependencies=[Depends(security.access_token_required)])
# async def admin_panel(request: Request, token: RequestToken = Depends(security.get_token_from_request(csrf_protect=False))):
async def admin_panel(request: Request, token: RequestToken = Depends(get_token_dep)):
    try:
        security.verify_token(token=token)
        context = {
            "projects": [prj.to_dict() for prj in get_all_projects()]
        }
        return templates.TemplateResponse(request=request, name="admin-panel.html", context=context)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
    
"""
    try:
        security.verify_token(token)
        context = {
            "projects": [prj.to_dict() for prj in get_all_projects()]
        }
        return templates.TemplateResponse(request, "admin-panel.html", context)
    except Exception as e:
        raise HTTPException(401, detail={"message": str(e)}) from e
"""

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
