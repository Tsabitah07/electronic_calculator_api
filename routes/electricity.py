from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from controller import electricityController as controller
import schema.electricityResponse as schema

router = APIRouter()


@router.post("/", response_model=schema.SingleResponse)
def create_electricity(item: schema.ResponseCreate, db: Session = Depends(get_db)):
    item = controller.create_item(db, item)
    data = {
        "message": "Successfully created electricity item",
        "status": 201,
        "data": item
    }

    return data

@router.get("/", response_model=schema.ListResponse)
def read_electricities(db: Session = Depends(get_db)):
    item = controller.read_items(db)
    data = {
        "message": "Successfully retrieved electricity items",
        "status": 200,
        "data": item
    }

    return data


@router.get("/{id}", response_model=schema.SingleResponse)
def read_electricity(id: int, db: Session = Depends(get_db)):
    item = controller.read_item(db, id)
    data = {
        "message": "Successfully retrieved electricity item",
        "status": 200,
        "data": item
    }

    return data


@router.put("/{id}", response_model=schema.SingleResponse)
def update_electricity(id: int, data: schema.ResponseCreate, db: Session = Depends(get_db)):
    item = controller.update_item(db, id, data)
    response = {
        "message": "Successfully updated electricity item",
        "status": 200,
        "data": item
    }

    return response


@router.delete("/{id}")
def delete_electricity(id: int, db: Session = Depends(get_db)):
    return controller.delete_item(db, id)