from sqlalchemy import func, inspect
from app.db.engine import engine, Base, Session
from app.models.project import Project
from app.models.user import User


def create_tables():
    inspector = inspect(engine)
    tables = inspector.get_table_names()

    if not tables:
        Base.metadata.create_all(engine)
        
        
def auth(username, password):
    with Session() as session:
        if session.query(User).exists() is not None:
            print("user exists")
            user = session.query(User).filter(User.username == username).first()
            if hash(password) == user.password:
                print("password correct!")
                return True
        else:
            print("new user creating")
            new_user = User(username, hash(password))
            session.add(new_user)
            session.commit()
            return True
        return False
        

def get_all_projects():
    with Session() as session:
        return session.query(Project).all()
    
    
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
    