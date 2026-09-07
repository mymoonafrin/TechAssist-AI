import json
import os
from datetime import datetime
from langchain_core.tools import tool

TICKET_FILE = "data/tickets.json"

@tool
def create_support_ticket(issue: str, category: str, priority: str = "Medium"):
    """Create a local IT support ticket for an unresolved technical issue."""

    os.makedirs("data", exist_ok=True)

    if os.path.exists(TICKET_FILE):
        with open(TICKET_FILE, "r", encoding="utf-8") as file:
            tickets = json.load(file)
    else:
        tickets = []

    ticket_id = f"TKT-{len(tickets) + 1:04d}"

    ticket = {
        "ticket_id": ticket_id,
        "issue": issue,
        "category": category,
        "priority": priority,
        "status": "Open",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    tickets.append(ticket)

    with open(TICKET_FILE, "w", encoding="utf-8") as file:
        json.dump(tickets, file, indent=4)

    return (
        f"Support ticket created successfully.\n"
        f"Ticket ID: {ticket_id}\n"
        f"Category: {category}\n"
        f"Priority: {priority}\n"
        f"Status: Open"
    )

if __name__ == "__main__":
    result = create_support_ticket.invoke({
        "issue": "Printer continues to show a hardware error after troubleshooting.",
        "category": "Printer",
        "priority": "High"
    })

    print("TechAssist Ticket System:")
    print(result)