from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_ENV: str = "dev"
    APP_PORT: int = 8000
    OPENAI_API_KEY: str | None = None
    CHROMA_DIR: str = "./data/vectorstore"
    SF_INSTANCE_URL: str | None = None
    SF_USERNAME: str | None = None
    SF_PASSWORD: str | None = None
    SF_SECURITY_TOKEN: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()
