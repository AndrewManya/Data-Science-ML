"""Custom exceptions for the application."""

class APIException(Exception):
    """Base API exception."""
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code

class ValidationException(APIException):
    """Raised when validation fails."""
    def __init__(self, message: str):
        super().__init__(message, 400)

class AuthenticationException(APIException):
    """Raised when authentication fails."""
    def __init__(self, message: str = "Authentication failed"):
        super().__init__(message, 401)

class AuthorizationException(APIException):
    """Raised when authorization fails."""
    def __init__(self, message: str = "Insufficient permissions"):
        super().__init__(message, 403)

class NotFoundException(APIException):
    """Raised when resource is not found."""
    def __init__(self, message: str = "Resource not found"):
        super().__init__(message, 404)
