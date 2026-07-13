"""Tests for organization service."""

import pytest
from app.services.organization_service import create_organization
from app.schemas.organization import OrganizationCreate

def test_create_organization():
    """Test organization response model."""
    from app.schemas.organization import OrganizationResponse
    from uuid import uuid4
    from datetime import datetime
    
    org = OrganizationResponse(
        id=uuid4(),
        name="Test NGO",
        description="Test",
        website="https://test.com",
        created_at=datetime.now()
    )
    assert org.name == "Test NGO"
    assert org.website == "https://test.com"
