from fastapi import Body
from fastapi import Depends
from typing import Annotated

from src.main import app
from src.shared.domain.entities.base_response_entity import BaseResponseEntity
from src.feedbacks.infrastructure.dependecies import feedback_controller
from src.feedbacks.infrastructure.schemas.feedback_schema import FeedbackCreate
from src.auth.infrastructure.dependecies.get_current_user import get_current_user


@app.get("/feedbacks/meal_uuid/{meal_uuid}", status_code=200)
def list_feedbacks(
    meal_uuid: str,
    number_page: int = 1,
    size_page: int = 10,
    current_user: Annotated[str, Depends(get_current_user)] = None,
):
    data = feedback_controller.list_feedback_by_meal_uuid(
        meal_uuid=meal_uuid, page_number=number_page, page_size=size_page
    )

    response = BaseResponseEntity(
        data=data,
        success=True,
        message="Feedbacks listed successfully",
        status_code=200,
    )

    return response.dict()


@app.post("/feedbacks", status_code=201)
def create_feedback(
    feedback: Annotated[FeedbackCreate, Body(embed=False)],
    current_user: Annotated[str, Depends(get_current_user)] = None,
):
    request = feedback.model_dump()
    data = feedback_controller.create_feedback(request)

    if data:
        response = BaseResponseEntity(
            data=data,
            success=True,
            message="Feedback created successfully",
            status_code=201,
        )

        return response.dict()

    response = BaseResponseEntity(
        data=None, success=False, message="Error creating feedback", status_code=400
    )

    return response.dict()
