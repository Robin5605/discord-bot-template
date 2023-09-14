from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvConfig(BaseSettings):
    """Base configuration that loads from .env files"""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        extra="ignore",
    )


class BotSettings(EnvConfig):
    prefix: str = "$"
    token: str

    model_config = SettingsConfigDict(env_prefix="bot_")


bot_settings = BotSettings()  # pyright: ignore
