from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from . import models, schemas
from app.database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Broken Task API")


@app.get("/")
def root():
    return {"message": "Ticket API Working"}

@app.post("/tickets", response_model=schemas.TicketResponse, status_code=status.HTTP_201_CREATED)
def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    new_ticket = models.Ticket(
        id = ticket.id,
        title = ticket.title,
        description = ticket.description,
        priority = ticket.priority,
        status = ticket.status,
        created_at = ticket.created_at,
    )

    if new_ticket is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

@app.get("/tickets", response_model=list[schemas.TicketResponse])
def get_all_tickets(db: Session = Depends(get_db)):
    tickets = db.query(models.Ticket).all()
    return tickets

@app.get("/tickets/{ticket_id}", response_model=schemas.TicketResponse)
def get_ticket_by_id(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()

    if ticket is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return ticket

@app.put("/tickets/{ticket_id}", response_model=schemas.TicketResponse)
def update_ticket(ticket_id: int, ticket: schemas.TicketUpdate, db: Session = Depends(get_db)):
    myticket = db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()

    if myticket is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    myticket.title = ticket.title
    myticket.description = ticket.description
    myticket.completed = ticket.completed

    db.commit()
    db.refresh(myticket)

    return myticket

@app.delete("/ticket/{ticket_id}", status_code=status.HTTP_204_NO_CONTENT)
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