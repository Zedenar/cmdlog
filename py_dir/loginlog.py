import subprocess
import time

cmd = "last"

# Start command in background using subprocess.Popen()
p = subprocess.Popen(cmd, shell=True)

# Continue execution of the main program
while p.poll() is None:  # poll returns None if process is still running
    time.sleep(1)  # wait for a second before checking again
else:
    print("\n")
