from database import Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

class ElectronicData(Base):
    __tablename__ = 'electronic_data'

    id = Column(Integer, primary_key=True, index=True)
    name_id = Column(Integer, nullable=False)
    # name_id = Column(Integer, ForeignKey('electronic_name.id', ondelete='CASCADE'), nullable=False)
    # name_rel = relationship("ElectronicName", back_populates="electronic_data")
    type = Column(String(100), nullable=False)
    min_consumption = Column(Float, default=0)
    max_consumption = Column(Float, default=0)