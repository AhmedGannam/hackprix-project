# backend/app/db/session.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL

# create an async engine — DATABASE_URL can be empty for now
engine = create_async_engine(
    DATABASE_URL,
    echo=True,              # logs SQL to the console
)

# session factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,  # objects remain usable after commit
)

# dependency to inject into your routes
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session