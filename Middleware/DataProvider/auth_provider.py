import config
from typing import Optional, List, cast, Sequence
from sqlmodel import select
from .base_provider import BaseProvider
from database.model.AuthModel import *
from database.sessionmaker import get_postgres_async_db_session

class AuthProvider(BaseProvider):

    #------------------------------
    # USER MANAGEMENT
    #--------------------------------

    async def get_user_by_email(self, email: str) -> Optional[User]:
        async with get_postgres_async_db_session() as session:
            result = await session.execute(select(User).where(User.email == email))
            return result.scalars().first()
        
    async def assign_role_to_user(self, user_id: int, role_id: int) -> UserRole:
        async with get_postgres_async_db_session() as session:
            link = UserRole(user_id=user_id, role_id=role_id)
            return cast(UserRole, await self.create(link))

    async def get_user_roles(self, user_id: int) -> Sequence[Role]:
        async with get_postgres_async_db_session() as session:
            result = await session.execute(select(Role)
                                           .join(UserRole, (Role.id == UserRole.role_id))  # type: ignore
                                           .where(UserRole.user_id == user_id))
            return result.scalars().all()
    
    async def get_user_permissions(self, user_id: int) -> Sequence[Permission]:
        async with get_postgres_async_db_session() as session:
            result = await session.execute(select(Permission)
                                           .join(RolePermission, (Permission.id == RolePermission.permission_id)) # type: ignore
                                           .join(UserRole, (RolePermission.role_id == UserRole.role_id)). # type: ignore
                                           where(UserRole.user_id == user_id))
            return result.scalars().all()
        
    
    #--------------------------------------
    # ROLE MANNAGEMENT
    #-------------------------------------

    async def get_role_by_name(self, role_name: str) -> Optional[Role]:
        async with get_postgres_async_db_session() as session:
            result = await session.execute(select(Role).where(Role.name == role_name))
            return result.scalars().first()
        
    async def assign_permission_to_role(self, role_id: int, permission_id: int) -> RolePermission:
        async with get_postgres_async_db_session() as session:
            link = RolePermission(role_id=role_id, permission_id=permission_id)
            return cast(RolePermission, await self.create(link))
        
    
    # ------------------------------
    # PERMISSION MANAGEMENT
    # ------------------------------

    async def get_permission_by_name(self, name: str) -> Optional[Permission]:
        async with get_postgres_async_db_session() as session:
            result = await session.execute(select(Permission).where(Permission.name == name))
            return result.scalars().first()