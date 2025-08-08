# sdk_assignment

---

## 🧠 Agents

### MathAgent (`math_agent.py`)
- Filters input using `input_filter` to detect math-related queries.
- Uses the custom subtraction tool when appropriate.

### GeneralAssistant (`general_agent.py`)
- Handles non-math queries using its own input filter.

---

## 🛠️ Custom Tool

### Subtraction Tool (`subtraction_tool.py`)
- Implements a subtraction function.
- Uses a Pydantic schema (`subtraction_schema.py`) to validate input.

---

## ✅ Input Validation

### Pydantic Schema (`subtraction_schema.py`)
- Ensures input contains two integers: `a` and `b`.
- Includes comments comparing `dataclass` vs `Pydantic`.

---

## 🔄 Streaming Output

### Stream Handler (`stream_handler.py`)
- Captures and prints streaming events from agents.

---

## 🗂️ Session Context

### Session Store (`session_store.py`)
- Stores and retrieves session data using SQLite.
- Ensures context persistence across agent interactions.

---

## 🚀 Execution

### Main File (`main.py`)
- Runs both agents asynchronously using `asyncio.run()` and `run_agents()`.
- All components strictly follow the assignment instructions.

