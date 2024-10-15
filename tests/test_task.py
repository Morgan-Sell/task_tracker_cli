import json
import os
from tempfile import TemporaryDirectory
import pytest

from src.inputs import add_task, find_task


def test_add_task_success():
    with TemporaryDirectory() as tmp_directory:
        file_path = os.path.join(tmp_directory, "test.json")

        add_task(1, "Change my bike tires", file_path)

        # confirm task has been correctly added to the json file
        with open(file_path, mode="r") as json_file:
            data = json.load(json_file)

            # Assert
            assert list(data.keys()) == [
                "id",
                "description",
                "status",
                "created_at",
                "updated_at",
            ]

            assert data["id"] == 1
            assert data["description"] == "Change my bike tires"
            assert data["status"] == "todo"


def test_find_task_success(sample_tasks):
    
    task = find_task(task_id=3, tasks=sample_tasks)

    assert task["description"] == "Prepare for meeting"
    assert task["status"] == "completed"
    assert task["created_at"] == "2024-10-12 09:15:00"
    assert task["updated_at"] == "2024-10-13 18:00:00"