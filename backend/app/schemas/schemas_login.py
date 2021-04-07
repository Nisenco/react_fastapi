from app.schemas.rwschema import RWModel
from typing import Optional


class LoginModel(RWModel):
    username: str
    password: str
    id: Optional[str]


class MFAInfo(RWModel):
    username: str
    dynamic_password: str
    ip: Optional[str]


class UserTokenInfo(RWModel):
    id: int
    name: str
    account: str
    group_id: int
    role: str
    is_manager: bool
    token_expire_delta: Optional[int]
