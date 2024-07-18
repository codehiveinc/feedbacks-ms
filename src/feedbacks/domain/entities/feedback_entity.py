from src.feedbacks.domain.enums.rating_enum import RatingEnum


class FeedbackEntity:
    def __init__(
        self,
        id: int,
        uuid: str,
        content: str,
        rating: RatingEnum,
        user_uuid: str,
        meal_uuid: str,
        created_at,
        updated_at,
    ):
        self.id = id
        self.uuid = uuid
        self.content = content
        self.rating = rating
        self.user_uuid = user_uuid
        self.meal_uuid = meal_uuid
        self.created_at = created_at
        self.updated_at = updated_at
