from abc import ABC, abstractmethod
from src.feedbacks.domain.entities.feedback_entity import FeedbackEntity

class FeedbackRepositoryPort(ABC):
    @abstractmethod
    def save(self, feedback: FeedbackEntity) -> None:
        pass

    @abstractmethod
    def find_by_id(self, feedback_id: str) -> FeedbackEntity:
        pass

    @abstractmethod
    def find_all(self) -> list[FeedbackEntity]:
        pass
