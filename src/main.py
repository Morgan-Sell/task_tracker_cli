import os
from src.operations import is_task_id_valid, is_user_command_valid, parse_cli_input
from src.task import add_task, update_task_description, update_task_status
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



        # if not adding a new task or listing, confirm task ID is valid
        
        try:         
            # confirm command is valid
            is_user_command_valid(user_command)
            
            if user_command not in ["add", "list"]:
                task_id = int(parsed_input[1])
                is_task_id_valid(task_id, task_counter)

            user_tasks = read_json(file_path)

        except ValueError as e:
            print("\n" f"Error: {e}")
            print(
                "Resubmit a request to your task tracker.\n"
            )
            
        # execture appropriate action based on user input
        if user_command == "add":
            add_task(
                task_id=task_counter,
                task_desc=parsed_input[1],
                filename=file_path,
            )
            task_counter += 1

        elif user_command == "update":
            # update task description and save changes
            new_description = parsed_input[2]
            user_tasks_updated = update_task_description(user_tasks, task_id, new_description)
            save_data_to_json(user_tasks_updated, file_path)

        elif user_command == "mark-in-progress": 
            # update task status to in-progress and save changes
            user_tasks_updated = update_task_status(user_tasks, task_id, "in-progress")
            save_data_to_json(user_tasks_updated, file_path)

        
        elif user_command == "mark-done": 
            # update task status to done and save changes
            user_tasks_updated = update_task_status(user_tasks, task_id, "done")
            save_data_to_json(user_tasks_updated, file_path)
        
        elif user_command == "delete":
            # subtract 1 to get the index for the task ID
            del user_tasks[task_id-1]
            save_data_to_json(user_tasks, file_path)

if __name__ == "__main__":
    main()

