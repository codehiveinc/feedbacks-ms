from src.config import *
from src.shared.infrastructure.database.base import Base
from src.shared.infrastructure.database.session import engine

from fastapi import FastAPI

Base.metadata.create_all(bind=engine)
app = FastAPI()




from src.feedbacks.infrastructure.routers.feedbacks_router import *