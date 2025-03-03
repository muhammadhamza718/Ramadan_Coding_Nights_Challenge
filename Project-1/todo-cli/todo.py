import click # to create a cli
import json # to save and load tasks from a file
import os # to check if a file exists

TODO_FILE = "todo.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)       

@click.group()
def cli():
    """Simple Todo List Manager"""
    pass

@cli.command()
@click.argument("task")
def add(task):
    """Add a new task to the list"""
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    click.echo(f"Task added successfully: {task}")

@cli.command() 
def list():
    """List all the tasks"""
    tasks = load_tasks()
    if not tasks:
        click.echo("No tasks found.")
        return

    for index, task in enumerate(tasks, 1):
        status = "✅" if task["completed"] else "❌"
        click.echo(f"{index}. [{status}] {task['task']}")

@cli.command()
@click.argument("task_number", type=int)
def completed(task_number):
    """Mark a task as completed"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)
        click.echo(f"Task {task_number} marked as completed.")
    else:
        click.echo(f"Invalid task number: {task_number}")

@cli.command()
@click.argument("task_number", type=int)
def remove(task_number):
    """Remove a task"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f'Removed task: {removed_task["task"]}')
    else:
        click.echo("Invalid task number")

cli.add_command(add)
cli.add_command(list)
cli.add_command(completed)
cli.add_command(remove)

if __name__ == "__main__":
    cli()
