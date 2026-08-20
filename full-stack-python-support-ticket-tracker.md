# Objective

Build a complete full-stack Python application that allows users to create, view, update, and delete support tickets.

You will build and connect:

**Browser UI → REST API → Application Logic → Database**

The goal of this assignment is not to build a visually impressive application. The goal is to demonstrate that you can take a set of requirements and turn them into working software.

---

## Scenario

Your team needs a lightweight internal application for tracking technical support requests. Each ticket must contain:

- `id`
- `title`
- `description`
- `priority`
- `status`
- `created_at`

### Valid Priorities

```text
low
medium
high
```

### Valid Statuses

```text
open
in_progress
closed
```

---

## Required Technology

Use:

- Python
- FastAPI
- Pydantic
- SQLite
- pytest

Do not use a JavaScript frontend framework for the required implementation.

---

## Part 1: Build the API

Implement the following endpoints.

### Create a Ticket

```http
POST /tickets
```

Example request:

```json
{
  "title": "VPN connection failing",
  "description": "User cannot connect to the corporate VPN.",
  "priority": "high"
}
```

A newly created ticket should default to:

```text
status = open
```

The server is responsible for generating:

- `id`
- `created_at`

### Get All Tickets

```http
GET /tickets
```

Return all currently stored tickets.

### Get One Ticket

```http
GET /tickets/{ticket_id}
```

Return the requested ticket.

If the ticket does not exist, return an appropriate HTTP error.

### Update a Ticket

```http
PUT /tickets/{ticket_id}
```

Allow the user to modify:

- `title`
- `description`
- `priority`
- `status`

### Delete a Ticket

```http
DELETE /tickets/{ticket_id}
```

Remove the ticket from the database.

Attempting to retrieve the deleted ticket afterward should return `404`.

---

## Part 2: Validate Requests

Use Pydantic models to define the application's request and response structures.

Your application must reject invalid requests.

Examples include:

- Missing required fields
- Invalid priority values
- Invalid status values
- Incorrect data types

Do not rely on the database to perform all input validation.

---

## Part 3: Add Persistence

Tickets must survive an application restart.

For example:

```text
Start application
      ↓
Create ticket
      ↓
Stop application
      ↓
Restart application
      ↓
GET /tickets
      ↓
Ticket still exists
```

A Python list or dictionary is not sufficient persistence.

---

## Part 4: Build the Browser Interface

Create a simple web page for interacting with the application.

The browser must allow a user to:

- View existing tickets
- Create a ticket
- Change a ticket's status
- Delete a ticket

Your frontend must communicate with the FastAPI backend using HTTP.

For example:

```javascript
fetch("/tickets")
```

The page does not need sophisticated styling.

Functional is more important than beautiful.

---

## Part 5: Write Tests

Use pytest.

At minimum, test the following behaviors:

- Creating a valid ticket succeeds
- Invalid ticket input is rejected
- Getting an existing ticket succeeds
- Getting a nonexistent ticket returns `404`
- Updating a ticket changes the persisted record
- Deleting a ticket removes the record

Tests should communicate the behavior they are proving.

Prefer:

```python
def test_get_nonexistent_ticket_returns_404():
```

over:

```python
def test1():
```

---

## Part 6: Handle Errors

Your application should fail predictably.

Consider what should happen when:

```http
GET /tickets/99999
```

or:

```http
DELETE /tickets/99999
```

or when the client submits:

```json
{
  "title": "Broken laptop",
  "description": "Screen is black",
  "priority": "URGENTEST"
}
```

Use appropriate HTTP status codes.

Be prepared to explain why the status code you selected is appropriate.

---

## Project Organization

You are responsible for deciding how to organize your application.

One possible structure is:

```text
ticket-tracker/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── database.py
│
├── static/
│   ├── app.js
│   └── style.css
│
├── templates/
│   └── index.html
│
├── tests/
│   └── test_tickets.py
│
├── requirements.txt
└── README.md
```

This structure is an example, not a requirement.

You should be able to explain the organization you chose.

---

## Definition of Done

- [ ] Application starts successfully
- [ ] Browser interface loads
- [ ] Tickets can be created
- [ ] Tickets can be retrieved
- [ ] Tickets can be updated
- [ ] Tickets can be deleted
- [ ] Invalid input is rejected
- [ ] Missing resources return appropriate errors
- [ ] DB persistence works
- [ ] Browser communicates with the REST API
- [ ] pytest tests pass
- [ ] README explains how to run the application

---

## README Requirements

Your README should explain how another developer can:

1. Clone the project
2. Create or activate the Python environment
3. Install dependencies
4. Start the application
5. Open the browser interface
6. Run the tests

Assume the person reading the README has never worked with your repository before.

---

## Final Review

When your application is complete, you should be able to demonstrate:

```text
Create Ticket
     ↓
Store in DB
     ↓
Display in Browser
     ↓
Update Ticket
     ↓
Refresh Browser
     ↓
Verify Changes Persist
     ↓
Delete Ticket
     ↓
Verify 404
     ↓
Run pytest
```
