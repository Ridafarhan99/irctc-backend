from fastapi.middleware.cors import CORSMiddleware
from src.config.settings import settings

allowed_origins = (
    [origin.strip() for origin in settings.ALLOWED_ORIGINS.split(",")]
    if getattr(settings, "ALLOWED_ORIGINS", None)
    else []
)

def add_cors(app):
    app.add_middleware(
        CORSMiddleware,

        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["Content-Type", "Authorization"],
    )