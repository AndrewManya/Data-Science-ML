"""Tests for user service."""

import pytest
from app.services.user_service import (
    create_user,
    hash_password,
    verify_password,
    get_user_by_email,
)
from app.schemas.user import UserCreate

def test_hash_password():
    """Test password hashing."""
    password = "testpassword123"
    hashed = hash_password(password)
    assert hashed != password
    assert verify_password(password, hashed)

def test_verify_password_fail():
    """Test password verification failure."""
    password = "testpassword123"
    wrong_password = "wrongpassword"
    hashed = hash_password(password)
    assert not verify_password(wrong_password, hashed)
