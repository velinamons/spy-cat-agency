from pydantic import BaseModel, field_validator
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
