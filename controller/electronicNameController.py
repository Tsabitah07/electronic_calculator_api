from sqlalchemy.orm import Session
from fastapi import HTTPException
import models.ElectronicName as models
import schema.electronicResponse as schema

# CREATE
def create_item(db: Session, item: schema.ResponseNameCreate):
    db_item = models.ElectronicName(
        name=item.name
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# READ ALL
def read_items(db: Session):
    return db.query(models.ElectronicName).all()

# READ ONE
def read_item(db: Session, id: int):
    item = db.query(models.ElectronicName).filter(models.ElectronicName.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# UPDATE
def update_item(db: Session, id: int, new_data: schema.ResponseNameCreate):
    item = db.query(models.ElectronicName).filter(models.ElectronicName.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item.name = new_data.name

    db.commit()
    db.refresh(item)
    return item

# DELETE
def delete_item(db: Session, id: int):
    item = db.query(models.ElectronicName).filter(models.ElectronicName.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(item)
    db.commit()
    return {"message": "Item deleted"}

