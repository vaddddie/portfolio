from sqladmin import Admin, ModelView
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request

from app.models.user import User
from app.models.project import Project, ProjectImage


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email, User.full_name, User.is_active]
    column_searchable_list = [User.email, User.full_name]
    can_create = True
    can_edit = True
    can_delete = True

class ProjectAdmin(ModelView, model=Project):
    column_list = [
        Project.id,
        Project.images,
        Project.title,
        Project.client,
        Project.category,
        Project.date,
        Project.project_url,
        Project.subtitle,
        Project.description,
    ]
    column_searchable_list = [Project.title, Project.category]
    can_create = True
    can_edit = True
    can_delete = True

class ProjectImageAdmin(ModelView, model=ProjectImage):
    column_list = [ProjectImage.id, ProjectImage.project_id, ProjectImage.image_url]
    column_searchable_list = [ProjectImage.project_id]
    can_create = True
    can_edit = True
    can_delete = True

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

def admin_init(app, engine, Session):
    # from app.main import app
    # from app.db.engine import engine, Session
    
    # --- инициализация админки (передаём engine или session_maker) ---
    auth_backend = AdminAuth(secret_key="very-secret-key")
    admin = Admin(app=app, engine=engine, session_maker=Session,
                  authentication_backend=auth_backend, base_url="/admin")
    admin.add_view(UserAdmin)
    admin.add_view(ProjectAdmin)
    admin.add_view(ProjectImageAdmin)
