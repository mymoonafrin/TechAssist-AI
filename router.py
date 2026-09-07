import re

def classify_request(query, conversation=""):
    text = query.lower().strip()

    ping_patterns = [
        r"\bping\b",
        r"\bpinging\b",
        r"\bping test\b"
    ]

    system_patterns = [
        "operating system",
        "os version",
        "system information",
        "system info",
        "computer information",
        "computer specs",
        "computer specification",
        "processor",
        "cpu",
        "ram",
        "machine information",
        "what system am i using",
        "what operating system"
    ]

    internet_patterns = [
        "check my internet",
        "check internet",
        "test my internet",
        "test internet",
        "is my internet working",
        "internet connection available",
        "internet connectivity check"
    ]

    troubleshooting_patterns = [
        "printer",
        "printing",
        "print",
        "wi-fi",
        "wifi",
        "wireless",
        "internet not working",
        "no internet",
        "cannot access the internet",
        "can't access the internet",
        "cannot connect to internet",
        "can't connect to internet",
        "network problem",
        "network issue",
        "network connectivity",
        "computer is slow",
        "computer slow",
        "computer is very slow",
        "computer has become slow",
        "laptop is slow",
        "laptop slow",
        "laptop is very slow",
        "slow computer",
        "slow laptop",
        "blue screen",
        "bsod",
        "system crash",
        "computer crash",
        "computer crashes",
        "software installation",
        "software install",
        "install software",
        "cannot install",
        "can't install",
        "unable to install",
        "installation problem",
        "installation issue",
        "forgot my password",
        "forgot password",
        "password reset",
        "reset my password",
        "password problem",
        "password issue",
        "account locked",
        "account access",
        "hardware error",
        "hardware failure",
        "hardware problem",
        "still not working",
        "still doesn't work",
        "still does not work",
        "problem persists",
        "issue persists",
        "troubleshooting"
    ]

    for pattern in ping_patterns:
        if re.search(pattern, text):
            return "ping"

    for pattern in system_patterns:
        if pattern in text:
            return "system_info"

    for pattern in internet_patterns:
        if pattern in text:
            return "internet_check"

    if (
        ("computer" in text or "laptop" in text)
        and (
            "slow" in text
            or "slower" in text
            or "performance" in text
        )
    ):
        return "troubleshoot"

    for pattern in troubleshooting_patterns:
        if pattern in text:
            return "troubleshoot"

    return "general"


if __name__ == "__main__":
    test_queries = [
        "My Wi-Fi is connected but I have no internet.",
        "My printer is not printing.",
        "My computer is very slow.",
        "My computer keeps showing a blue screen.",
        "I cannot install my software.",
        "I forgot my password.",
        "Check my internet connection.",
        "Ping google.com",
        "What operating system am I using?",
        "My printer has a hardware error and still does not work.",
        "What is the weather today?"
    ]

    for query in test_queries:
        print(f"{query} -> {classify_request(query)}")