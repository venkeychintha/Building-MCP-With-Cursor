# Building-MCP-With-Cursor
# Multi-Server MCP Agent with LangGraph and OpenAI

This project demonstrates how to build an **AI agent using LangGraph and the Model Context Protocol (MCP)** by integrating multiple tool servers into a single intelligent workflow.

The agent connects to:

* **Math MCP Server** → performs arithmetic operations
* **Weather MCP Server** → returns weather information
* **OpenAI GPT model** → handles reasoning and tool selection

This project showcases **multi-tool orchestration**, **MCP server integration**, and **agent-based reasoning workflows**.

---

## 🚀 Features

* Multi-server MCP integration
* LangGraph ReAct Agent
* OpenAI-powered reasoning
* Math tool server
* Weather tool server
* Async Python workflow
* Supports multiple transports:

  * `stdio`
  * `streamable-http`

---

## 📁 Project Structure

```bash
.
├── main.py
├── mathserver.py
├── weather.py
├── client.py
├── requirements.txt
└── README.md
```

### File Details

* **main.py** → Main AI agent orchestration logic 
* **mathserver.py** → MCP math tool server 
* **weather.py** → MCP weather tool server 
* **requirements.txt** → Project dependencies 

---

## 🛠 Technologies Used

* Python
* LangChain
* LangGraph
* MCP (Model Context Protocol)
* FastMCP
* OpenAI API
* AsyncIO

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/multi-server-mcp-agent.git
cd multi-server-mcp-agent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Dependencies: 

```txt
langchain-groq
langchain-mcp-adapters
mcp
langgraph
langchain_openai
```

---

## 🔐 Environment Setup

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## ▶️ Running the Project

### Step 1: Start Weather MCP Server

Run the weather server first:

```bash
python weather.py
```

This starts the server using **HTTP streaming transport**.

---

### Step 2: Run Main Agent

In another terminal:

```bash
python main.py
```

The agent will automatically connect to:

* Math server
* Weather server
* OpenAI model

and invoke the correct tools based on user queries.

---

## 💡 Example Output

```bash
Math response: 96
Weather response: It is always raining in the California
```

---

## 🔧 Available MCP Tools

### Math Server

Available tools: 

```python
add(a: int, b: int)
multiply(a: int, b: int)
```

Example:

```python
add(3, 5)
multiply(8, 12)
```

---

### Weather Server

Available tool: 

```python
get_weather(city: str)
```

Example:

```python
get_weather("California")
```

---

## 🧠 How It Works

The `MultiServerMCPClient` connects multiple MCP servers:

```python
client = MultiServerMCPClient({...})
```

It fetches tools dynamically:

```python
tools = await client.get_tools()
```

A LangGraph ReAct agent is created:

```python
agent = create_react_agent(model, tools)
```

The agent automatically decides which tool to call based on the user prompt.

---

## 📚 Learning Outcomes

This project helps in understanding:

* AI agent architecture
* MCP server design
* Multi-tool orchestration
* LangGraph workflows
* Async agent execution
* LLM-based tool routing

---

## 🚀 Future Enhancements

* Integrate real weather API
* Add division / advanced math tools
* Add database tool integration
* Add file system MCP tools
* Support multi-agent workflows
* Add memory support

---

## 👨‍💻 Author

Built as a hands-on project for learning **MCP + LangGraph + AI Agent orchestration**.
