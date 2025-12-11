# providers/user_provider.py
from sqlmodel import select
from .base_provider import BaseProvider
from database.model.AuthModel import *
from typing import Optional, List, cast

class UserProvider(BaseProvider):

    async def create_user(self, user: User) -> User:
        return cast(User, await self.create(user))

    async def get_user_by_id(self, user_id: int) -> Optional[User]:
        return cast(User, await self.get_by_id(User, user_id))

    async def get_user_by_email(self, email: str) -> Optional[User]:
        users = await self.filter(User, User.email == email)
        return cast(User, users[0] if users else None)

    async def update_user(self, user_id: int, data: dict) -> Optional[User]:
        return cast(User, await self.update(User, user_id, data))

    async def delete_user(self, user_id: int) -> bool:
        return await self.delete(User, user_id)

    async def list_users(self):
        return await self.get_all(User)

    async def assign_role(self, user_id: int, role_id: int):
        # Prevent duplicates
        exists = await self.exists(UserRole,
                                   UserRole.user_id == user_id,
                                   UserRole.role_id == role_id)

        if exists:
            return None

        relation = UserRole(user_id=user_id, role_id=role_id)
        return await self.create(relation)

    async def remove_role(self, user_id: int, role_id: int):
        # fetch the relation
        relations = await self.filter(
            UserRole,
            UserRole.user_id == user_id,
            UserRole.role_id == role_id
        )
        if not relations:
            return False

        relation = cast(UserRole, relations[0])
        return await self.delete(UserRole, relation.id)