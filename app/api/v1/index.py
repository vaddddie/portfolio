from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.templating import Jinja2Templates
from starlette.requests import Request

from app.db.controller import get_all_projects


router = APIRouter(prefix="")

templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    context = {
        'projects': get_all_projects()
    }
    return templates.TemplateResponse(request, "index.html", context)

@router.post("/send-message", response_class=HTMLResponse)
async def send_message(name = Form(), email = Form(), subject = Form(), message = Form()):
    print(name, email, subject, message)
    return 'OK'