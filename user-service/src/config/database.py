from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

from src.config.settings import settings
from src.config.logger import logger

# 1. Replaces: const adapter = new PrismaPg({ connectionString })
# Creates the connection engine to PostgreSQL
engine = create_async_engine(
    settings.database_url,
    echo=False,  # Set to True if you want to see raw SQL logs in terminal
    future=True
)

# 2. Replaces: new PrismaClient(...)
# Session factory that creates database sessions for incoming requests
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False
)

# 3. Base class that all your SQLAlchemy models (like User) will inherit from
Base = declarative_base()

# 4. FastAPI Dependency for database sessions
# This gives each API request its own clean DB session and closes it automatically when done
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception as e:
            logger.error(f"Database session error: {str(e)}")
            await session.rollback()
            raise
        finally:
            await session.close()