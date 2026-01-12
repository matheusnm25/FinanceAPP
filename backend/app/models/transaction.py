from app.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy import Enum
import enum

class TransactionType(enum.Enum):
    income = "income"
    expense = "expense"

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    description = Column(String)
    amount = Column(Float, nullable=False)
    type = Column(Enum(TransactionType), nullable=False)
    currency = Column(String(3), nullable=False)
    date = Column(Date, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"))
    group_id = Column(Integer, ForeignKey("groups.id"))

    user = relationship("User")
    company = relationship("Company")
    category = relationship("Category")
    group = relationship("Group")