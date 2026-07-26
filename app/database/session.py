from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from app.config.settings import DATABASE_URL


engine = create_async_engine(DATABASE_URL)

SessionLocal = (
    async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False

    )
)


async def get_session():
    async with SessionLocal as session:
        yield session