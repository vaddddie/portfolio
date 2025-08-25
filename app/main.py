from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app.api.v1 import index
from app.api.v1 import admin
from app.db.controller import create_tables


create_tables()

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(index.router)
app.include_router(admin.router)


