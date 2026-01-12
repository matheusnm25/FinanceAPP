from app.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)  # personal | business
    cnpj = Column(String)

    users = relationship("User", back_populates="company")
    groups = relationship("Group", back_populates="company")
    categories = relationship("Category", back_populates="company")