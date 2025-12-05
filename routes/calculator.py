from typing import Dict, Any

import controller.calculatorController as controller
from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schema.calculatorResponse as schema

router = APIRouter()

@router.post("/", tags=["Calculator"])
def calculate_cost(
    electricity_id: int,
    electronic_name_id: int,
    electronic_data_id: int,
    device_used: int,
    hours_used: float,
    db: Session = Depends(get_db)
):
    return controller.calculate(
        electricity_id,
        electronic_name_id,
        electronic_data_id,
        device_used,
        hours_used,
        db
    )

@router.post("/bulk", tags=["Calculator"])
def calculate_bulk(payload: schema.CalculationRequest, db: Session = Depends(get_db)) -> Dict[str, Any]:
    results = []
    total_min_cost = 0.0
    total_max_cost = 0.0
    total_min_kwh = 0.0
    total_max_kwh = 0.0

    for item in payload.items:
        try:
            result = controller.calculate(
                electricity_id=item.electricity_id,
                electronic_name_id=item.electronic_name_id,
                electronic_data_id=item.electronic_data_id,
                device_used=item.devices_used,
                hours_used=item.hours_used,
                db=db
            )
            # accumulate totals from successful results
            # guard against missing keys
            total_min_cost += float(result.get("min_cost", 0.0))
            total_max_cost += float(result.get("max_cost", 0.0))
            total_min_kwh += float(result.get("min_kwh", 0.0))
            total_max_kwh += float(result.get("max_kwh", 0.0))

            results.append(result)
        except HTTPException as exc:
            results.append({"input": item.dict(), "error": {"status_code": exc.status_code, "detail": exc.detail}})
    totals = {
        "total_min_cost": round(total_min_cost * 30, 4),
        "total_max_cost": round(total_max_cost * 30, 4),
        "total_min_kwh": round(total_min_kwh * 30, 4),
        "total_max_kwh": round(total_max_kwh * 30, 4),
    }
    return {"totals": totals, "results": results}