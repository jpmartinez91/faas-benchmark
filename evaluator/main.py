import shlex
import subprocess
import sys
from time import sleep
import schedule

count = 0


def job():
    global count
    print(count)
    subprocess.Popen(args)
    count = count + 1


schedule.every(1).minute.do(job)

for i in range(1, 2):
    command_line = f"python exec.py -f {i}"
    args = shlex.split(command_line)
    print(command_line)
    count = 0
    while (count < 300):
        schedule.run_pending()
    print("sleeping")
    # sleep(600)
print("end...")
