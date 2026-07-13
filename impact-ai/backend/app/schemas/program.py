"""Program schemas."""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from uuid import UUID

class ProgramBase(BaseModel):
    """Base program schema."""
    name: str
    description: Optional[str] = None
    budget: Optional[float] = None
    status: str = "active"

class ProgramCreate(ProgramBase):
    """Program creation schema."""
    organization_id: UUID

class ProgramResponse(ProgramBase):
    """Program response schema."""
    id: UUID
    organization_id: UUID
    created_at: datetime
    
    class Config:
        from_attributes = True
