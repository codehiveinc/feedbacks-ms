from src.feedbacks.application.ports.feedback_repository_port import (
    FeedbackRepositoryPort,
)
from src.shared.domain.entities.pagination_response_entity import (
    PaginationResponseEntity,
)


class ListFeedbackByMealUUIDUseCase:
    def __init__(self, feedback_repository: FeedbackRepositoryPort):
        self.feedback_repository = feedback_repository

    def execute(
        self, meal_uuid: str, page_number: int, page_size: int
    ) -> PaginationResponseEntity:
        return self.feedback_repository.find_all_by_meal_uuid(
            meal_uuid=meal_uuid, page_number=page_number, page_size=page_size
        )
