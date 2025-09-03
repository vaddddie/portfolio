from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    __tablename__ = "Users"

    id: int | None = Field(default=None, primary_key=True)
    email: str
    password: str
    full_name: str | None = None
    is_active: bool = True