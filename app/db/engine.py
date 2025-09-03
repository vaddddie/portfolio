from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = 'postgresql://user:password@db:5432/mydatabase'
Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=False)

Session = sessionmaker(bind=engine)
    

