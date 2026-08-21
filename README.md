### Running the Backend of the Application:

Cloning the repository:

https://github.com/Atharva-Coforge/Jira-Assignment.git


"""
Running the Application

Requirements
------------
Python 3.9+

Setup
-----
Create a virtual environment:

    python3 -m venv .venv

Activate it:

    source .venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

Run
---
Start the backend application:

    uvicorn app.main:app --reload

The API will be available at:

    http://127.0.0.1:8000

Interactive API documentation is available at:

    http://127.0.0.1:8000/docs


### Starting the Frontend of the Application

Change the present working directory to frontend:

    cd frontend

Run the frontend of the Application using:

    python -m http.server 5500


## Response Status Codes

| Code | Status | Description |
| :--- | :--- | :--- |
| `200` | Success | Request succeeded |
| `201` | Successfully Created | Ticket created successfully | 
| `204` | Successfully Deleted | Ticket deleted successfully without returning anything | 
| `404` | Not Found | Ticket does not exist |
| `422` | Unprocessable Request | Ticket exists but not in proper format |
| `5xx` | Internal Error | Server-side issue |


## Endpoints:

GET "/" - ROOT 
POST "/tickets" - create_ticket
GET "/tickets" - get_all_tickets
GET "/tickets/{ticket_id}" - get_ticket_by_id
PUT - /tickets/{ticket_id} - update_ticket
DELETE - /ticket/{ticket_id} -  delete_ticket

## Requirements to run the Application:
fastapi==0.103.2
uvicorn==0.23.2
sqlalchemy==2.0.52
pydantic==1.10.18
pytest==7.4.4
httpx==0.24.1


## TODO:
- Make the frontend attractive.
- Write more unit tests (Currently I have only the minimum ones required).
- Setting up a debugger.
- We have a problem that if we enter an empty string in title it takes an empty string and creates a ticket with empty title and description, that should not happen.