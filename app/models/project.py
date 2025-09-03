from sqlalchemy import Column
from sqlmodel import SQLModel, Field, Relationship
import datetime
from typing import List, Optional
from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import ImageType


class Project(SQLModel, table=True):
    __tablename__ = "projects"

    id: int | None = Field(default=None, primary_key=True)
    images: List["ProjectImage"] = Relationship(back_populates="project")
    title: str
    client: str
    category: str
    date: datetime.date
    project_url: str
    subtitle: str
    description: str

    def to_dict(self):
        return {
            'id': self.id,
            'images': self.images,
            'title': self.title,
            'client': self.client,
            'category': self.category,
            'date': self.date,
            'project_url': self.project_url,
            'subtitle':  self.subtitle,
            'description': self.description
        }

class ProjectImage(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    project_id: int = Field(foreign_key="projects.id")
    image: str | None = Field(sa_column=Column(ImageType(storage=FileSystemStorage(path=f"app/static/img/projects/"))))

    project: Optional[Project] = Relationship(back_populates="images")