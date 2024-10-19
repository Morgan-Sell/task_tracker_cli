import json

from src.storage import read_json, save_data_to_json


def test_read_json(tmp_path, sample_tasks):

    # Prepare temporary test file
    test_json = tmp_path / "test.json"
    json_text = [sample_tasks[0]]
    test_json.write_text(json.dumps(json_text, indent=4))

    data = read_json(test_json)

    expected_result = [
        {
            "id": 1,
            "description": "Buy groceries",
            "status": "todo",
            "created_at": "2024-10-14 10:30:00",
            "updated_at": "2024-10-14 10:30:00",
        }
    ]

    assert data == expected_result


def test_save_data_to_json(tmpdir, sample_tasks):
    temp_file = tmpdir.join("test.json")
    save_data_to_json(sample_tasks, temp_file)

    with open(temp_file, "r") as json_file:
        data = json.load(json_file)

    # Check results
    assert len(data) == 5
    assert data[2] == {
        "id": 3,
        "description": "Prepare for meeting",
        "status": "done",
        "created_at": "2024-10-12 09:15:00",
        "updated_at": "2024-10-13 18:00:00",
    }
