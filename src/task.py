from typing import Dict, List
from datetime import datetime
import json

from src.storage import read_json, save_data_to_json


class Task:
    """
    Represents a task with an ID, description, status, and timestamps for creation and updates.

    Attributes:
        id (int): The unique identifier for the task.
        description (str): A brief description of the task.
        status (str): The current status of the task (e.g., 'todo', 'in-progress').
        created_at (str): The timestamp when the task was created.
        updated_at (str): The timestamp when the task was last updated.
    """
    def __init__(
        self,
        id: int,
        description: str,
        status: str,
        created_at: str,
        updated_at: str
    ):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self) -> Dict:
        """
        Converts the Task object into a dictionary format.

        Returns:
        dict: A dictionary containing the task's ID, description, status, and formatted timestamps.
        """
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            "updated_at": self.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
        }


# --- FUNCTIONS ---
def add_task(task_id: int, task_desc: str, filename: str) -> None:
    """
    Adds a new task to the task list stored in a JSON file.

    Args:
        task_id (int): The unique ID for the task.
        task_desc (str): A brief description of the task.
        filename (str): The path to the JSON file where tasks are stored.

    Returns:
        None
    """
    task = Task(
        id=task_id,
        description=task_desc,
        status="todo",
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    
    data = read_json(filename)
    data.append(task.to_dict())
    save_data_to_json(data, filename)

def update_task_description(tasks: List[Dict], task_id: int, new_description: str) -> List[Dict]:
    """
    Updates the description of a task by its ID and updates the timestamp.

    Args:
        tasks (List[Dict]): The list of tasks.
        task_id (int): The ID of the task to update.
        new_description (str): The new description for the task.

    Returns:
        List[Dict]: The updated list of tasks.

    Raises:
        ValueError: If the task with the given ID does not exist.
    """
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updated_at"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            return tasks
    
    raise ValueError(f"Task # {task_id} does not exist.")


def update_task_status(tasks: List, task_id: int, new_status: str) -> List[Dict]:
    """
    Updates the status of a task by its ID and updates the timestamp.

    Args:
        tasks (List[Dict]): The list of tasks.
        task_id (int): The ID of the task to update.
        new_status (str): The new status for the task.

    Returns:
        List[Dict]: The updated list of tasks.

    Raises:
        ValueError: If the task with the given ID does not exist.
    """
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updated_at"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            return tasks
    
    raise ValueError(f"Task # {task_id} does not exist.")


def list_tasks_based_on_status(tasks: List[Dict], task_status: str) -> None:
    """
    Displays tasks that match the given status.

    Args:
        tasks (List[Dict]): The list of tasks.
        task_status (str): The status to filter tasks by (e.g., 'todo', 'in-progress').

    Returns:
        None
    """
    print(f"\n Your {task_status} Tasks: \n")
    for task in tasks:
        if task["status"] == task_status:
            print(f"ID: {task['id']}")
            print(f"Description: {task['description']}")
            print(f"Status: {task['status']}")
            print(f"Created At: {task['created_at']}")
            print(f"Updated At: {task['updated_at']}")
            print("-" * 40)
