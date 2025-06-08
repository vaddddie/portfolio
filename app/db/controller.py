from sqlalchemy import func, inspect
from app.db.engine import engine, Base, Session
from app.models.project import Project


def create_tables():
    inspector = inspect(engine)
    tables = inspector.get_table_names()

    if not tables:
        Base.metadata.create_all(engine)
        
def create_project():
    pass
    