from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    CONSUMER_KEY: str = Field(..., env="CONSUMER_KEY")
    CONSUMER_SECRET: str = Field(..., env="CONSUMER_SECRET")
    ACCESS_TOKEN_KEY: str = Field(..., env="ACCESS_TOKEN_KEY")
    ACCESS_TOKEN_SECRET: str = Field(..., env="ACCESS_TOKEN_SECRET")
    WEER_LIVE_API_KEY: str = Field(..., env="WEER_LIVE_API_KEy")
    WEER_LIVE_BASE_URL: str = Field(..., env="WEER_LIVE_BASE_URL")
    WEER_LIVE_LOCATION: str = Field(..., env="WEER_LIVE_LOCATION")

    class Config:
        env_prefix = ""
        case_sentive = False
        env_file = ".env"
        env_file_encoding = "utf-8"
