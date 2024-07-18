from src.feedbacks.infrastructure.adapters.repositories.feedback_repository_adapter import (
    FeedbackRepositoryAdapter,
)
from src.feedbacks.application.use_cases.create_feedback_use_case import (
    CreateFeedbackUseCase,
)
from src.feedbacks.application.use_cases.list_feedback_by_meal_uuid_use_case import (
    ListFeedbackByMealUUIDUseCase,
)
from src.feedbacks.infrastructure.controllers.feedback_controller import (
    FeedbackController,
)
from src.shared.infrastructure.database.session import db


feedback_repository = FeedbackRepositoryAdapter(db)

create_feedback_use_case = CreateFeedbackUseCase(feedback_repository)
list_feedback_by_meal_uuid_use_case = ListFeedbackByMealUUIDUseCase(feedback_repository)

feedback_controller = FeedbackController(
    create_feedback_use_case, list_feedback_by_meal_uuid_use_case
)
