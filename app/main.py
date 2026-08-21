from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from . import models, schemas
from app.database import Base, engine, get_db
from fastapi.responses import FileResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ticket Management API")

origins = [
    "http://localhost:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,         
    allow_methods=["*"],         
    allow_headers=["*"],            
)

@app.get("/")
def root():
    return {"message" : "Working fine!"}

@app.post("/tickets", response_model=schemas.TicketResponse, status_code=status.HTTP_201_CREATED)
def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    new_ticket = models.Ticket(
        title = ticket.title,
        description = ticket.description,
        priority = ticket.priority,
        status = ticket.status,
    )

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

@app.get("/tickets")
def get_all_tickets(db: Session = Depends(get_db)):
    return db.query(models.Ticket).all()

@app.get("/tickets/{ticket_id}", response_model=schemas.TicketResponse)
def get_ticket_by_id(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()

    if ticket is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ticket not found",
        )

    return ticket

@app.put("/tickets/{ticket_id}", response_model=schemas.TicketResponse)
def update_ticket(ticket_id: int, ticket: schemas.TicketUpdate, db: Session = Depends(get_db)):
    myticket = db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()

    if myticket is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ticket not found",
        )

    myticket.title = ticket.title
    myticket.description = ticket.description
    myticket.priority = ticket.priority
    myticket.status = ticket.status

    db.commit()
    db.refresh(myticket)

    return myticket

@app.delete("/tickets/{ticket_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()

    if ticket is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ticket not found",
        )

    db.delete(ticket)
    db.commit()

    return