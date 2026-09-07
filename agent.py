from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage

from tools import check_internet, get_system_info, ping_host
from rag_tool import search_knowledge_base

llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

tools = [
    check_internet,
    get_system_info,
    ping_host,
    search_knowledge_base
]

tool_map = {
    "check_internet": check_internet,
    "get_system_info": get_system_info,
    "ping_host": ping_host,
    "search_knowledge_base": search_knowledge_base
}

llm_with_tools = llm.bind_tools(tools)

system_message = SystemMessage(
    content="""
You are TechAssist AI, an IT helpdesk agent.

You have access to four tools.

Use check_internet when the user asks whether their computer has internet connectivity.

Use get_system_info when the user asks about their computer operating system, machine, processor, Python version, or other system information.

Use ping_host when the user asks whether a specific website, server, hostname, or IP address is reachable.

Use search_knowledge_base when the user describes an IT problem and needs troubleshooting instructions. This includes Wi-Fi problems, printer problems, slow computers, blue screen errors, software installation problems, password problems, and general network problems.

If the user describes an IT problem that requires troubleshooting, search the knowledge base before giving troubleshooting instructions.

Do not invent troubleshooting steps that are not supported by the knowledge base.

When a tool is appropriate, use the tool instead of simply explaining what the tool could do.

After receiving a tool result, provide a clear answer to the user.

Do not interpret AMD64 as an AMD processor. AMD64 describes the system architecture. Use the processor field when identifying the processor.
"""
)

print("TechAssist AI")
print("Type 'exit' to quit.")

while True:
    query = input("\nYou: ")

    if query.lower() == "exit":
        print("TechAssist AI: Goodbye!")
        break

    messages = [
        system_message,
        HumanMessage(content=query)
    ]

    response = llm_with_tools.invoke(messages)

    messages.append(response)

    if response.tool_calls:
        print("\nTools selected:")

        for tool_call in response.tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]

            print(f"- {tool_name}")

            selected_tool = tool_map[tool_name]
            tool_result = selected_tool.invoke(tool_args)

            messages.append(
                ToolMessage(
                    content=str(tool_result),
                    tool_call_id=tool_call["id"]
                )
            )

        final_response = llm.invoke(messages)

        print(f"\nTechAssist AI: {final_response.content}")

    else:
        print(f"\nTechAssist AI: {response.content}")