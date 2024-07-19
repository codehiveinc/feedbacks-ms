from sqlalchemy.orm import Session
from src.feedbacks.application.ports.feedback_repository_port import (
    FeedbackRepositoryPort,
)
from src.feedbacks.domain.entities.feedback_entity import FeedbackEntity
from src.feedbacks.infrastructure.models.feedback_model import FeedbackModel
from src.shared.domain.entities.pagination_response_entity import (
    PaginationResponseEntity,
)
from src.feedbacks.infrastructure.utils.feedback_analyzer import analyze_sentiment


class FeedbackRepositoryAdapter(FeedbackRepositoryPort):
    def __init__(self, db: Session):
        self.db = db

    def save(self, feedback: FeedbackEntity) -> FeedbackEntity | None:
        feedback_model = FeedbackModel(
            uuid=feedback.uuid,
            content=feedback.content,
            rating=feedback.rating,
            author_uuid=feedback.user_uuid,
            meal_uuid=feedback.meal_uuid,
        )

        try:
            self.db.add(feedback_model)
            self.db.commit()
            self.db.refresh(feedback_model)

            return FeedbackEntity(
                id=feedback_model.id,
                uuid=feedback_model.uuid,
                content=feedback_model.content,
                rating=feedback_model.rating,
                user_uuid=feedback_model.author_uuid,
                meal_uuid=feedback_model.meal_uuid,
                created_at=feedback_model.created_at,
                updated_at=feedback_model.updated_at,
            )
        except Exception as e:
            self.db.rollback()
            return None

    def find_all_by_meal_uuid(
        self, meal_uuid: str, page_number: int, page_size: int
    ) -> PaginationResponseEntity:
        offset = (page_number - 1) * page_size

        feedbacks = (
            self.db.query(FeedbackModel)
            .filter(FeedbackModel.meal_uuid == meal_uuid)
            .order_by(FeedbackModel.created_at.asc())
            .offset(offset)
            .limit(page_size)
            .all()
        )

        feedback_entities = [
            FeedbackEntity(
                id=feedback.id,
                uuid=feedback.uuid,
                content=feedback.content,
                rating=feedback.rating,
                user_uuid=feedback.author_uuid,
                meal_uuid=feedback.meal_uuid,
                created_at=feedback.created_at,
                updated_at=feedback.updated_at,
            )
            for feedback in feedbacks
        ]

        total_items = (
            self.db.query(FeedbackModel)
            .filter(FeedbackModel.meal_uuid == meal_uuid)
            .count()
        )

        response = PaginationResponseEntity(
            items=feedback_entities,
            total_items=total_items,
            page_number=page_number,
            page_size=page_size,
        )

        return response


    def analyze_meal_feedback(self, content: str):
        return analyze_sentiment(content)