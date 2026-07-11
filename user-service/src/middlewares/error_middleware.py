from fastapi import Request
from fastapi.responses import JSONResponse
from src.utils.errors import AppError
from src.config.logger import logger

# 1. Catch-all handler for your custom structured application errors
async def app_error_handler(request: Request, exc: AppError):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": exc.code,
            "message": exc.message
        }
    )

# 2. Global fallback handler for unexpected application crashes (e.g., database failures, logic crashes)
async def unhandled_exception_handler(request: Request, exc: Exception):
    logger.error(f"UNHANDLED ERROR at {request.url.path}: {str(exc)}")
    
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": "SERVER_ERROR",
            "message": "Internal Server Error"
        }
    )