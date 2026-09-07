from router import classify_request

queries = [
    "What does an IT helpdesk do?",
    "My printer is not printing. How can I fix it?",
    "My laptop is connected to Wi-Fi but I cannot access the internet.",
    "Can you check whether my computer has internet access?",
    "Can you check whether google.com is reachable?",
    "What processor is installed on my computer?"
]

for query in queries:
    category = classify_request(query)

    print("\nUser:", query)
    print("Category:", category)