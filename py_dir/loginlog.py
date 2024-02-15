import datetime
import subprocess
import sys
import time
import os
from settings.config import settingslog_path
from settings.config import timestring
from settings.config import history_path

# Set the path for where the logfiles and directories are stored (can be modified)
dir_list = os.listdir(settingslog_path)
username = os.getlogin() + "_"
timestr = timestring  # To change the time-format for the logfiles - please look in py_dir/config

cmd = "last"

# Create a file with the active username + date and time from "right now" - and "open" it
logoutput = username + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
sys.stdout = open(os.path.join(settingslog_path, logoutput) + '.log', 'w')

# Start command in background using subprocess.Popen()
p = subprocess.Popen(cmd, shell=True)

# Continue execution of the main program
while p.poll() is None:  # poll returns None if process is still running
    time.sleep(1)  # wait for a second before checking again
else:
    print("Command finished")

# Print the result to the logfile together with the command used (cmd)
result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print("The command used: " + cmd + "\n" + "\n" + result.stdout.decode())

# Print cmd to logs/history.log
with open(history_path, "a") as f:
    print(cmd, file=f)
    f.close()


