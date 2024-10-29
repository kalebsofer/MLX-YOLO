from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MINIO_URL: str = "minio:9000"
    MINIO_ACCESS_KEY: str = "minioadmin"
    MINIO_SECRET_KEY: str = "minioadmin"
    MINIO_SECURE: bool = False

    class Config:
        env_file = ".env.dev"


def get_settings() -> Settings:
    return Settings()