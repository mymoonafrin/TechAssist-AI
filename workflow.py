from langchain_ollama import ChatOllama

from router import classify_request
from rag_tool import search_knowledge_base
from tools import check_internet, get_system_info, ping_host
from ticket_tool import create_support_ticket
from memory import add_message, get_recent_memory


llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)


def format_memory():
    memory = get_recent_memory(6)

    if not memory:
        return ""

    formatted = []

    for message in memory:
        role = message.get("role", "")
        content = message.get("content", "")

        if role == "user":
            formatted.append(f"User: {content}")
        elif role == "assistant":
            formatted.append(f"Assistant: {content}")

    return "\n".join(formatted)


def generate_general_response(query):
    memory = format_memory()

    prompt = f"""
You are TechAssist AI, an IT helpdesk assistant.

Answer the user's question clearly and briefly.

Conversation history:
{memory}

Current user request:
{query}

Give a helpful answer.
Do not invent technical facts.
"""

    response = llm.invoke(prompt)

    return response.content.strip()


def extract_troubleshooting_content(document):
    text = document

    if "Troubleshooting Steps:" in text:
        text = text.split("Troubleshooting Steps:", 1)[1]

    if "Escalation:" in text:
        text = text.split("Escalation:", 1)[0]

    return text.strip()


def generate_troubleshooting_response(query, knowledge):
    memory = format_memory()

    prompt = f"""
You are TechAssist AI, an IT helpdesk assistant.

The user has reported an IT problem.

Use the knowledge base information below to provide troubleshooting instructions.

Knowledge base:
{knowledge}

Conversation history:
{memory}

Current user problem:
{query}

Instructions:
- Give practical troubleshooting steps.
- Preserve all relevant steps from the knowledge base.
- Do not remove important steps.
- Do not invent steps that are not supported by the knowledge base.
- Number the steps clearly.
- If the knowledge base contains escalation guidance, mention it when appropriate.
- Keep the answer easy for a beginner to follow.
"""

    response = llm.invoke(prompt)

    return response.content.strip()


def should_escalate(query):
    text = query.lower()

    escalation_patterns = [
        "hardware error",
        "hardware failure",
        "hardware problem",
        "hardware issue",
        "still not working",
        "still doesn't work",
        "still does not work",
        "problem persists",
        "issue persists",
        "keeps crashing",
        "keeps showing",
        "repeatedly crashes",
        "cannot fix",
        "can't fix",
        "unable to fix",
        "tried everything",
        "nothing works",
        "nothing worked"
    ]

    for pattern in escalation_patterns:
        if pattern in text:
            return True

    return False


def determine_ticket_category(query):
    text = query.lower()

    if "printer" in text or "printing" in text or "print" in text:
        return "Printer"

    if "wifi" in text or "wi-fi" in text or "wireless" in text:
        return "Wi-Fi"

    if "network" in text or "internet" in text:
        return "Network"

    if "password" in text or "account" in text:
        return "Account Access"

    if "software" in text or "install" in text or "installation" in text:
        return "Software"

    if "blue screen" in text or "bsod" in text or "crash" in text:
        return "System Crash"

    if "slow" in text or "performance" in text:
        return "Computer Performance"

    return "IT Troubleshooting"


def determine_priority(query):
    text = query.lower()

    high_priority_patterns = [
        "hardware error",
        "hardware failure",
        "system crash",
        "blue screen",
        "bsod",
        "security",
        "account locked",
        "cannot access",
        "critical"
    ]

    for pattern in high_priority_patterns:
        if pattern in text:
            return "High"

    return "Medium"


def process_request(query):
    activity = []

    category = classify_request(query)
    activity.append(f"Request classified → {category}")

    if category == "troubleshoot":
        knowledge = search_knowledge_base.invoke(query)

        activity.append("Knowledge base searched")
        activity.append("Relevant troubleshooting knowledge retrieved")

        knowledge_text = extract_troubleshooting_content(knowledge)

        response = generate_troubleshooting_response(
            query,
            knowledge_text
        )

        activity.append("Troubleshooting response generated")

        if should_escalate(query):
            activity.append("Escalation requirement detected")

            ticket_category = determine_ticket_category(query)
            priority = determine_priority(query)

            ticket_result = create_support_ticket.invoke({
                "issue": query,
                "category": ticket_category,
                "priority": priority
            })

            activity.append("Support ticket created")

            response = (
                f"{response}\n\n"
                f"Escalation:\n"
                f"{ticket_result}"
            )

    elif category == "internet_check":
        activity.append("Internet diagnostic tool executed")

        diagnostic_result = check_internet.invoke({})

        activity.append("Diagnostic result received")

        response = (
            "Internet Connectivity Check:\n\n"
            f"{diagnostic_result}"
        )

    elif category == "ping":
        parts = query.split()

        host = ""

        for part in parts:
            cleaned = part.strip(".,!?")

            if (
                "." in cleaned
                or cleaned.lower() == "localhost"
                or cleaned.replace("-", "").isalnum()
            ):
                if cleaned.lower() not in ["ping", "pinging", "test"]:
                    host = cleaned
                    break

        if not host:
            host = "google.com"

        activity.append(f"Ping diagnostic executed → {host}")

        diagnostic_result = ping_host.invoke({
            "host": host
        })

        activity.append("Ping diagnostic result received")

        response = (
            f"Ping Diagnostic for {host}:\n\n"
            f"{diagnostic_result}"
        )

    elif category == "system_info":
        activity.append("System information tool executed")

        system_result = get_system_info.invoke({})

        activity.append("System information retrieved")

        response = (
            "System Information:\n\n"
            f"{system_result}"
        )

    else:
        response = generate_general_response(query)

        activity.append("General AI response generated")

    add_message("user", query)
    add_message("assistant", response)

    activity.append("Response delivered")

    return response, activity


if __name__ == "__main__":
    print("TechAssist AI")
    print('Type "exit" to quit.')

    while True:
        query = input("\nYou: ").strip()

        if query.lower() == "exit":
            print("Goodbye!")
            break

        if not query:
            continue

        response, activity = process_request(query)

        print("\nActivity:")
        for item in activity:
            print(f"- {item}")

        print("\nTechAssist AI:")
        print(response)