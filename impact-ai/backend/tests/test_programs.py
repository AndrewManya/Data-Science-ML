"""Tests for programs service."""

import pytest
from app.schemas.program import ProgramResponse
from uuid import uuid4
from datetime import datetime

def test_program_response_model():
    """Test program response model."""
    program = ProgramResponse(
        id=uuid4(),
        organization_id=uuid4(),
        name="Health Program",
        description="Community health initiative",
        budget=50000.0,
        status="active",
        created_at=datetime.now()
    )
    assert program.name == "Health Program"
    assert program.status == "active"
    assert program.budget == 50000.0
