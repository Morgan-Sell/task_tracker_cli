import json
import os
import time
from datetime import datetime
from tempfile import TemporaryDirectory

import pytest

from src.storage import read_json
from src.task import add_task, update_task_description, update_task_status


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
    json_results = read_json(test_json)
    current_date = time.strftime("%Y-%m-%d", time.localtime())

    # Confirm results
    expected_results = [
        {
            "id": 1,
            "description": "Read new book",
            "status": "todo",
            "created_at": "2024-10-14 08:00:00",
            "updated_at": "2024-10-14 08:00:00",
        },
        {
            "id": 2,
            "description": "Clean car engine",
            "status": "todo",
            "created_at": current_date,
            "updated_at": current_date,
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


def test_update_task_description_success(sample_tasks):
    # prepare for test
    tasks = sample_tasks
    task_id = 5
    new_description = "Go fishing!"
    tasks_updated = update_task_description(tasks, task_id, new_description)

    # Format to remove time
    expected_updated_at = datetime.now().date().strftime("%Y-%m-%d")
    new_updated_at = datetime.strptime(
        tasks_updated[4]["updated_at"], "%Y-%m-%d %H:%M:%S"
    ).strftime("%Y-%m-%d")

    # Prepare expected results
    assert tasks_updated[4]["description"] == new_description
    assert new_updated_at == expected_updated_at


@pytest.mark.parametrize("errors", [0, 10, "integer"])
def test_update_task_description_raises_error(errors, sample_tasks):
    with pytest.raises(ValueError):
        update_task_description(sample_tasks, errors, "Fly to the moon!")


def test_update_task_status_success(sample_tasks):
    tasks = sample_tasks

    # change tasks' status
    updated_tasks = update_task_status(tasks, 2, "done")
    results = update_task_status(updated_tasks, 4, "in-progress")

    # prepare results
    expected_task_2 = {
        "id": 2,
        "description": "Complete Python project",
        "status": "done",
        "created_at": "2024-10-13 14:45:00",
        "updated_at": datetime.now().date().strftime("%Y-%m-%d"),
    }
    expected_task_4 = {
        "id": 4,
        "description": "Read new book",
        "status": "in-progress",
        "created_at": "2024-10-14 08:00:00",
        "updated_at": datetime.now().date().strftime("%Y-%m-%d"),
    }

    # prepare responses
    task_2_results = results[1]
    task_2_results["updated_at"] = datetime.strptime(
        task_2_results["updated_at"], "%Y-%m-%d %H:%M:%S"
    ).strftime("%Y-%m-%d")

    task_4_results = results[3]
    task_4_results["updated_at"] = datetime.strptime(
        task_4_results["updated_at"], "%Y-%m-%d %H:%M:%S"
    ).strftime("%Y-%m-%d")

    # Check results
    assert expected_task_2 == task_2_results
    assert expected_task_4 == task_4_results


@pytest.mark.parametrize("errors", [0, 10, "integer"])
def test_update_task_status_raises_error(errors, sample_tasks):
    with pytest.raises(ValueError):
        update_task_description(sample_tasks, errors, "Fly to the moon!")
