import click
import json
import os

TODO_FILE = "todos.json"

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
    click.echo(f"Added task: {task}")

@cli.command()
def list():
    """List all tasks."""
    todos = load_todos()
    if not todos:
        click.echo("No tasks found.")
        return
    for i, todo in enumerate(todos, 1):
        status = "✓" if todo["done"] else " "
        click.echo(f"{i}. [{status}] {todo['task']}")

@cli.command()
@click.argument("index", type=int)
def complete(index):
    """Mark a task as complete."""
    todos = load_todos()
    if 1 <= index <= len(todos):
        todos[index - 1]["done"] = True
        save_todos(todos)
        click.echo(f"Marked task {index} as complete.")
    else:
        click.echo("Invalid task index.")

@cli.command()
@click.argument("index", type=int)
def delete(index):
    """Delete a task."""
    todos = load_todos()
    if 1 <= index <= len(todos):
        task = todos.pop(index - 1)
        save_todos(todos)
        click.echo(f"Deleted task: {task['task']}")
    else:
        click.echo("Invalid task index.")

if __name__ == "__main__":
   cli()
