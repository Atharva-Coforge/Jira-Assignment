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

document.getElementById("delete-btn").onclick = async function() {

}