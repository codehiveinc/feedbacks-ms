from abc import ABC, abstractmethod
from src.feedbacks.domain.entities.feedback_entity import FeedbackEntity
from src.shared.domain.entities.pagination_response_entity import (
    PaginationResponseEntity,
)


class FeedbackRepositoryPort(ABC):
    @abstractmethod
    def save(self, feedback: FeedbackEntity) -> FeedbackEntity | None:
        pass

    @abstractmethod
    def find_all_by_meal_uuid(
        self, meal_uuid: str, page_number: int, page_size: int
    ) -> list[FeedbackEntity]:
        pass

    @abstractmethod
    def analyze_meal_feedback(self, content: str):
        pass
