from typing import List, Union, Optional
from pydantic import BaseModel
from datetime import datetime
from app.models import priority_list, status_list

class TicketCreate(BaseModel):
    id: int 
    title: str 
    description: str 
    priority: priority_list
    status: status_list
    created_at: datetime

    class Config:
        orm_mode = True

class TicketUpdate(BaseModel):
    id: int 
    title: Optional[str] 
    description: Optional[str] 
    priority: priority_list
    status: status_list
    created_at: datetime

    class Config:
        orm_mode = True

class TicketResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    priority: priority_list
    status: status_list
    created_at: datetime

    class Config:
        orm_mode = True
