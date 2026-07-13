"""Data validation utilities."""

from typing import Any, List
import re

def validate_email(email: str) -> bool:
    """Validate email format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone: str) -> bool:
    """Validate phone number format."""
    pattern = r'^\+?1?\d{9,15}$'
    return re.match(pattern, phone) is not None

def validate_url(url: str) -> bool:
    """Validate URL format."""
    pattern = r'^https?://[\w.-]+\.\w+'
    return re.match(pattern, url) is not None

def sanitize_input(value: str, max_length: int = 1000) -> str:
    """Sanitize user input."""
    if not isinstance(value, str):
        return str(value)[:max_length]
    return value.strip()[:max_length]
