from typing import Dict
from fastapi import HTTPException
from sqlalchemy.orm import Session

import models.Electricity as electricity_model
import models.ElectronicName as electronic_name_model
import models.ElectronicData as electronic_model

def calculate(electricity_id: int, electronic_name_id: int, electronic_data_id: int, device_used: int, hours_used: float, db: Session) -> Dict[str, float]:
    # load electricity profile
    electricity = db.query(electricity_model.Electricity).filter(electricity_model.Electricity.id == electricity_id).first()
    if not electricity:
        raise HTTPException(status_code=404, detail="Electricity profile not found")

    # load electronic name
    name_obj = db.query(electronic_name_model.ElectronicName).filter(electronic_name_model.ElectronicName.id == electronic_name_id).first()
    if not name_obj:
        raise HTTPException(status_code=404, detail="Electronic name not found")

    # load electronic data
    data = db.query(electronic_model.ElectronicData).filter(electronic_model.ElectronicData.id == electronic_data_id).first()
    if not data:
        raise HTTPException(status_code=404, detail="Electronic data not found")

    # ensure the electronic data belongs to the provided electronic name
    if data.name_id != electronic_name_id:
        raise HTTPException(status_code=400, detail="electronic_data does not belong to the provided electronic_name")

    # validate kwh_watt to avoid division by zero
    if not electricity.kwh_watt or electricity.kwh_watt == 0:
        raise HTTPException(status_code=500, detail="Invalid kwh_watt in electricity profile")

    min_watt = float(data.min_consumption or 0.0)
    max_watt = float(data.max_consumption or 0.0)

    kwh_divisor = 1000
    min_kwh = round((min_watt / kwh_divisor) * float(hours_used) * int(device_used), 3)
    max_kwh = round((max_watt / kwh_divisor) * float(hours_used) * int(device_used), 3)

    cost_per_kwh = float(electricity.cost_per_kwh or 0.0)
    min_cost = min_kwh * cost_per_kwh
    max_cost = max_kwh * cost_per_kwh

    return {
        "electronic_name": name_obj.name,
        "electronic_type": data.type,
        "devices_used": int(device_used),
        "hours_used": int(hours_used),
        "min_consumption_watt": round(min_watt, 4),
        "max_consumption_watt": round(max_watt, 4),
        "min_kwh": round(min_kwh, 4),
        "max_kwh": round(max_kwh, 4),
        "min_cost": round(min_cost, 4),
        "max_cost": round(max_cost, 4)
    }