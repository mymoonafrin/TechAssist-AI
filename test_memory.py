from memory import add_message, get_recent_memory

add_message("user", "My printer is not working.")
add_message("assistant", "Let's troubleshoot your printer.")

memory = get_recent_memory()

print("Conversation Memory:")

for message in memory:
    print(f"{message['role']}: {message['content']}")