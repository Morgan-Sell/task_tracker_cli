from typing import Dict, List
import json



def read_json(filename: str) -> Dict:
    try:
        with open(filename, "r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = []

    return data


def save_data_to_json(data: List, filename: str) -> None:   
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)
