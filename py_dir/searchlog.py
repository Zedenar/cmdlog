import os
from settings.config import search_path

input_file = input("Enter a filename:\n#: ")
print(search_path)
try:
    with open(os.path.join(search_path, input_file), 'r') as f:

        logsearch = input("Enter a keyword:\n#: ")

        for line in f:
            line = line.rstrip()
            if logsearch in line:
                print(line)
    f.close()
except:
    print("File can not be opened, please try another filename.")
    quit()


