from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.templating import Jinja2Templates
from starlette.requests import Request


router = APIRouter(prefix="")

templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse(request, "index.html")

@router.post("/send-message", response_class=HTMLResponse)
async def send_message(name = Form(), email = Form(), subject = Form(), message = Form()):
    print(name, email, subject, message)
    return 'OK'