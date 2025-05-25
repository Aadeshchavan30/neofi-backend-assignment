
from pydantic import BaseModel
from typing import List

class UserPermission(BaseModel):
    user_id: int
    role: str  # 'Owner', 'Editor', 'Viewer'

class ShareRequest(BaseModel):
    users: List[UserPermission]

class PermissionOut(BaseModel):
    user_id: int
    role: str
