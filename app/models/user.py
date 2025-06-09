from sqlalchemy import Column, Integer, String
from app.db.engine import Base

class User(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }