from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from controller import electronicNameController as controller
import schema.electronicResponse as schema

router = APIRouter()

@router.post("/", response_model=schema.SingleNameResponse)
def create_electronic(item: schema.ResponseNameCreate, db: Session = Depends(get_db)):
    item = controller.create_item(db, item)
    data = {
        "message": "Successfully created electronic item",
        "status": 201,
        "data": item
    }

    return data

@router.get("/", response_model=schema.ListNameResponse)
def read_electronics(db: Session = Depends(get_db)):
    item = controller.read_items(db)
    data = {
        "message": "Successfully retrieved electronic items",
        "status": 200,
        "data": item
    }

    return data

@router.get("/{id}", response_model=schema.SingleNameResponse)
def read_electronic(id: int, db: Session = Depends(get_db)):
    item = controller.read_item(db, id)
    data = {
        "message": "Successfully retrieved electronic item",
        "status": 200,
        "data": item
    }

    return data

@router.put("/{id}", response_model=schema.SingleNameResponse)
def update_electronic(id: int, data: schema.ResponseNameCreate, db: Session = Depends(get_db)):
    item = controller.update_item(db, id, data)
    response = {
        "message": "Successfully updated electronic item",
        "status": 200,
        "data": item
    }

    return response

@router.delete("/{id}")
def delete_electronic(id: int, db: Session = Depends(get_db)):
    return controller.delete_item(db, id)

