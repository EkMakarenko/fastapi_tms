from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from src.rest.schemas.remove_nullable_value_schema import RemoveNullableValueSchema


class HotelListSchema(BaseModel):
    id: int
    name: str
    country: str
    city: str
    street: str
    house_number: Optional[str]
    longitude: float
    latitude: float
    created_at: datetime
    updated_at: datetime


class HotelRetrieveSchema(BaseModel):
    id: int
    name: str
    country: str
    city: str
    street: str
    house_number: Optional[str]
    longitude: float
    latitude: float


class HotelCreateSchema(BaseModel):
    name: str
    country: str
    city: str
    street: str
    house_number: Optional[str]


class HotelUpdateInputSchema(RemoveNullableValueSchema):
    name: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    street: Optional[str] = None
    house_number: Optional[int] = None


class HotelUpdateResponseSchema(BaseModel):
    id: int
    name: str
    country: str
    city: str
    street: str
    house_number: Optional[str]
    longitude: float
    latitude: float
    created_at: datetime
    updated_at: datetime
