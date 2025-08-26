from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

DATABASE_URL = 'postgresql://user:password@db:5432/mydatabase'
Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=False)
# engine = create_async_engine(DATABASE_URL, echo=True)
# async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Session = sessionmaker(bind=engine)
    

