import os
from rich.console import Console
console = Console()
from settings.config import listfiles_path
from settings.config import logger_path
from settings.config import readfile_path
from settings.config import delfile_path
from settings.config import loginlog_path
from settings.config import searchlog_path
from listfiles import lslog

menu = {
    "CmdLog": " ",
    1: "Run a $Bash-command to log.",
    2: "Look at the login-attempts.",
    3: "List the logfiles.",
    4: "Read a file.",
    5: "Search for a keyword within a logfile.",
    6: "Delete a file.",
    "Type": "[Exit] or [Quit] to go back to the terminal\n"
}

while True:
    for key, value in menu.items():
        console.print( key, value, justify="left")

    selection = input("Please type in a number from the list below. \n #: ")

    if selection == '1':
        os.system(f"python3 {logger_path}")  # run "py_dir/logger.py"

    if selection == '2':
        os.system(f"python3 {loginlog_path}")  # run "py_dir/loginlog.py"

    elif selection == '3':
        os.system(f"python3 {listfiles_path}")  # run "py_dir/listfiles.py"

    elif selection == '4':
        print(lslog)
        os.system(f"python3 {readfile_path}")  # run "py_dir/readfile.py"

    elif selection == '5':
        print(lslog)
        os.system(f"python3 {searchlog_path}")  # run "py_dir/searchlog.py"

    elif selection == '6':
        print(lslog)
        os.system(f"python3 {delfile_path}")  # run "py_dir/delfile.py"

    elif selection == 'Quit' or "quit" or "QUIT" or "Exit" or "Exit" or "exit" or "E" or "Q":
        print("Have a nice day!")
        break
    else:
        pass
