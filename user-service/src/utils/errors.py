# Base exception class that inherits from Python's native Exception class
# (Replaces: class AppError extends Error)
class AppError(Exception):
    def __init__(self, message: str, status_code: int, code: str):
        super().__init__(message) 
        self.message = message    
        self.status_code = status_code 
        self.code = code          

# --- CHILD ERROR CLASSES MAPPING ---

class BadRequestError(AppError):
    def __init__(self, message: str, code: str = 'BAD_REQUEST'):
        super().__init__(message, 400, code)

class UnauthorizedError(AppError):
    def __init__(self, message: str, code: str = 'UNAUTHORIZED'):
        super().__init__(message, 401, code)

class ForbiddenError(AppError):
    def __init__(self, message: str, code: str = 'FORBIDDEN'):
        super().__init__(message, 403, code)

class NotFoundError(AppError):
    def __init__(self, message: str, code: str = 'NOT_FOUND'):
        super().__init__(message, 404, code)

class ConflictError(AppError):
    def __init__(self, message: str, code: str = 'CONFLICT'):
        super().__init__(message, 409, code)

class TooManyRequestsError(AppError):
    def __init__(self, message: str, code: str = 'TOO_MANY_REQUESTS'):
        super().__init__(message, 429, code)

class InternalServerError(AppError):
    def __init__(self, message: str = 'Internal Server Error', code: str = 'SERVER_ERROR'):
        super().__init__(message, 500, code)