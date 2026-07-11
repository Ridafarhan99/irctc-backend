from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
import uvicorn

from src.config.settings import settings
from src.config.logger import logger
from src.middlewares.req_middleware import log_requests
from src.middlewares.error_middleware import app_error_handler, unhandled_exception_handler
from src.utils.errors import AppError
from src.middlewares.cors_middleware import add_cors

app = FastAPI(title="IRCTC User Microservice")

add_cors(app)

@app.middleware("http")
async def security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    return response

app.add_middleware(BaseHTTPMiddleware, dispatch=log_requests)

app.add_exception_handler(AppError, app_error_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)

@app.get("/")
async def root():
    return "Hello from main.py of User Service"

@app.get("/health")
async def health():
    return "ok"

if __name__ == "__main__":
    # Log the application initialization sequence using the configured port (40001)
    logger.info(f"User Service is running on http://localhost:{settings.port}")
    
    # Fire up the live hot-reloading server process
    uvicorn.run("src.main:app", host="0.0.0.0", port=settings.port, reload=True)