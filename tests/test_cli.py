
from src.cli import (
    parse_cli_input,
    is_integer,
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