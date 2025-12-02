import controller.calculatorController as controller
from database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/", tags=["Calculator"])
def calculate_cost(electronic_id: int, electricity_id: int, hours_used: int, devices_used: int = 1,
                   db: Session = Depends(get_db)):
    try:
        total_cost = controller.calculate_energy_cost(
            electronic_id, electricity_id, devices_used, hours_used, db)
        return {
            "message": "Successfully calculated energy cost",
            "status": 200,
            "data": {
                "total_cost": total_cost
            }
        }
    except ValueError as e:
        return {
            "message": str(e),
            "status": 404,
            "data": None
        }