# Todo CLI

A simple command-line interface (CLI) application for managing a todo list, built with Python and `uv`.

## Installation

1. Install `uv`:
   ```bash
   pip install uv
   ```

2. Clone this repository and navigate to the project directory:
   ```bash
   git clone <repository-url>
   cd todo-cli
   ```

3. Initialize the project and install dependencies:
   ```bash
   uv sync
   ```

## Usage

Activate the virtual environment:
```bash
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

Run the CLI:
```bash
uv run todo-cli --help
```

Available commands:
- `todo-cli add <task>`: Add a new task.
- `todo-cli list`: List all tasks.
- `todo-cli complete <index>`: Mark a task as complete.
- `todo-cli delete <index>`: Delete a task.

## Example
```bash
$ uv run todo-cli add "Buy groceries"
Added task: Buy groceries
$ uv run todo-cli list
1. [ ] Buy groceries
$ uv run todo-cli complete 1
Marked task 1 as complete.
$ uv run todo-cli list
1. [✓] Buy groceries
```
