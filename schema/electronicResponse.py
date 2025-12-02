from typing import List, Optional
from pydantic import BaseModel

class ResponseNameBase(BaseModel):
    name: str

class ResponseDataBase(BaseModel):
    name: Optional[str] = None
    type: str
    min_consumption: int
    max_consumption: int

class ResponseNameCreate(ResponseNameBase):
    pass

class ResponseDataCreate(ResponseDataBase):
    name_id: int

class ResponseName(ResponseNameBase):
    id: int

    class Config:
        orm_mode = True

class ResponseData(ResponseDataBase):
    id: int
    name_id: int

    class Config:
        orm_mode = True

class ListResponse(BaseModel):
    message: str
    status: int
    data: List[ResponseData]

    class Config:
        orm_mode = True

class SingleResponse(BaseModel):
    message: str
    status: int
    data: ResponseData

    class Config:
        orm_mode = True

class ListNameResponse(BaseModel):
    message: str
    status: int
    data: List[ResponseName]

    class Config:
        orm_mode = True

class SingleNameResponse(BaseModel):
    message: str
    status: int
    data: ResponseName

    class Config:
        orm_mode = True