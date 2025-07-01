import click
import json
import os
from rich.console import Console
from rich.table import Table
from rich import box

TODO_FILE = "todos.json"
console = Console()

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=2)

@click.group()
def cli():
    pass

@cli.command()
@click.argument("task")
def add(task):
    """Add a new task to the todo list."""
    todos = load_todos()
    todos.append({"task": task, "done": False})
    save_todos(todos)
    console.print(f"[green]Added task:[/green] {task}")

@cli.command()
def list():
    """List all tasks."""
    todos = load_todos()
    if not todos:
        console.print("[yellow]No tasks found.[/yellow]")
        return
    table = Table(title="ToDo List", box=box.ROUNDED, show_lines=True)
    table.add_column("Nr.", style="cyan", justify="right")
    table.add_column("Status", style="magenta")
    table.add_column("Task", style="white")
    for i, todo in enumerate(todos, 1):
        status = "[green]✓[/green]" if todo["done"] else "[red]✗[/red]"
        table.add_row(str(i), status, todo["task"])
    console.print(table)

@cli.command()
@click.argument("index", type=int)
def complete(index):
    """Mark a task as complete."""
    todos = load_todos()
    if 1 <= index <= len(todos):
        todos[index - 1]["done"] = True
        save_todos(todos)
        console.print(f"[bold green]Task {index} marked as done.[/bold green]")
    else:
        console.print("[red]Invalid task index.[/red]")

@cli.command()
@click.argument("index", type=int)
def delete(index):
    """Delete a task."""
    todos = load_todos()
    if 1 <= index <= len(todos):
        task = todos.pop(index - 1)
        save_todos(todos)
        console.print(f"[bold red]Deleted task:[/bold red] {task['task']}")
    else:
        console.print("[red]Invalid task index.[/red]")

if __name__ == "__main__":
    cli()
