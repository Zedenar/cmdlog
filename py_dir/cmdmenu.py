import os
from settings.config import listfiles_path
from settings.config import logger_path
from settings.config import readfile_path
from settings.config import delfile_path
from settings.config import ClearCommand
from settings.config import loginlog_path
from settings.config import searchlog_path
from listfiles import lslog

os.system(ClearCommand)

menu = {
    1: "Run a $Bash-command to log.",
    2: "Look at the login-attempts.",
    3: "List the logfiles.",
    4: "Read a file.",
    5: "Search for a keyword within a logfile.",
    6: "Delete a file.",
    7: "Exit/Quit"
}

while True:
    for key, value in menu.items():
        print(key, value)

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

    elif selection == '7':
        print("Have a nice day!")
        break
    else:
        pass
