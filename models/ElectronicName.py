from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class ElectronicName(Base):
    __tablename__ = 'electronic_name'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250), nullable=False)

    # electronic_data = relationship(
    #     "ElectronicData",
    #     back_populates="name_rel",
    #     cascade="all, delete-orphan",
    #     passive_deletes=True
    # )