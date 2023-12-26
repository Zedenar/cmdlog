# This code is open-source - do with it as you please.
#
# Please create a directory in your homefolder called ' logfiles ' e.g. /home/"username"/logfiles/
# And change >>> path = "/home/mungi/logfiles/" <<< to the username you are currently using.

import datetime     
import subprocess
import sys
import time
import os

# Set the path for where the logfiles and directories are stored (can be modified)
path = "/home/mungi/cmdlog/logfiles/"
dir_list = os.listdir(path)

# The commands you would like to run (Bash)
# cmd = "ps aux"
print("The logfiles are located in " + path)
cmd = input("Please type the $Bash command you would like to log: ")

# Set the timeformat for the filenames
# %Y = Year , %m = month , %d = day , %H = Hour , %M = Minutes , %S = Seconds
timestr = time.strftime("%Y%m%d-%H.%M.%S")


# Create a file with the date and time from right now - and open it
filename1 = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
sys.stdout = open(path + filename1 + '.log', 'w')

# Print the result to the logfile
result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(result.stdout.decode())



#---------------------------------------------------------------------------------------------------------------------
# TODO: Add the logfiles to a dictionary and create a menu e.g. and via input() make it possible to open the logfiles
# TODO: From a GUI.
# ____Logfiles___
# 0 filename1.txt
# 1 filename1.txt
# 2 filename1.txt
# 3 filename1.txt
# 4 filename1.txt
# 5 filename1.txt
#
# Please type the number of the log-file you would like to open:
