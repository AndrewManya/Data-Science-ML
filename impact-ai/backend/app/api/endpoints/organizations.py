"""Programs API endpoints."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.program import ProgramCreate, ProgramResponse
from app.services.program_service import create_program, list_programs, get_program
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=ProgramResponse)
async def create_prog(program: ProgramCreate, db: Session = Depends(get_db)):
    """Create a new program."""
    return create_program(db, program)

@router.get("/", response_model=list[ProgramResponse])
async def list_progs(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    """List programs."""
    return list_programs(db, skip, limit)

@router.get("/{program_id}", response_model=ProgramResponse)
async def get_prog(program_id: str, db: Session = Depends(get_db)):
    """Get program by ID."""
    return get_program(db, program_id)
