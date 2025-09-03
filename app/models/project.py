from sqlmodel import SQLModel, Field, Relationship
import datetime
from typing import List, Optional


class Project(SQLModel, table=True):
    __tablename__ = "Projects"

    id: int | None = Field(default=None, primary_key=True)
    images: List["ProjectImage"] = Relationship(back_populates="project")
    title: str
    client: str
    category: str
    date: datetime.date
    project_url: str
    subtitle: str
    description: str
    author_id: int = Field(foreign_key="users.id")

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
    image_url: str

    project: Optional[Project] = Relationship(back_populates="images")