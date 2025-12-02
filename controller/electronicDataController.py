from sqlalchemy.orm import Session
from fastapi import HTTPException
import models.ElectronicData as ed_models
import models.ElectronicName as name_models
import schema.electronicResponse as schema

# CREATE
def create_item(db: Session, item: schema.ResponseDataCreate):
    name_obj = db.query(name_models.ElectronicName).filter(name_models.ElectronicName.id == item.name_id).first()
    if not name_obj:
        raise HTTPException(status_code=400, detail="name_id does not exist in electronic_name")

    db_item = ed_models.ElectronicData(
        name_id=item.name_id,
        type=item.type,
        min_consumption=item.min_consumption,
        max_consumption=item.max_consumption
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    db_item.name = name_obj.name
    return db_item

# READ ALL
def read_items(db: Session, name_id: int = None):
    query = db.query(ed_models.ElectronicData)

    if name_id is not None:
        items = query.filter(ed_models.ElectronicData.name_id == name_id).all()
    else:
        items = query.all()

    for it in items:
        name_obj = db.query(name_models.ElectronicName)\
                     .filter(name_models.ElectronicName.id == it.name_id)\
                     .first()
        it.name = name_obj.name if name_obj else None

    return items

# READ ONE
def read_item(db: Session, name_id: int = None):
    items = db.query(ed_models.ElectronicData).filter(
        ed_models.ElectronicData.name_id == name_id
    ).all()

    for item in items:
        name_obj = db.query(name_models.ElectronicName).filter(
            name_models.ElectronicName.id == item.name_id
        ).first()
        item.name = name_obj.name if name_obj else None

    return items

# UPDATE
def update_item(db: Session, id: int, new_data: schema.ResponseDataCreate):
    item = db.query(ed_models.ElectronicData).filter(ed_models.ElectronicData.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    name_obj = db.query(name_models.ElectronicName).filter(name_models.ElectronicName.id == new_data.name_id).first()
    if not name_obj:
        raise HTTPException(status_code=400, detail="name_id does not exist in electronic_name")

    item.name_id = new_data.name_id
    item.type = new_data.type
    item.min_consumption = new_data.min_consumption
    item.max_consumption = new_data.max_consumption

    db.commit()
    db.refresh(item)

    item.name = name_obj.name
    return item

# DELETE
def delete_item(db: Session, id: int):
    item = db.query(ed_models.ElectronicData).filter(ed_models.ElectronicData.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(item)
    db.commit()
    return {"message": "Item deleted"}