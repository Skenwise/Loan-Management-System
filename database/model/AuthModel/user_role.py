from sqlmodel import SQLModel, Field
from typing import ClassVar

class UserRole(SQLModel, table=True):
    __tablename__: ClassVar[str] = "user_roles"

    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    role_id: int = Field(foreign_key="roles.id")