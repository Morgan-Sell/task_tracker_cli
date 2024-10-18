import os
from src.operations import is_task_id_valid, is_user_command_valid, parse_cli_input
from src.task import add_task, update_task_description
from src.storage import clean_json, read_json, save_data_to_json




def main() -> None:
    
    # Configure appliction
    task_counter = 1
    tracker_filename = "src/tracker.json"
    cwd = os.getcwd()
    file_path = os.path.join(cwd, tracker_filename)

    # ensure JSON is an empty list
    clean_json(file_path)
    
    while True:
        user_input = input("Your Task Tracker: ")

        # process data
        parsed_input = parse_cli_input(user_input)
        user_command = parsed_input[0].lower()

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
            # get and test user-provided task ID
            try: 
                task_id = int(parsed_input[1])
                is_task_id_valid(task_id, task_counter)
                
                # prepare data
                user_tasks = read_json(file_path)
                description = parsed_input[2]
        
                # update tasks and save changes
                user_tasks_updated = update_task_description(user_tasks, task_id, description)
                save_data_to_json(user_tasks_updated, file_path)

            except ValueError as e:
                print("\n" f"Error: {e}")
            
                print(
                    "If you would like to update a task, enter an integer equal " \
                    f"to or less than {task_counter-1}.\n"
                )
        elif user_command == "mark-in-progress":
            pass

if __name__ == "__main__":
    main()

