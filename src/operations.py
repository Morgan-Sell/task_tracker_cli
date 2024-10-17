from typing import Dict, Union
from src.config import USER_COMMANDS
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


def is_integer(element: Union[int, str]) -> bool:
    try:
        int(element)
        return True
    except ValueError:
        return False


def is_user_command_valid(command: str) -> ValueError:
    commands_str = ", ".join(USER_COMMANDS)
    if command not in USER_COMMANDS:
        raise ValueError(
            f"Invalid command. User entered {command}. "
            f"Acceptable commands are {commands_str}."
        )
