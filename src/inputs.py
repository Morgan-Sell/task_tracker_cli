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
    
