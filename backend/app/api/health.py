# backend/app/api/health.py
from fastapi import APIRouter, Depends
# from sqlalchemy.ext.asyncio import AsyncSession
# from app.db.session import get_db

router = APIRouter()

@router.get("/health")
async def health_check():
    # simple raw SQL to verify DB connection
    # result = await db.execute("SELECT 1")
    return {
        "status": "ok",
        # "db_response": result.scalar_one()
        "message": "No DB Connections yet - just backend is working"
    }