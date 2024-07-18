from src.feedbacks.application.ports.feedback_repository_port import FeedbackRepositoryPort
from src.feedbacks.domain.entities.feedback_entity import FeedbackEntity

class ListFeedbackUseCase:
    def __init__(self, feedback_repository: FeedbackRepositoryPort):
        self.feedback_repository = feedback_repository

    def execute(self) -> list[FeedbackEntity]:
        return self.feedback_repository.find_all()