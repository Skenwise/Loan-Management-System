
# providers/base_provider.py
import config
from sqlmodel import SQLModel, select
from database.sessionmaker import get_db_session, get_async_db_session
from typing import Type, List, Optional, Any, Sequence

class BaseProvider:
    """
    BaseProvider contains generic CRUD helpers for any SQLModel table.
    Module-specific providers (AuthProvider, LoanProvider) will inherit from this.
    """

    def __init__(self):
        pass

    async def get_by_id(self, model: Type[SQLModel], id: Any) -> Optional[SQLModel]:
        async with get_async_db_session() as session:
            return await session.get(model, id)

    async def get_all(self, model: Type[SQLModel]) -> Sequence[SQLModel]:
        async with get_async_db_session() as session:
            result = await session.execute(select(model))
            return result.scalars().all()

    async def create(self, instance: SQLModel) -> SQLModel:
        async with get_async_db_session() as session:
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return instance

    async def update(self, model: Type[SQLModel], id: Any, data: dict) -> Optional[SQLModel]:
        async with get_async_db_session() as session:
            instance = await session.get(model, id)
            if not instance:
                return None
            for key, value in data.items():
                setattr(instance, key, value)
            await session.commit()
            await session.refresh(instance)
            return instance

    async def delete(self, model: Type[SQLModel], id: Any) -> bool:
        async with get_async_db_session() as session:
            instance = await session.get(model, id)
            if not instance:
                return False
            await session.delete(instance)
            await session.commit()
            return True

    async def filter(self, model: Type[SQLModel], *conditions) -> Sequence[SQLModel]:
        async with get_async_db_session() as session:
            result = await session.execute(select(model).where(*conditions))
            return result.scalars().all()

    async def exists(self, model: Type[SQLModel], *conditions) -> bool:
        async with get_async_db_session() as session:
            result = await session.execute(select(model).where(*conditions))
            return result.first() is not None

    async def paginate(self, model: Type[SQLModel], offset: int = 0, limit: int = 20) -> Sequence[SQLModel]:
        async with get_async_db_session() as session:
            result = await session.execute(select(model).offset(offset).limit(limit))
            return result.scalars().all()