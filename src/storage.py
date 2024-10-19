import json
from typing import Any, Dict, List


def read_json(filename: str) -> List[Any]:
    try:
        with open(filename, "r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = []

    return data


def save_data_to_json(data: List[Dict], filename: str) -> None:
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)


def clean_json(filename: str) -> None:
    data = []
    save_data_to_json(data, filename)
