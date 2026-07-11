import time
from fastapi import Request
from src.config.logger import logger

async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info(f"[{request.method}] {request.url.path} - status: {response.status_code} - {process_time * 1000:.0f}ms")
    return response