from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.dialects.postgresql import ARRAY
from app.db.engine import Base

class Project(Base):
    __tablename__ = 'projects'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    images = Column(ARRAY(String))
    title = Column(String)
    client = Column(String)
    category = Column(String)
    date = Column(Date)
    project_url = Column(String)
    subtitle =  Column(String)
    description = Column(String)

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