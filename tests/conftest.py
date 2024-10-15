import pytest


pytest.fixture(session="function")
def sample_tasks():
    tasks = [
        {
            "id": 1,
            "description": "Buy groceries",
            "status": "todo",
            "created_at": "2024-10-14 10:30:00",
            "updated_at": "2024-10-14 10:30:00"
        },
        {
            "id": 2,
            "description": "Complete Python project",
            "status": "in-progress",
            "created_at": "2024-10-13 14:45:00",
            "updated_at": "2024-10-14 09:00:00"
        },
        {
            "id": 3,
            "description": "Prepare for meeting",
            "status": "completed",
            "created_at": "2024-10-12 09:15:00",
            "updated_at": "2024-10-13 18:00:00"
        },
        {
            "id": 4,
            "description": "Read new book",
            "status": "todo",
            "created_at": "2024-10-14 08:00:00",
            "updated_at": "2024-10-14 08:00:00"
        },
        {
            "id": 5,
            "description": "Exercise at gym",
            "status": "in-progress",
            "created_at": "2024-10-13 17:30:00",
            "updated_at": "2024-10-14 07:00:00"
        }
    ]

    return tasks