from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class ImperkaSettings(BaseSettings):
    
    model_config=SettingsConfigDict(env_prefix="imperka_", env_ignore_empty=True)
    
    secret_key: str = Field(default="secret_key")
    username: str = Field(default="admin")
    password: str = Field(default="password")
    
    algorithm: str = Field(default="HS256")
    access_token_expire_in_minutes: int = Field(default=30)
    refresh_token_expire_in_days: int = Field(default=7)
    
    mongodb_url: str = Field(default="mongodb://localhost:27017")
    mongodb_db: str = Field(default="database")
    
settings = ImperkaSettings()