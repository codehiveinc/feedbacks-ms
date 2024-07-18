class BaseResponseEntity:
    def __init__(self, data: dict | None, success: bool, message: str, status_code: int):
        self.data = data
        self.success = success
        self.message = message
        self.status_code = status_code

    def dict(self):
        return {
            "data": self.data,
            "success": self.success,
            "message": self.message,
            "status_code": self.status_code,
        }