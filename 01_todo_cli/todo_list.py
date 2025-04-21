"""
Todo List CLI Application

A command-line interface application for managing tasks with features like adding,
listing, marking as completed, and removing tasks. Tasks are persisted to a JSON file.

Author: [Your Name]
GitHub: [Your GitHub Profile]
License: MIT
Version: 1.0.0
"""

import click # to create a cli
import json # to save and load tasks from a file
import os # to check if a file exists
import sys
import logging
from typing import List, Dict, Any, Optional
from datetime import datetime
import colorama
from colorama import Fore, Style

# Initialize colorama for cross-platform colored output
colorama.init()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("todo.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Constants
TODO_FILE = "todo.json"
BACKUP_DIR = "backups"
VERSION = "1.0.0"

def load_tasks() -> List[Dict[str, Any]]:
    """
    Load tasks from the JSON file.
    
    Returns:
        List[Dict[str, Any]]: List of task dictionaries
    """
    try:
        if not os.path.exists(TODO_FILE):
            logger.info(f"Todo file not found. Creating new file: {TODO_FILE}")
            return []
        
        with open(TODO_FILE, "r", encoding="utf-8") as file:
            tasks = json.load(file)
            logger.info(f"Loaded {len(tasks)} tasks from {TODO_FILE}")
            return tasks
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON from {TODO_FILE}: {str(e)}")
        click.echo(f"{Fore.RED}Error: Todo file is corrupted. Creating a new one.{Style.RESET_ALL}")
        return []
    except Exception as e:
        logger.error(f"Unexpected error loading tasks: {str(e)}")
        click.echo(f"{Fore.RED}Error loading tasks: {str(e)}{Style.RESET_ALL}")
        return []

def save_tasks(tasks: List[Dict[str, Any]]) -> bool:
    """
    Save tasks to the JSON file.
    
    Args:
        tasks: List of task dictionaries to save
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Create backup before saving
        if os.path.exists(TODO_FILE):
            create_backup()
            
        with open(TODO_FILE, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)
            
        logger.info(f"Saved {len(tasks)} tasks to {TODO_FILE}")
        return True
    except Exception as e:
        logger.error(f"Error saving tasks: {str(e)}")
        click.echo(f"{Fore.RED}Error saving tasks: {str(e)}{Style.RESET_ALL}")
        return False

def create_backup() -> None:
    """
    Create a backup of the todo file.
    """
    try:
        if not os.path.exists(BACKUP_DIR):
            os.makedirs(BACKUP_DIR)
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = os.path.join(BACKUP_DIR, f"todo_{timestamp}.json")
        
        with open(TODO_FILE, "r", encoding="utf-8") as src, open(backup_file, "w", encoding="utf-8") as dst:
            dst.write(src.read())
            
        logger.info(f"Created backup: {backup_file}")
    except Exception as e:
        logger.error(f"Error creating backup: {str(e)}")

def add_task(task: str, priority: Optional[str] = None, due_date: Optional[str] = None) -> bool:
    """
    Add a new task to the list.
    
    Args:
        task: The task description
        priority: Optional priority level (high, medium, low)
        due_date: Optional due date in YYYY-MM-DD format
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        tasks = load_tasks()
        
        # Validate due date if provided
        if due_date:
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                click.echo(f"{Fore.RED}Error: Invalid date format. Use YYYY-MM-DD{Style.RESET_ALL}")
                return False
        
        # Validate priority if provided
        if priority and priority.lower() not in ["high", "medium", "low"]:
            click.echo(f"{Fore.RED}Error: Priority must be high, medium, or low{Style.RESET_ALL}")
            return False
        
        new_task = {
            "task": task,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        if priority:
            new_task["priority"] = priority.lower()
            
        if due_date:
            new_task["due_date"] = due_date
            
        tasks.append(new_task)
        success = save_tasks(tasks)
        
        if success:
            click.echo(f"{Fore.GREEN}Task added successfully: {task}{Style.RESET_ALL}")
            return True
        return False
    except Exception as e:
        logger.error(f"Error adding task: {str(e)}")
        click.echo(f"{Fore.RED}Error adding task: {str(e)}{Style.RESET_ALL}")
        return False

def list_tasks(filter_completed: Optional[bool] = None, sort_by: Optional[str] = None) -> None:
    """
    List all tasks with optional filtering and sorting.
    
    Args:
        filter_completed: Filter by completion status (True, False, None for all)
        sort_by: Sort by field (priority, due_date, created_at)
    """
    try:
        tasks = load_tasks()
        
        if not tasks:
            click.echo(f"{Fore.YELLOW}No tasks found.{Style.RESET_ALL}")
            return
        
        # Filter tasks if needed
        if filter_completed is not None:
            tasks = [task for task in tasks if task["completed"] == filter_completed]
            
        # Sort tasks if needed
        if sort_by:
            if sort_by == "priority":
                priority_order = {"high": 0, "medium": 1, "low": 2}
                tasks.sort(key=lambda x: priority_order.get(x.get("priority", "low"), 3))
            elif sort_by == "due_date":
                tasks.sort(key=lambda x: x.get("due_date", "9999-12-31"))
            elif sort_by == "created_at":
                tasks.sort(key=lambda x: x.get("created_at", ""))
        
        click.echo(f"\n{Fore.CYAN}📋 TASK LIST ({len(tasks)} tasks){Style.RESET_ALL}\n")
        
        for index, task in enumerate(tasks, 1):
            status = f"{Fore.GREEN}✅{Style.RESET_ALL}" if task["completed"] else f"{Fore.RED}❌{Style.RESET_ALL}"
            
            # Format priority with color
            priority_str = ""
            if "priority" in task:
                if task["priority"] == "high":
                    priority_str = f" {Fore.RED}[HIGH]{Style.RESET_ALL}"
                elif task["priority"] == "medium":
                    priority_str = f" {Fore.YELLOW}[MEDIUM]{Style.RESET_ALL}"
                elif task["priority"] == "low":
                    priority_str = f" {Fore.BLUE}[LOW]{Style.RESET_ALL}"
            
            # Format due date
            due_date_str = ""
            if "due_date" in task:
                due_date_str = f" {Fore.CYAN}Due: {task['due_date']}{Style.RESET_ALL}"
            
            click.echo(f"{index}. [{status}] {task['task']}{priority_str}{due_date_str}")
        
        click.echo("")
    except Exception as e:
        logger.error(f"Error listing tasks: {str(e)}")
        click.echo(f"{Fore.RED}Error listing tasks: {str(e)}{Style.RESET_ALL}")

def mark_completed(task_number: int) -> bool:
    """
    Mark a task as completed.
    
    Args:
        task_number: The task number to mark as completed
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        tasks = load_tasks()
        
        if not tasks:
            click.echo(f"{Fore.YELLOW}No tasks found.{Style.RESET_ALL}")
            return False
            
        if 0 < task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            tasks[task_number - 1]["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            success = save_tasks(tasks)
            
            if success:
                click.echo(f"{Fore.GREEN}Task {task_number} marked as completed.{Style.RESET_ALL}")
                return True
            return False
        else:
            click.echo(f"{Fore.RED}Invalid task number: {task_number}{Style.RESET_ALL}")
            return False
    except Exception as e:
        logger.error(f"Error marking task as completed: {str(e)}")
        click.echo(f"{Fore.RED}Error marking task as completed: {str(e)}{Style.RESET_ALL}")
        return False

def remove_task(task_number: int) -> bool:
    """
    Remove a task.
    
    Args:
        task_number: The task number to remove
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        tasks = load_tasks()
        
        if not tasks:
            click.echo(f"{Fore.YELLOW}No tasks found.{Style.RESET_ALL}")
            return False
            
        if 0 < task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            success = save_tasks(tasks)
            
            if success:
                click.echo(f"{Fore.GREEN}Removed task: {removed_task['task']}{Style.RESET_ALL}")
                return True
            return False
        else:
            click.echo(f"{Fore.RED}Invalid task number{Style.RESET_ALL}")
            return False
    except Exception as e:
        logger.error(f"Error removing task: {str(e)}")
        click.echo(f"{Fore.RED}Error removing task: {str(e)}{Style.RESET_ALL}")
        return False

@click.group()
def cli():
    """Simple Todo List Manager with advanced features"""
    pass

@cli.command()
@click.argument("task")
@click.option("--priority", "-p", type=click.Choice(["high", "medium", "low"]), help="Set task priority")
@click.option("--due-date", "-d", help="Set due date (YYYY-MM-DD)")
def add(task, priority, due_date):
    """Add a new task to the list"""
    add_task(task, priority, due_date)

@cli.command()
@click.option("--completed", "-c", is_flag=True, help="Show only completed tasks")
@click.option("--pending", "-p", is_flag=True, help="Show only pending tasks")
@click.option("--sort", "-s", type=click.Choice(["priority", "due_date", "created_at"]), help="Sort tasks by field")
def list(completed, pending, sort):
    """List all the tasks"""
    filter_completed = None
    if completed:
        filter_completed = True
    elif pending:
        filter_completed = False
        
    list_tasks(filter_completed, sort)

@cli.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark a task as completed"""
    mark_completed(task_number)

@cli.command()
@click.argument("task_number", type=int)
def remove(task_number):
    """Remove a task"""
    remove_task(task_number)

@cli.command()
def stats():
    """Show task statistics"""
    try:
        tasks = load_tasks()
        
        if not tasks:
            click.echo(f"{Fore.YELLOW}No tasks found.{Style.RESET_ALL}")
            return
            
        total = len(tasks)
        completed = sum(1 for task in tasks if task["completed"])
        pending = total - completed
        
        click.echo(f"\n{Fore.CYAN}📊 TASK STATISTICS{Style.RESET_ALL}\n")
        click.echo(f"Total tasks: {total}")
        click.echo(f"Completed: {completed} ({completed/total*100:.1f}%)")
        click.echo(f"Pending: {pending} ({pending/total*100:.1f}%)")
        
        # Priority breakdown
        priorities = {"high": 0, "medium": 0, "low": 0}
        for task in tasks:
            if "priority" in task:
                priorities[task["priority"]] += 1
                
        click.echo("\nPriority breakdown:")
        click.echo(f"High: {priorities['high']}")
        click.echo(f"Medium: {priorities['medium']}")
        click.echo(f"Low: {priorities['low']}")
        
        click.echo("")
    except Exception as e:
        logger.error(f"Error showing statistics: {str(e)}")
        click.echo(f"{Fore.RED}Error showing statistics: {str(e)}{Style.RESET_ALL}")

@cli.command()
def version():
    """Show the application version"""
    click.echo(f"Todo CLI v{VERSION}")

if __name__ == "__main__":
    cli()
