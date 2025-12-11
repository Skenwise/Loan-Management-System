from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine

sqlite_engine = create_engine(
    "sqlite:///database/systemDatabase.db",
    echo=True, 
    connect_args={"check_same_thread": False} # needed for SQLite multithreading
)

sqlite_async_engine = create_async_engine(
    "sqlite+aiosqlite:///database/systemDatabase.db",
    echo=True
)

postgres_engine = create_engine(
    "postgresql+psycopg2://postgres:Black99raiser%*@localhost:5432/loansystem",
    echo=True
)

postgres_async_engine = create_async_engine(
    "postgresql+asyncpg://postgres:Black99raiser%*@localhost:5432/loansystem",
    echo=True
)
