from sqlmodel import SQLModel, Field
from typing import Optional, ClassVar

class Permission(SQLModel, table=True):
    __tablename__: ClassVar[str] = "permissions"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True, nullable=False)
    description: Optional[str] = None