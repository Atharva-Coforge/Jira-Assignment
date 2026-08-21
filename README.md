## Running the Backend:

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
Start the application:

    uvicorn app.main:app --reload

The API will be available at:

    http://127.0.0.1:8000

Interactive API documentation is available at:

    http://127.0.0.1:8000/docs


Status Codes:

## Response Status Codes

| Code | Status | Description |
| :--- | :--- | :--- |
| `200` | OK | Request succeeded |
| `201` | Created | Resource created successfully | 
| `404` | Not Found | Ticket does not exist |
| `422` | Unprocessable Entity | Resource exists but not in proper format |
| `500` | Internal Error | Server-side failure |



## Endpoints:

GET "/" - ROOT 
POST "/tickets" - create_ticket
GET "/tickets" - get_all_tickets
GET "/tickets/{ticket_id}" - get_ticket_by_id
PUT - /tickets/{ticket_id} - update_ticket
DELETE - /ticket/{ticket_id} -  delete_ticket

Requirements to run 