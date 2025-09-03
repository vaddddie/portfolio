from passlib.context import CryptContext
from sqlalchemy import func, inspect
from app.db.engine import engine, Base, Session
from app.models.project import Project
from app.models.user import User
from sqlmodel import SQLModel

"""
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
    
def auth(username, password):
    with Session() as session:
        if session.query(User).first() is not None:
            user = session.query(User).filter(User.username == username).first()
            if verify_password(password, user.password):
                return True
        else:
            new_user = User(username=username, password=hash_password(password))
            session.add(new_user)
            session.commit()
            return True
        return False
"""


def create_tables():
    inspector = inspect(engine)
    tables = inspector.get_table_names()

    if not tables:
        SQLModel.metadata.create_all(engine)  

def get_all_projects():
    with Session() as session:
        return session.query(Project).all()
    
"""
def create_project(images, title, client, category, date, project_url, subtitle, description):
    with Session() as session:
        new_project = Project(
            images=images,
            title=title,
            client=client,
            category=category,
            date=date,
            project_url=project_url,
            subtitle=subtitle,
            description=description
        )
        session.add(new_project)
        session.commit()
"""