from typing import List

from pydantic import BaseModel

class ResponseBase(BaseModel):
    name: str
    kwh_watt: int
    cost_per_kwh: int

class ResponseCreate(ResponseBase):
    pass

class Response(ResponseBase):
    id: int

    class Config:
        orm_mode = True

class ListResponse(BaseModel):
    message: str
    status: int
    data: List[Response]

    class Config:
        orm_mode = True

class SingleResponse(BaseModel):
    message: str
    status: int
    data: Response

    class Config:
        orm_mode = True