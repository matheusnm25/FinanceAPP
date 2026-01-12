from app.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    is_active = Column(Boolean, default=True)

    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    permission_id = Column(Integer, ForeignKey("permissions.id"), nullable=False)

    company = relationship("Company", back_populates="users")
    permission_id = Column(
    Integer,
    ForeignKey("permissions.id"),
    nullable=False
)