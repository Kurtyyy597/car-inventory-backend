from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
import models, schemas
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite default
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Backend is running 🚀"}

@app.get("/cars", response_model=list[schemas.CarResponse])
def get_cars(db: Session = Depends(get_db)):
    return db.query(models.Car).all()

@app.post("/cars", response_model=schemas.CarResponse)
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    db_car = models.Car(**car.model_dump())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

@app.put("/cars/{car_id}", response_model=schemas.CarResponse)
def update_car(car_id: int, car: schemas.CarCreate, db: Session = Depends(get_db)):
    db_car = db.query(models.Car).filter(models.Car.id == car_id).first()
    if not db_car:
        return {"error": "Car not found"}

    for key, value in car.model_dump().items():
        setattr(db_car, key, value)

    db.commit()
    db.refresh(db_car)
    return db_car

@app.delete("/cars/{car_id}")
def delete_car(car_id: int, db: Session = Depends(get_db)):
    db_car = db.query(models.Car).filter(models.Car.id == car_id).first()
    if not db_car:
        return {"error": "Car not found"}

    db.delete(db_car)
    db.commit()
    return {"message": "Car deleted"}



