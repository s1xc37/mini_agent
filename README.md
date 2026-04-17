# 🧠 mini_agent

A local AI-powered coding agent built on top of a local LLM through a llama.cpp-compatible API.

Unlike a simple chat wrapper, this project is built around a **planner → executor → tools** workflow.  
The goal is to explore how a local model can break a user task into steps, execute them through tools, and keep context during a session.

---

## ✨ What this project does

`mini_agent` can currently:

- generate a structured plan from a user request
- execute tasks step-by-step in one session
- read files
- write files
- maintain conversation context
- route model output into real tool execution through JSON actions

This makes it closer to a minimal local coding agent than a plain terminal chatbot.

---

## 🏗 Architecture

The current flow looks like this:

```text
User Input
   ↓
Planner
   ↓
Execution Plan (JSON)
   ↓
Executor
   ↓
Action JSON
   ↓
Handler
   ↓
Tools
   ↓
Result → back to context
```

### `agent/`
Core orchestration logic.

- `loop.py` — main runtime loop
- `state.py` — system/user message setup
- `handler.py` — action dispatch
- `planning.py` — plan generation
- `prompts/` — planner and executor prompts

### `llm/`
Model communication layer.

- `llm_client.py` — sends requests to the local model server
- `payload_builder.py` — builds payloads for API requests

### `tools/`
Execution layer.

- `read_file.py`
- `write_file.py`
- `say.py`
- `registry.py`

### Root
- `main.py` — entry point
- `config.py` — configuration
- `.env.example` — environment template

---

## 🧩 How it works

### 1. Planner
The planner receives the user request and converts it into a step-by-step plan.

Example:

```json
{
  "goal": "Create a simple landing page in index.html",
  "plan": [
    {
      "step": 1,
      "action": "write_file",
      "description": "Create index.html with a basic HTML structure"
    },
    {
      "step": 2,
      "action": "write_file",
      "description": "Add main landing page sections like header, hero block, and footer"
    }
  ]
}
```

### 2. Executor
The executor receives one step at a time and converts it into an executable JSON action.

Example:

```json
{
  "action": "write_file",
  "file_path": "./index.html",
  "content": "<!DOCTYPE html>..."
}
```

### 3. Handler + Tools
The handler routes the action to the correct tool, and the result is pushed back into the ongoing context.

---

## 🛠 Available actions

| Action | Description |
|---|---|
| `say` | Return text output |
| `write_file` | Write content to a file |
| `read_file` | Read file content |

---

## 🚀 Why this repo is interesting

This repository is not just “LLM calls a tool.”

It already demonstrates several ideas used in real agent systems:

- planner / executor separation
- structured JSON contracts between modules
- tool dispatching through a registry
- multi-step execution in one session
- context feedback loop after tool execution
- local inference instead of external SaaS APIs

That makes it a good experimental base for:
- local coding agents
- tool-using assistants
- multi-agent workflows
- Jinja / native tool-calling migration
- observability and logging experiments

---

## 📦 Requirements

- Python 3.10+
- a running local llama.cpp-compatible server
- a model that can reliably follow structured JSON output

Example:

```bash
./llama-server -m model.gguf
```

---

## ⚡ Usage

```bash
python main.py
```

Example prompts:

```text
>>> Create a simple HTML landing page in index.html
>>> Read file index.html
>>> Create style.css and move styles there
```

---

## 🔧 Configuration

Example `config.py`:

```python
API_URL = "http://127.0.0.1:8080"
MODEL_NAME = "your-model.gguf"
TEMP = 0.3
```

---

## ⚠️ Current limitations

- quantized models may still occasionally break JSON formatting
- long outputs may trigger Unicode / encoding issues
- file operations are not sandboxed yet
- retry / recovery is still minimal
- tool calling is still JSON-driven, not native Jinja tool calling

---

## 🗺 Roadmap

- [x] Basic local agent loop
- [x] Tool system
- [x] Planner → executor split
- [x] Multi-step execution in one session
- [ ] Better logging / observability
- [ ] Native Jinja-based tool calling
- [ ] Safer retry / recovery flow
- [ ] File-aware context management
- [ ] Output validation layer
- [ ] Multi-agent orchestration

---

## 📚 Motivation

The main goal of this repository is to understand agent systems from the inside by building one manually.

Instead of hiding everything behind a heavy framework, this project explores:
- how local models behave in agent loops
- how planning and execution can be separated
- how tools can be integrated with minimal infrastructure
- how to keep the system understandable while it grows

---

## 🧪 Status

**Early MVP, but functional.**

The project already supports:
- planning
- execution
- file tool usage
- contextual multi-step behavior

---

## 📄 License

MIT

---

## 🧑‍💻 Author

Built by [s1xc37](https://github.com/s1xc37) as part of hands-on exploration into:
- LLM agents
- local inference
- tool-based execution systems
- planner / executor architectures
