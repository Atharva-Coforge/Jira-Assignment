from sqlalchemy import Integer, String, Column, Boolean, func, Enum, DateTime
from app.database import Base
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
import datetime, enum

class priority_list(enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class status_list(enum.Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    priority = Column(Enum(priority_list), nullable=False, default=priority_list.LOW)
    status = Column(Enum(status_list), nullable=False, default=status_list.OPEN)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

