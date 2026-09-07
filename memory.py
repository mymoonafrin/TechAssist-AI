import json
import os

MEMORY_FILE = "data/conversation_memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    return []

def save_memory(memory):
    os.makedirs("data", exist_ok=True)

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, indent=4)

def add_message(role, content):
    memory = load_memory()

    memory.append({
        "role": role,
        "content": content
    })

    save_memory(memory)

def get_recent_memory(limit=6):
    memory = load_memory()

    return memory[-limit:]

def clear_memory():
    if os.path.exists(MEMORY_FILE):
        os.remove(MEMORY_FILE)