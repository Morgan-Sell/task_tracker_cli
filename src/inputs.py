from typing import Dict
from src.task import Task
from datetime import datetime
import json


def split_input(input: str) -> list:
    return 


def add_task(task_id: int, task_desc: str, filename: str) -> None:
    task = Task(
        id=task_id,
        description=task_desc,
        status="todo",
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    with open(filename, "w") as json_file:
        json.dump(task.to_dict(), json_file, indent=4)
    


def find_task(task_id: int, tasks: Dict) -> Dict:
    
    for task in tasks:
        if task["id"] == task_id:
            return task
    
    raise ValueError(
        f"Task # {task_id} does not exist."
    )


