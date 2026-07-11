from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    service_name: str = "user-service"
    port: int = 4001
    node_env: str = "development"
    log_level: str = "info"
    redis_url: str = "redis://:irctcpass@redis:6379"
    allowed_origins: str = "http://localhost:4000"

    # Pydantic V2 style configuration mapping
    model_config = SettingsConfigDict(
        env_file=".env",
        env_case_sensitive=False,
        extra="ignore"  
    )

# Create the instance to be used across the application
settings = Settings()