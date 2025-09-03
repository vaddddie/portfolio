from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

from app.models.project import Project

class ProjectImage(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    project_id: int = Field(foreign_key="project.id")
    image_url: str

    project: Optional[Project] = Relationship(back_populates="images")