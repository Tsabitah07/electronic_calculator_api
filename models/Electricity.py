from sqlalchemy import Column, Integer, String
from database import Base

class Electricity(Base):
    __tablename__ = "electricity"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    kwh_watt = Column(Integer)
    cost_per_kwh = Column(Integer)
