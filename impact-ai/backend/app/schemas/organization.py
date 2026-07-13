"""Organization schemas."""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from uuid import UUID

class OrganizationBase(BaseModel):
    """Base organization schema."""
    name: str
    description: Optional[str] = None
    website: Optional[str] = None

class OrganizationCreate(OrganizationBase):
    """Organization creation schema."""
    pass

class OrganizationResponse(OrganizationBase):
    """Organization response schema."""
    id: UUID
    created_at: datetime
    
    class Config:
        from_attributes = True
