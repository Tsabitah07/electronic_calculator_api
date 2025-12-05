from database import Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

class ElectronicData(Base):
    __tablename__ = 'electronic_data'

    id = Column(Integer, primary_key=True, index=True)
    name_id = Column(Integer, nullable=False)
    type = Column(String(100), nullable=False)
    min_consumption = Column(Float, default=0)
    max_consumption = Column(Float, default=0)