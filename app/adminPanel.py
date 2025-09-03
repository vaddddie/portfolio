from sqlmodel import SQLModel, Field
from sqladmin import Admin, ModelView
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request

class User(SQLModel, table=True):
    __tablename__ = "users"
    
    id: int | None = Field(default=None, primary_key=True)
    email: str
    full_name: str | None = None
    is_active: bool = True

class Post(SQLModel, table=True):
    __tablename__ = "posts"

    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str
    author_id: int = Field(foreign_key="users.id")

class AdminAuth(AuthenticationBackend):
    def __init__(self, secret_key: str):
        super().__init__(secret_key=secret_key)

    async def login(self, request: Request) -> bool:
        form = await request.form()
        username = form.get("username")
        password = form.get("password")
        # TODO: проверить username/password в вашей БД
        if username == "admin" and password == "admin":
            request.session.update({"admin": True})
            return True
        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        return bool(request.session.get("admin"))

class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email, User.full_name, User.is_active]
    column_searchable_list = [User.email, User.full_name]
    can_create = True
    can_edit = True
    can_delete = True

class PostAdmin(ModelView, model=Post):
    column_list = [Post.id, Post.title, Post.content, Post.author_id]
    column_searchable_list = [Post.title, Post.content]
    can_create = True
    can_edit = True
    can_delete = True

def admin_init():
    from app.main import app
    from app.db.engine import engine, Session
    
    # --- инициализация админки (передаём engine или session_maker) ---
    auth_backend = AdminAuth(secret_key="very-secret-key")
    admin = Admin(app=app, engine=engine, session_maker=Session,
                  authentication_backend=auth_backend, base_url="/admin")
    admin.add_view(UserAdmin)
    admin.add_view(PostAdmin)
