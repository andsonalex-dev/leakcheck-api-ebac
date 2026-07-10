from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    APP_NAME: str
    APP_ENV: str

    HOST: str
    PORT: int

    LEAKCHECK_URL: str

    class Config:
        env_file = ".env"

settings = Settings()