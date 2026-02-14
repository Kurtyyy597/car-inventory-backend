from pydantic import BaseModel
from typing import Optional

class CarBase(BaseModel):
    brand: str
    model: str
    year: int
    price: int
    mileage: int
    transmission: str
    fuel_type: str
    status: str
    image: Optional[str] = None

class CarCreate(CarBase):
    pass

class CarResponse(CarBase):
    id: int

    class Config:
        from_attributes = True
