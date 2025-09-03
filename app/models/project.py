from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlmodel import SQLModel, Field
import datetime

class Project(SQLModel, table=True):
    __tablename__ = "Projects"

    id: int | None = Field(default=None, primary_key=True)
    image_urls: list[str] = Field(default_factory=list, sa_column=Field(sa_column=Column(ARRAY(String)))) # Только для Postgres
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
            'images': self.image_urls,
            'title': self.title,
            'client': self.client,
            'category': self.category,
            'date': self.date,
            'project_url': self.project_url,
            'subtitle':  self.subtitle,
            'description': self.description
        }