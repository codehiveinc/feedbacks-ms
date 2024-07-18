from fastapi import Body
from typing import Annotated

from src.main import app
from src.feedbacks.infrastructure.dependecies import (
    list_feedback_use_case,
    create_feedback_use_case,
)
from src.shared.domain.entities.base_response_entity import BaseResponseEntity
from src.feedbacks.infrastructure.schemas.feedback_schema import FeedbackCreate


@app.get("/feedbacks")
def get_feedbacks():
    feedbacks = list_feedback_use_case.execute()

    base_response = BaseResponseEntity(
        data=feedbacks, success=True, message="Feedbacks listed", status_code=200
    )

    return base_response.dict()


@app.post("/feedbacks", status_code=201)
def create_feedback(feedback: Annotated[FeedbackCreate, Body(embed=False)]):
    request = feedback.model_dump()
    feedback = create_feedback_use_case.execute(content=request["content"], user_uuid=request["user_uuid"], meal_uuid=request["meal_uuid"])

    base_response = BaseResponseEntity(
        data=feedback, success=True, message="Feedback created", status_code=201
    )

    return base_response.dict()
