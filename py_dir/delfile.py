import os
from settings.config import settingslog_path
from settings.config import listfiles_path

lslog = [file for file in os.listdir(settingslog_path) if file.endswith('.log')]
file_count = len(lslog)

os.system(f"python3 {listfiles_path}")

if file_count > 0:
    print(lslog)

    del_file = input("Please type in the filename of the file you wish to DELETE! \n #: ")
    os.remove(os.path.join(settingslog_path, del_file))
else:
    print("No files found!")

