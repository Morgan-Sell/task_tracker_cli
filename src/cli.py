from typing import Dict
from src.task import Task
from datetime import datetime
import json


def parse_cli_input(cli_input: str) -> list:
    result = []
    current_element = []
    in_quotes = False

    for char in cli_input:
        if char == '"':
            in_quotes = not in_quotes
        elif char == ' ' and in_quotes is False:
            if len(current_element) > 0:
                result.append("". join(current_element))
                current_element = []
        else:
            current_element.append(char)
    
    # append the last element
    if len(current_element) > 0:
        result.append(''.join(current_element))
    
    return result


