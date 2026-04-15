# 🧠 Local AI Code Agent

A simple local AI-powered coding agent built on top of a local LLM (via llama.cpp-compatible API).

The agent can:

* read files
* write files
* maintain conversation state
* execute actions based on structured JSON output from the model

---

## 🚀 Features

* 🔁 Interactive agent loop (CLI)
* 🧠 LLM-driven decision making
* 🛠 Tool system (extensible)
* 📂 File system interaction:

  * read files
  * write files
* 💬 Persistent message context
* 📦 Modular architecture (agent / llm / tools)

---

## ⚙️ Architecture Overview

The system is split into logical components:

```
User Input
   ↓
Agent Loop
   ↓
LLM (chat completion)
   ↓
JSON Action
   ↓
Handler (dispatch)
   ↓
Tools (execution)
   ↓
Result → back to context
```

### Components

#### `agent/`

* `loop.py` — main execution loop
* `state.py` — initial system prompt & message state
* `handler.py` — routes actions to tools

#### `llm/`

* `llm_client.py` — API communication with local model
* `payload_builder.py` — builds request payload

#### `tools/`

* `read_file.py`
* `write_file.py`
* `say.py`
* `registry.py` — tool mapping

#### `config.py`

* model name
* API URL
* temperature

---

## 🧩 How It Works

The model is instructed to output strict JSON:

```json
{
  "action": "write_file",
  "file_path": "index.html",
  "content": "<html>...</html>"
}
```

The agent:

1. Sends user input to the model
2. Receives JSON response
3. Parses it
4. Executes the corresponding tool
5. Feeds the result back into the conversation

---

## 📦 Requirements

* Python 3.10+
* Running local LLM server (llama.cpp or compatible)

Example:

```bash
./llama-server -m model.gguf
```

---

## ⚡ Usage

```bash
python main.py
```

Then interact:

```
>>> Create a file index.html
>>> Read file index.html
```

---

## 🔧 Configuration

Edit `config.py`:

```python
API_URL = "http://127.0.0.1:8080"
MODEL_NAME = "your-model.gguf"
TEMP = 0.3
```

---

## 🛠 Available Tools

| Tool         | Description        |
| ------------ | ------------------ |
| `say`        | Prints text        |
| `write_file` | Writes a file      |
| `read_file`  | Reads file content |

---

## ⚠️ Known Issues

* Model may sometimes return invalid JSON
* Unicode issues may occur with long outputs
* No retry mechanism (yet)
* No sandboxing for file operations

---

## 🔮 Future Improvements

* [ ] Tool calling via Jinja templates
* [ ] Multi-step reasoning loop
* [ ] Planner → Executor architecture
* [ ] File context awareness
* [ ] Retry / error recovery system
* [ ] JSON schema validation
* [ ] Multi-agent support

---

## 📚 Motivation

This project is an experiment in building a minimal local AI agent system:

* without external frameworks
* with full control over logic
* focused on understanding LLM orchestration

---

## 🧪 Status

**MVP — functional but evolving**

---

## 💡 Notes

This is not production-ready.
The goal is learning and experimentation.

---

## 🧑‍💻 Author

Built as part of exploration into:

* LLM agents
* local inference
* tool-based execution systems
