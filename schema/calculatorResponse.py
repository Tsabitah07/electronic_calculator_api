from pydantic import BaseModel
from typing import List
import controller.calculatorController as controller

class CalculationItem(BaseModel):
    electricity_id: int
    electronic_name_id: int
    electronic_data_id: int
    devices_used: int
    hours_used: float

class CalculationRequest(BaseModel):
    items: List[CalculationItem]