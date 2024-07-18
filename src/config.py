from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    database_url: str
    access_token_secret: str
    rabbitmq_host: str
    rabbitmq_username: str
    rabbitmq_password: str
    saga_exchange_name: str

    class Config:
        env_file = ".env"


settings = Settings()
