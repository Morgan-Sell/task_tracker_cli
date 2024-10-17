import json
import os
from tempfile import TemporaryDirectory
import pytest
import numpy as np
import time
from datetime import datetime

from src.task import add_task, find_task, update_task
from src.storage import read_json


def test_add_task_success():
    with TemporaryDirectory() as tmp_directory:
        file_path = os.path.join(tmp_directory, "test.json")

        add_task(1, "Change my bike tires", file_path)

        # confirm task has been correctly added to the json file
        with open(file_path, mode="r") as json_file:
            data = json.load(json_file)

            # Assert
            assert list(data[0].keys()) == [
                "id",
                "description",
                "status",
                "created_at",
                "updated_at",
            ]

            assert data[0]["id"] == 1
            assert data[0]["description"] == "Change my bike tires"
            assert data[0]["status"] == "todo"


def test_add_task_with_existing_data(tmp_path, sample_tasks):
    # Prepare temporary test file
    test_json = tmp_path / "test.json"
    task = sample_tasks[3]
    task["id"] = 1
    json_text = [task]
    test_json.write_text(json.dumps(json_text, indent=4))

    # Action
    add_task(2, "Clean car engine", test_json)
    json_results= read_json(test_json)
    current_date = time.strftime("%Y-%m-%d", time.localtime())
    
    # Confirm results
    expected_results = [
         {
            "id": 1,
            "description": "Read new book",
            "status": "todo",
            "created_at": "2024-10-14 08:00:00",
            "updated_at": "2024-10-14 08:00:00"
        },
        {
            "id": 2,
            "description": "Clean car engine",
            "status": "todo",
            "created_at": current_date,
            "updated_at": current_date
        },
    ]

    assert len(json_results) == 2
    assert json_results[0] == expected_results[0]

    # break out task 2 because of matching exact time
    assert json_results[1]["id"] == 2
    assert json_results[1]["description"] == "Clean car engine"
    assert json_results[1]["status"] == "todo"
    
    created_date = datetime.strptime(json_results[1]["created_at"], "%Y-%m-%d %H:%M:%S")
    created_date = created_date.strftime("%Y-%m-%d")
    assert created_date == current_date
    
    
    # assert time.strftime(
    #     "%Y-%m-%d", json_results[1]["updated_at"]
    #  ) == current_date


def test_find_task_success(sample_tasks):
    
    task = find_task(task_id=3, tasks=sample_tasks)

    assert task["description"] == "Prepare for meeting"
    assert task["status"] == "completed"
    assert task["created_at"] == "2024-10-12 09:15:00"
    assert task["updated_at"] == "2024-10-13 18:00:00"


def test_update_task_success(sample_tasks):
    # prepare for test
    tasks = sample_tasks
    task_id = 5
    new_description = "Go fishing!"
    tasks_updated = update_task(tasks, task_id, new_description)

    # Check results
    expected_results = {
            "id": 5,
            "description": "Go fishing!",
            "status": "in-progress",
            "created_at": "2024-10-13 17:30:00",
            "updated_at": "2024-10-14 07:00:00"
        }
    
    assert expected_results == tasks_updated[4]
    