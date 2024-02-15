import os
from settings.config import settingslog_path

lslog = [file for file in os.listdir(settingslog_path) if file.endswith('.log')]
file_count = len(lslog)

if file_count > 0:
    input_file = input("Please type in the filename of the file you wish to READ! \n #: ")
    with open(os.path.join(settingslog_path, input_file), 'r') as f:
        print(f.read())
        f.close()
else:
    print("No files found!")