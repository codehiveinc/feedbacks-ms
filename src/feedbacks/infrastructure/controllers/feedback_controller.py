from src.feedbacks.application.use_cases.create_feedback_use_case import (
    CreateFeedbackUseCase,
)
from src.feedbacks.application.use_cases.list_feedback_by_meal_uuid_use_case import (
    ListFeedbackByMealUUIDUseCase,
)

class FeedbackController:
    def __init__(
        self,
        create_feedback_use_case: CreateFeedbackUseCase,
        list_feedback_use_case: ListFeedbackByMealUUIDUseCase,
    ):
        self.create_feedback_use_case = create_feedback_use_case
        self.list_feedback_use_case = list_feedback_use_case

    def create_feedback(self, feedback: dict) -> dict | None:
        return self.create_feedback_use_case.execute(
            content=feedback["content"],
            author_uuid=feedback["user_uuid"],
            meal_uuid=feedback["meal_uuid"],
        )

    def list_feedback_by_meal_uuid(
        self, meal_uuid: str, page_number: int, page_size: int
    ) -> dict:
        return self.list_feedback_use_case.execute(
            meal_uuid=meal_uuid, page_number=page_number, page_size=page_size
        )
