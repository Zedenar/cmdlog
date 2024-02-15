import os
from settings.config import settingslog_path

print('-----LOGFILES-----')

lslog = [file for file in os.listdir(settingslog_path) if file.endswith('.log')]
file_count = len(lslog)

if file_count > 0:
    print(lslog)
else:
    print("No files found!")

print('------------------')
