from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config import settings


DATABASE_URL = settings.database_url

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class DatabaseSession:
    _instance = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = SessionLocal()
        return cls._instance

db = DatabaseSession.get_instance()
