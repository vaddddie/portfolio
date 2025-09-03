from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from starlette.staticfiles import StaticFiles

from app.api.v1 import index
# from app.api.v1 import admin
from app.adminPanel import admin_init
from app.db.controller import create_tables
from app.db.engine import engine, Session


SESSION_MAX_AGE = 3600 # Час

@asynccontextmanager
async def lifespan(app: FastAPI):
    admin_init(app, engine, Session)
    #SQLModel.metadata.create_all(engine)
    create_tables()
    yield


# create_tables()

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    SessionMiddleware,
    secret_key="very-secret-key",
    max_age=SESSION_MAX_AGE,
    same_site="lax",      # безопасный вариант для cookie
)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(index.router)
# app.include_router(admin.router)


