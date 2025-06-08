from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine(f'postgresql://user:password@db:5432/mydatabase', echo=False)

Session = sessionmaker(bind=engine)
    

