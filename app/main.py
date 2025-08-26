from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from starlette.staticfiles import StaticFiles
from sqlmodel import SQLModel

from app.api.v1 import index
# from app.api.v1 import admin
from app.adminPanel import admin_init
from app.db.controller import create_tables
from app.db.engine import Session


@asynccontextmanager
async def lifespan(app: FastAPI):
    admin_init()
    async with Session.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    yield


# create_tables()

app = FastAPI(lifespan=lifespan)
app.add_middleware(SessionMiddleware, secret_key="very-secret-key")
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(index.router)
# app.include_router(admin.router)


