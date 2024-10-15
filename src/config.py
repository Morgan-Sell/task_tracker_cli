import os
from pathlib import Path
from typing import Any, Dict, List, Union


# global constants
STATUS_TYPES = [
    "todo",
    "in-progress",
    "done"
]

USER_COMMANDS = [
    "add",
    "update",
    "delete",
    "mark-in-progress",
    "mark-done",
    "list",    
]

USER_COMMANDS_WITH_ID = [
    "update",
    "delete",
    "mark-in-progress",
    "mark-done",  
]