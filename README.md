# TechAssist AI — Agentic IT Helpdesk

TechAssist AI is an agentic AI-powered IT helpdesk system designed to diagnose common technical problems, retrieve relevant troubleshooting knowledge, execute diagnostic tools, maintain conversation context, and escalate unresolved issues by creating support tickets.

The system combines Agentic AI, Retrieval-Augmented Generation (RAG), diagnostic tools, conversation memory, and automated escalation into a single interactive helpdesk application.

## Project Overview

Traditional IT helpdesk systems often depend on predefined responses or manual support processes. TechAssist AI provides an intelligent workflow that analyzes a user's request, determines the appropriate action, retrieves relevant technical knowledge, executes diagnostic tools when required, and provides a troubleshooting response.

If an issue cannot be resolved through the available troubleshooting knowledge, the system can automatically escalate the issue by creating a support ticket.

## Key Features

* Intelligent request classification
* Retrieval-Augmented Generation (RAG)
* IT troubleshooting knowledge base
* Internet connectivity diagnostics
* Host ping diagnostics
* System information detection
* Conversation memory
* Automated issue escalation
* Support ticket creation
* Interactive Streamlit web interface
* Local LLM inference using Ollama
* Lightweight architecture suitable for resource-constrained systems

## Agentic Workflow

The system follows a controlled agentic workflow:

```text
                    User Request
                         |
                         v
                 Request Classifier
                         |
          +--------------+--------------+
          |              |              |
          v              v              v
    Troubleshooting   Diagnostics     General
          |              |              |
          v              v              v
       RAG Search     Tool Execution   LLM
          |              |
          v              v
Relevant Knowledge  Diagnostic Result
          |              |
          v              |
   Troubleshooting      |
      Response          |
          |              |
          +------+-------+
                 |
                 v
          Escalation Check
                 |
        +--------+--------+
        |                 |
        v                 v
     Resolved         Unresolved
        |                 |
        |                 v
        |          Support Ticket
        |             Creation
        +--------+--------+
                 |
                 v
           Final Response
                 |
                 v
        Conversation Memory
```

## RAG Architecture

TechAssist AI uses Retrieval-Augmented Generation to provide troubleshooting information from a dedicated IT knowledge base.

The RAG pipeline consists of:

```text
Knowledge Base Documents
          |
          v
      Text Loading
          |
          v
     Text Embeddings
          |
          v
    Chroma Vector DB
          |
          v
      User Query
          |
          v
   Similarity Search
          |
          v
Relevant Troubleshooting
       Knowledge
          |
          v
     LLM Response
```

The knowledge base currently contains troubleshooting information for:

* Wi-Fi and internet connectivity
* Printer problems
* Slow computers
* Blue screen errors
* Software installation problems
* Password reset
* Network connectivity

## Diagnostic Tools

TechAssist AI includes multiple tools that allow the system to obtain information instead of relying only on generated responses.

### Internet Connectivity Tool

Checks whether the system currently has internet connectivity.

### Ping Tool

Tests connectivity to a specified host.

Example:

```text
Ping google.com
```

### System Information Tool

Retrieves information about the local system, including:

* Operating system
* OS version
* Computer name
* Machine architecture
* Processor information
* Python version

### Support Ticket Tool

Creates a local support ticket when an issue requires escalation.

Each ticket contains:

* Ticket ID
* Issue description
* Category
* Priority
* Status
* Creation timestamp

## Conversation Memory

TechAssist AI maintains local conversation memory so that previous interactions can be retained across requests.

Conversation data is stored locally in:

```text
data/conversation_memory.json
```

This file is excluded from Git using `.gitignore`.

The memory system supports:

* Saving user messages
* Saving assistant responses
* Retrieving recent conversation history
* Clearing conversation memory

## Escalation System

Not every technical problem can be resolved automatically.

TechAssist AI identifies certain unresolved or hardware-related issues and can escalate them to IT support.

Example:

```text
User:
My printer has a hardware error and still does not work.

System:
Escalation requirement detected

Support Ticket:
TKT-0001
Category: IT Troubleshooting
Priority: High
Status: Open
```

This creates a complete workflow from problem detection to human-support escalation.

## Technology Stack

| Technology              | Purpose                                 |
| ----------------------- | --------------------------------------- |
| Python 3.11             | Core programming language               |
| LangChain               | Agent and AI application framework      |
| LangChain Core          | Tool and workflow components            |
| LangChain Community     | Vector store and embedding integrations |
| LangChain Ollama        | Ollama LLM integration                  |
| Ollama                  | Local LLM runtime                       |
| Qwen 2.5 1.5B           | Local language model                    |
| ChromaDB                | Vector database                         |
| FAISS CPU               | Vector similarity support               |
| Hugging Face Embeddings | Document and query embeddings           |
| Streamlit               | Interactive web interface               |
| Pydantic                | Data validation                         |
| Rich                    | Terminal output formatting              |

## Required Packages

```text
langchain==0.2.16
langchain-core==0.2.39
langchain-community==0.2.16
langchain-ollama==0.1.3
pydantic==2.8.2
rich==13.9.4
chromadb==0.5.18
faiss-cpu==1.9.0
```

## Project Structure

```text
TechAssist-AI/
│
├── app.py
├── agent.py
├── workflow.py
├── router.py
│
├── rag.py
├── rag_chat.py
├── rag_tool.py
├── vector_db.py
│
├── tools.py
├── network_tool.py
├── ping_tool.py
├── system_info_tool.py
├── ticket_tool.py
│
├── memory.py
│
├── requirements.txt
├── .gitignore
│
├── data/
│   └── knowledge_base/
│       ├── blue_screen.txt
│       ├── network.txt
│       ├── password_reset.txt
│       ├── printer.txt
│       ├── slow_computer.txt
│       ├── software_installation.txt
│       └── wifi.txt
│
└── venv/
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/mymoonafrin/TechAssist-AI.git
```

Move into the project directory:

```bash
cd TechAssist-AI
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Install Ollama and make sure it is available from the terminal.

Verify the installation:

```bash
ollama --version
```

### 5. Pull the Language Model

This project uses Qwen 2.5 1.5B:

```bash
ollama pull qwen2.5:1.5b
```

Verify that the model is available:

```bash
ollama list
```

## Building the Vector Database

Before using the RAG functionality, create the vector database from the knowledge base:

```bash
python vector_db.py
```

The generated Chroma database is stored locally in:

```text
data/chroma_db/
```

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in the browser.

The local Streamlit address is:

```text
http://localhost:8501
```

## Example Queries

### Troubleshooting

```text
My Wi-Fi is connected but I have no internet.
```

```text
My printer is not printing.
```

```text
My computer is very slow.
```

```text
My computer keeps showing a blue screen.
```

```text
I cannot install my software.
```

```text
I forgot my password.
```

### Diagnostics

```text
Check my internet connection.
```

```text
Ping google.com
```

```text
What operating system am I using?
```

### Escalation

```text
My printer has a hardware error and still does not work.
```

The system can identify the issue as requiring escalation and create a support ticket.

## Agent Decision Flow

TechAssist AI classifies incoming requests into different workflow categories.

```text
User Query
    |
    v
Request Classification
    |
    +---- Troubleshooting
    |          |
    |          v
    |      RAG Search
    |          |
    |          v
    |    Generate Solution
    |
    +---- Internet Check
    |          |
    |          v
    |    Network Diagnostic
    |
    +---- Ping
    |          |
    |          v
    |      Ping Tool
    |
    +---- System Information
    |          |
    |          v
    |    System Info Tool
    |
    +---- General Query
               |
               v
            LLM Response
```

## Why RAG is Used

A general language model may generate technically incorrect or outdated troubleshooting instructions.

RAG improves reliability by retrieving information from a controlled IT knowledge base before generating troubleshooting guidance.

This allows TechAssist AI to:

* Ground responses in stored technical knowledge
* Reduce unsupported troubleshooting suggestions
* Provide consistent troubleshooting procedures
* Extend the knowledge base with additional documents

## Why Tools are Used

Some questions require real system information rather than generated knowledge.

For example:

```text
What operating system am I using?
```

is better answered using a system information tool than asking the language model to guess.

Similarly:

```text
Check my internet connection.
```

requires an actual connectivity check.

Tools therefore allow the system to interact with the local environment and perform real diagnostics.

## Why Escalation is Used

An IT helpdesk should not attempt to solve every problem automatically.

When an issue appears to require human intervention, TechAssist AI can create a support ticket instead of repeatedly generating troubleshooting instructions.

This provides a path from:

```text
AI Diagnosis
      |
      v
Troubleshooting
      |
      v
Issue Still Unresolved
      |
      v
Human Support Escalation
```

## User Interface

The application provides an interactive Streamlit interface containing:

* TechAssist AI dashboard
* Chat interface
* Quick troubleshooting actions
* Conversation history
* Workflow activity display
* System diagnostics
* Support escalation information

## Future Enhancements

Potential future improvements include:

* Integration with enterprise ticketing systems
* Email notifications for escalated tickets
* User authentication
* Real-time network monitoring
* Additional diagnostic tools
* Larger enterprise IT knowledge bases
* Automatic ticket prioritization
* Multi-user support
* Cloud deployment
* More advanced agent planning
* Integration with ServiceNow or Jira
* Voice-based IT support
* Continuous knowledge-base updates

## Project Objective

The primary objective of TechAssist AI is to demonstrate how Agentic AI can be applied to IT support by combining:

```text
Agentic Workflow
       +
RAG
       +
LLM
       +
Diagnostic Tools
       +
Conversation Memory
       +
Escalation
```

Together, these components create an intelligent IT helpdesk capable of understanding user requests, retrieving relevant technical information, performing diagnostics, maintaining context, and escalating unresolved issues.

## Conclusion

TechAssist AI demonstrates a practical implementation of an agentic IT helpdesk using locally hosted AI.

Instead of functioning only as a chatbot, the system combines reasoning, retrieval, tools, memory, and escalation to create a complete technical-support workflow.

The architecture is designed to be lightweight, modular, extensible, and suitable for further development into a production-oriented IT support assistant.

## Author

**N. Mymoon Afrin**


