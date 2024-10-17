
import pytest
from src.config import USER_COMMANDS
from src.operations import (
    parse_cli_input,
    is_integer,
    is_user_command_valid
)


def test_parse_cli_input():
    # test case 1: add input
    cli_input = 'add "Plan intergalatic voyage"'
    res = parse_cli_input(cli_input)
    assert res == ["add", "Plan intergalatic voyage"]

    # test case 2: update task
    cli_input = 'update 33 "Fix sailboat"'
    res = parse_cli_input(cli_input)
    assert res == ["update", "33", "Fix sailboat"]

    # test case 3: update task
    cli_input = 'delete 10'
    res = parse_cli_input(cli_input)
    assert res == ["delete", "10"]

    # test case 4: list all tasks
    cli_input = 'list'
    res = parse_cli_input(cli_input)
    assert res == ["list"]


def test_is_integer():
    # case 1: integer
    assert is_integer(42) == True

    # case 2: string
    assert is_integer("integer") == False


def test_is_command_valid_raises_error():
    commands_str = ", ".join(USER_COMMANDS)
    
    with pytest.raises(ValueError) as exc_info:
        is_user_command_valid("GO!")
    
 
    expected_result = f"Invalid command. User entered GO!. Acceptable commands are {commands_str}."
    assert str(exc_info.value) == expected_result
