# Example seed.py
from sqlalchemy.orm import Session
from database import SessionLocal
from models.Electricity import Electricity
from models.ElectronicData import ElectronicData
from models.ElectronicName import ElectronicName


def seed_data(db: Session):
    # Example: Check if data already exists to prevent duplicate seeding
    if not db.query(Electricity).first():
        electricity_data = [
            Electricity(name="Residential", kwh_watt=500, cost_per_kwh=900),
            Electricity(name="Commercial", kwh_watt=900, cost_per_kwh=1200),
            Electricity(name="Industrial", kwh_watt=1200, cost_per_kwh=1500)
        ]
        db.add_all(electricity_data)
        db.commit()
        print("Database seeded with initial users.")
    else:
        print("Database already seeded.")

    if not db.query(ElectronicName).first():
        electronic_name_data = [
            ElectronicName(name="Refrigerator"),
            ElectronicName(name="Air Conditioner"),
            ElectronicName(name="Washing Machine"),
            ElectronicName(name="Television"),
            ElectronicName(name="Computer")
        ]
        db.add_all(electronic_name_data)
        db.commit()
        print("Electronic names seeded.")
    else:
        print("Electricity data already exists, skipping seeding.")

    if not db.query(ElectronicData).first():
        electronic_data = [
            ElectronicData(name_id=1, type="Fridge", min_consumption=100, max_consumption=200),
            ElectronicData(name_id=2, type="AC", min_consumption=800, max_consumption=1200),
            ElectronicData(name_id=3, type="Washing Machine", min_consumption=400, max_consumption=600),
            ElectronicData(name_id=4, type="TV", min_consumption=150, max_consumption=250),
            ElectronicData(name_id=5, type="Computer", min_consumption=250, max_consumption=350)
        ]
        db.add_all(electronic_data)
        db.commit()
        print("Electronic data seeded.")
    else:
        print("Electronic data already exists, skipping seeding.")

if __name__ == "__main__":
    db = SessionLocal()
    seed_data(db)
    db.close()
