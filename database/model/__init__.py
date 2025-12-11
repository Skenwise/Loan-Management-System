from sqlmodel import SQLModel
from .AuthModel import User, Role, Permission, UserRole, RolePermission

all_models = [User, Role, Permission, UserRole, RolePermission]
metadata = SQLModel.metadata