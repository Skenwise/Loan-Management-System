from sqlmodel import SQLModel, Field
from typing import ClassVar

class RolePermission(SQLModel, table=True):
    __tablename__: ClassVar[str] = "role_permissions"

    id: int = Field(default=None, primary_key=True)
    role_id: int = Field(foreign_key="roles.id")
    permission_id: int = Field(foreign_key="permissions.id")