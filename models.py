from sqlalchemy import Column, Integer, String
from database import Base

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    mileage = Column(Integer, nullable=False)
    transmission = Column(String)
    fuel_type = Column(String)
    status = Column(String)
    image = Column(String, nullable=True)
