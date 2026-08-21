const API_BASE = "http://localhost:8000";

function showMessage(id, text) {
    document.getElementById(id).innerText = text;
}

function formatTicket(ticket) {
    return "ID: " + ticket.id + "\n"
        + "Title: " + ticket.title + "\n"
        + "Description: " + ticket.description + "\n"
        + "Priority: " + ticket.priority + "\n"
        + "Status: " + ticket.status + "\n"
        + "Created: " + ticket.created_at;
}

document.getElementById("view-all-btn").onclick = async function() {
    const response = await fetch(API_BASE + "/tickets");
    const tickets = await response.json();

    if (tickets.length == 0) {
        showMessage("view-result", "No tickets.");
        return;
    }

    var text = "";
    for (var i = 0; i < tickets.length; i++) {
        text = text + formatTicket(tickets[i]) + "\n\n";
    }
    showMessage("view-result", text);
};

document.getElementById("view-one-btn").onclick = async function() {
    var id = document.getElementById("view-id").value;
    const response = await fetch(API_BASE + "/tickets/" + id);
    const ticket = await response.json();

    if (response.ok) {
        showMessage("view-result", formatTicket(ticket));
    } else {
        showMessage("view-result", "Ticket not found");
    }
};

document.getElementById("create-btn").onclick = async function() {

    var title = document.getElementById("create-title").value;
    if (title.length === 0 ){
        showMessage("create-result", "Could not create ticket because title is empty");
    }

    var description = document.getElementById("create-description").value;
    var priority = document.getElementById("create-priority").value;
    var status = document.getElementById("create-status").value;

    const response = await fetch(API_BASE + "/tickets", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title: title,
            description: description,
            priority: priority,
            status: status
        })
    });

    const ticket = await response.json();

    if (response.ok) {
        showMessage("create-result", "Created.\n\n" + formatTicket(ticket));
    } else {
        showMessage("create-result", "Could not create ticket");
    }
};

document.getElementById("update-btn").onclick = async function() {
    var id = document.getElementById("update-id").value;
    var title = document.getElementById("update-title").value;
    var description = document.getElementById("update-description").value;
    var priority = document.getElementById("update-priority").value;
    var status = document.getElementById("update-status").value;

    const response = await fetch(API_BASE + "/tickets/" + id, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title: title,
            description: description,
            priority: priority,
            status: status
        })
    });

    const ticket = await response.json();

    if (response.ok) {
        showMessage("update-result", "Updated.\n\n" + formatTicket(ticket));
    } else {
        showMessage("update-result", "Could not update ticket");
    }
};

document.getElementById("delete-btn").onclick = async function() {
    var id = document.getElementById("delete-id").value;

    const response = await fetch(API_BASE + "/ticket/" + id, {
        method: "DELETE"
    });

    if (response.ok) {
        showMessage("delete-result", "Deleted ticket " + id);
    } else {
        showMessage("delete-result", "Could not delete ticket");
    }
};
