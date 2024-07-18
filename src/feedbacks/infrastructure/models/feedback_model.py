from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy.sql import func
from src.feedbacks.domain.enums.rating_enum import RatingEnum
from src.shared.infrastructure.database.session import Base


class FeedbackModel(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String(255), unique=True, index=True)
    content = Column(String(255))
    rating = Column(Enum(RatingEnum))
    author_uuid = Column(String(255))
    meal_uuid = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
