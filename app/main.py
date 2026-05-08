import os
from dotenv import load_dotenv

from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from starlette.staticfiles import StaticFiles

from app.api.v1 import index
from app.adminPanel import admin_init
from app.db.controller import create_tables
from app.db.engine import engine, Session

SESSION_MAX_AGE = 3600 # Час

@asynccontextmanager
async def lifespan(app: FastAPI):
    admin_init(app, engine, Session)
    create_tables()
    yield

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(project_root, '.env')
load_dotenv(env_path)

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv('SECRET_KEY'),
    max_age=SESSION_MAX_AGE,
    same_site="lax",      # безопасный вариант для cookie
)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(index.router)


