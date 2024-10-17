from typing import Dict, List
from datetime import datetime
import json

from src.storage import read_json, save_data_to_json


class Task:
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

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            "updated_at": self.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
        }


    def add(self):
        pass
    

    def update(self):
        pass

    
    def delete(self):
        pass

# --- Functions ---
def add_task(task_id: int, task_desc: str, filename: str) -> None:
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


def find_task(task_id: int, tasks: Dict) -> Dict:   
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise ValueError(
        f"Task # {task_id} does not exist."
    )


def update_task(tasks: List, task_id: int, new_description: str) -> Dict:
    try:
        for task in tasks:
            if task["id"] == task_id:
                task["description"] = new_description
    except:
        raise ValueError(
            f"Task # {task_id} does not exist."
        )

    return tasks