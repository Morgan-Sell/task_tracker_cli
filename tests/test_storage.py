import json
import pytest

from src.storage import read_json


def test_read_json(tmp_path, sample_tasks):
    
    # Prepare temporary test file
    test_json = tmp_path / "test.json"
    json_text = [sample_tasks[0]]
    test_json.write_text(json.dumps(json_text, indent=4))

    data = read_json(test_json)

    expected_result = [{
            "id": 1,
            "description": "Buy groceries",
            "status": "todo",
            "created_at": "2024-10-14 10:30:00",
            "updated_at": "2024-10-14 10:30:00"
        }]
    
    assert data == expected_result