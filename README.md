# Task Tracker CLI

A command-line interface (CLI) application for managing and tracking tasks. This application allows users to add, update, and manage tasks with statuses like "To Do," "In Progress," and "Done." It stores task data in a JSON file, providing an easy and lightweight solution for task tracking.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Configuration](#configuration)
- [Dependencies](#dependencies)
- [License](#license)
- [Acknowledgement](#acknowledgement)

## Introduction

Task Tracker is a CLI application written in Python that helps users manage their daily tasks. Tasks can be categorized into different statuses, including "To Do," "In Progress," and "Done." This is ideal for users who prefer using the command line to manage their personal or professional task lists efficiently.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Morgan-Sell/task_tracker_cli.git
   cd task_tracker_cli

2. Install the necessary dependencies by running:

    ```bash
    pip install -r requirements.txt

3. Run the shell script to start the application:
   
   ```bash
   ./run/sh

## Usage

Once the CLI starts, you can perform the following operations:

- Add a task: You can add a new task to the tracker with a description.
- Update task status: Tasks can be updated to "To Do," "In Progress," or "Done."
- View tasks: View by tasks by their current status.
- Remove a task: Remove a task by its ID.


### Example

```
    # run application
    $ ./run.sh

    # start by adding tasks
    $ Your Task Tracker: add "Get haircut"
    $ Your Task Tracker: add "Replace bicycle tire"
    $ Your Task Tracker: add "Send a birthday card to mom"
    $ Your Task Tarcker: add "Buy one-way ticket to Tasmania"

    # modify task
    $ Your Task Tracker: mark-done 3
    $ Your Task Tracker: mark-in-progress 2
    $ Your Task Tracker: update 1 "Fix boat motor"
    
    # display selected tasks
    $ Your Task Tracker: list in-progress

    $ Your in-progress Tasks: 

    $ ID: 2
    $ Description: Replace bicycle tire
    $ Status: in-progress
    $ Created At: 2024-10-19 09:55:00
    $ Updated At: 2024-10-19 09:56:52
    $ ----------------------------------------
```
    
## Features
- Task Management: Add, update, and delete tasks.
- Status Tracking: Each task has a status - `todo`, `in-progress`, or `done`.
- JSON Storage: Task data is stored in a simple JSON format for easy access.
- Command-line Interface: User-friendly CLI for quick interaction with task data.

## Configuration
The application uses a `tracker.json` file to store tasks. The tasks include details such as:

- `id`: Unique identifier for the task.
- `description`: A brief description of the task.
- `status`: The current status of the task (todo, in-progress, or done).
- `created_at`: Timestamp indicating task creation.
- `updated_at`: Timestamp indicating last update times.

Example `tracker.json`:

    
    [
        {
            "id": 1,
            "description": "Water plants",
            "status": "done",
            "created_at": "2024-10-18 13:55:37",
            "updated_at": "2024-10-18 13:56:10"
        },
        {
            "id": 2,
            "description": "Walk the dinosaur",
            "status": "todo",
            "created_at": "2024-10-18 13:55:45",
            "updated_at": "2024-10-18 13:55:45"
        }
    ]

## Dependencies
- **Python** 3.x


Ensure all dependencies are listed in `requirements.txt` and installed using:

```
    pip install -r requirements.txt
```

Project page URL: https://github.com/Morgan-Sell/task_tracker_cli

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgement
This application was built following the design developed by [roadmap.sh's Task Tracker project](https://roadmap.sh/projects/task-tracker).