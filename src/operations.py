from typing import Any, Dict, Union
from src.config import USER_COMMANDS

def parse_cli_input(cli_input: str) -> list:
    """
    Parses a CLI input string into a list of arguments, handling 
    quoted strings as single elements.

    Args:
        cli_input (str): The command-line input string.

    Returns:
        list: A list of parsed elements from the input string.
    """
    
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
    """
    Checks if the given element can be converted to an integer.

    Args:
        element (Union[int, str]): The element to check.

    Returns:
        bool: True if the element can be converted to an integer, otherwise False.
    """
    try:
        int(element)
        return True
    except ValueError:
        return False


def is_user_command_valid(command: str) -> None:
    """
    Validate if the provided user command is in the allowed list of commands.

    Args:
        command (str): The user command to validate.

    Raises:
        ValueError: If the command is not in the list of acceptable commands.
    """
    commands_str = ", ".join(USER_COMMANDS)
    if command not in USER_COMMANDS:
        raise ValueError(
            f"Invalid command. User entered {command}. "
            f"Acceptable commands are {commands_str}."
        )


def is_task_id_valid(task_id: int, task_counter: int) -> None:
    """
    Validates if the given task ID is within the valid range.

    Args:
        task_id (int): The ID of the task to validate.
        task_counter (int): The total number of tasks.

    Raises:
        ValueError: If the task ID is not valid.
    """
    
    if not isinstance(task_id, int) or task_id < 1 or task_id > task_counter:
        raise ValueError(
            f"Invalid task ID. Received {task_id}."
        )
