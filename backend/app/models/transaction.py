from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from app.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    amount = Column(Float)
    type = Column(String)  # income | expense
    category = Column(String)
    date = Column(Date)
    user_id = Column(Integer, ForeignKey("users.id"))