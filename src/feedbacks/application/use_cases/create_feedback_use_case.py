import uuid

from src.feedbacks.application.ports.feedback_repository_port import (
    FeedbackRepositoryPort,
)
from src.feedbacks.domain.entities.feedback_entity import FeedbackEntity
from src.feedbacks.domain.enums.rating_enum import RatingEnum


class CreateFeedbackUseCase:
    def __init__(self, feedback_repository: FeedbackRepositoryPort):
        self.feedback_repositoy = feedback_repository

    def execute(self, content: str, author_uuid: str, meal_uuid: str) -> FeedbackEntity | None:
        feedback_uuid = str(uuid.uuid4())
        feedback_entity = FeedbackEntity(
            uuid=feedback_uuid,
            content=content,
            user_uuid=author_uuid,
            meal_uuid=meal_uuid,
            rating=RatingEnum.GOOD,
            id=None,
            created_at=None,
            updated_at=None,
        )
        feedback = self.feedback_repositoy.save(feedback_entity)
        return feedback
