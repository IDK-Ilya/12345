import uuid
from typing import Optional, List

from fastapi_users import schemas
from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: str = None
class ItemCreate(ItemBase):
    pass
class Item(ItemBase):
    id: int
    owner_id: int
    class Config:
        orm_mode = True

class Event(ItemBase):
    id: int
    items: List[Item] = []

    class Config:
        orm_mode = True
#----------------------------------------------------------------------------------
class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    username: str
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    telephone: str

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    password: str
    role_id: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
    telephone: str


class EventCreate(BaseModel):
    id: int
    name: str
    description: str
    date: str
    time: str
    address: str
    maxPeople: int
    place: str
    responsible_id: int
