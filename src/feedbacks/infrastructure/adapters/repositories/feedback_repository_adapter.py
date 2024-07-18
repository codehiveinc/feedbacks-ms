from sqlalchemy.orm import Session
from src.feedbacks.application.ports.feedback_repository_port import (
    FeedbackRepositoryPort,
)
from src.feedbacks.domain.entities.feedback_entity import FeedbackEntity
from src.feedbacks.infrastructure.models.feedback_model import FeedbackModel


class FeedbackRepositoryAdapter(FeedbackRepositoryPort):
    def __init__(self, db: Session):
        self.db = db

    def save(self, feedback: FeedbackEntity) -> None:
        feedback_model = FeedbackModel(
            uuid=feedback.uuid,
            content=feedback.content,
            rating=feedback.rating,
            author_uuid=feedback.user_uuid,
            meal_uuid=feedback.meal_uuid,
        )
        self.db.add(feedback_model)
        self.db.commit()
        self.db.refresh(feedback_model)

        return feedback_model

    def find_by_id(self, feedback_id: str) -> FeedbackEntity:
        return (
            self.db.query(FeedbackModel).filter(FeedbackModel.id == feedback_id).first()
        )

    def find_all(self) -> list[FeedbackEntity]:
        return self.db.query(FeedbackModel).all()
