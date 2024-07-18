from pydantic import BaseModel

class FeedbackBase(BaseModel):
    content: str
    user_uuid: str
    meal_uuid: str

class FeedbackCreate(FeedbackBase):
    pass