import os
from src.operations import is_user_command_valid, parse_cli_input
from src.task import add_task
from src.storage import read_json





def main() -> None:
    task_counter = 1
    tracker_filename = "src/tracker.json"
    
    while True:
        user_input = input("Your Task Tracker: ")

        # process data
        parsed_input = parse_cli_input(user_input)
        user_command = parsed_input[0].lower()

        # get filename to reference
        cwd = os.getcwd()
        file_path = os.path.join(cwd, tracker_filename)

        # confirm command is valid
        is_user_command_valid(user_command)

        # execture appropriate action based on user input
        if user_command == "add":
            add_task(
                task_id=task_counter,
                task_desc=parsed_input[1],
                filename=file_path,
            )
            task_counter += 1

        elif user_command == "update":
            tasks = read_json(file_path)



if __name__ == "__main__":
    main()

