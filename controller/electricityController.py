from sqlalchemy.orm import Session
from fastapi import HTTPException
import models.Electricity as models
import schema.electricityResponse as schema

# CREATE
def create_item(db: Session, item: schema.ResponseCreate):
    db_item = models.Electricity(
        name=item.name,
        kwh_watt=item.kwh_watt,
        cost_per_kwh=item.cost_per_kwh
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# READ ALL
def read_items(db: Session):
    return db.query(models.Electricity).all()


# READ ONE
def read_item(db: Session, id: int):
    item = db.query(models.Electricity).filter(models.Electricity.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


# UPDATE
def update_item(db: Session, id: int, new_data: schema.ResponseCreate):
    item = db.query(models.Electricity).filter(models.Electricity.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item.name = new_data.name
    item.kwh_watt = new_data.kwh_watt
    item.cost_per_kwh = new_data.cost_per_kwh

    db.commit()
    db.refresh(item)
    return item


# DELETE
def delete_item(db: Session, id: int):
    item = db.query(models.Electricity).filter(models.Electricity.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(item)
    db.commit()
    return {"message": "Item deleted"}