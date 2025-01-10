from typing import List

from pydantic import BaseModel, field_validator, Field
from app.services.cat_breed import validate_breed


class CatBase(BaseModel):
    name: str
    years_of_experience: int
    breed: str
    salary: float

    @field_validator('breed')
    def validate_breed_field(cls, value):
        is_valid, message = validate_breed(value)

        if not is_valid:
            raise ValueError(message)

        return message


class CatCreate(CatBase):
    pass


class CatUpdate(BaseModel):
    years_of_experience: int
    salary: float


class Cat(CatBase):
    id: int

    class Config:
        from_attributes = True


class TargetCreate(BaseModel):
    name: str
    country: str
    notes: str | None = None


class TargetUpdate(BaseModel):
    notes: str | None = None


class Target(BaseModel):
    id: int
    mission_id: int | None = None
    name: str
    country: str
    notes: str | None = None
    complete: bool

    class Config:
        from_attributes = True


class MissionCreate(BaseModel):
    cat_id: int | None
    targets: List[TargetCreate] = Field(..., min_items=1, max_items=3)


class Mission(BaseModel):
    id: int
    cat_id: int | None
    complete: bool
    targets: List[TargetCreate]

    class Config:
        from_attributes = True
