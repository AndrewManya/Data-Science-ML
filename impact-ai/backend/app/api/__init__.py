"""API routes package."""

from fastapi import APIRouter
from app.api.endpoints import users, organizations, programs

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(organizations.router, prefix="/organizations", tags=["organizations"])
api_router.include_router(programs.router, prefix="/programs", tags=["programs"])
