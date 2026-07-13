"""Organizations API endpoints."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.organization import OrganizationCreate, OrganizationResponse
from app.services.organization_service import create_organization, list_organizations, get_organization
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=OrganizationResponse)
async def create_org(org: OrganizationCreate, db: Session = Depends(get_db)):
    """Create a new organization."""
    return create_organization(db, org)

@router.get("/", response_model=list[OrganizationResponse])
async def list_orgs(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    """List organizations."""
    return list_organizations(db, skip, limit)

@router.get("/{org_id}", response_model=OrganizationResponse)
async def get_org(org_id: str, db: Session = Depends(get_db)):
    """Get organization by ID."""
    return get_organization(db, org_id)
