#!/usr/bin/env python3

import sys
import select
import os
import psutil
import datetime

def timer():
	bootTime = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%d-%m-%Y %H:%M:%S")
	timeElapsed = round(datetime.datetime.now().timestamp() - psutil.boot_time())
	return bootTime, timeElapsed

def write_csv(bootTime, timeElapsed):
	if "pybye" not in os.listdir(f"/home/{user}/Documents"):
		os.mkdir(logPath)
		with open(f"{logPath}/data.csv", "a") as f:
			f.write("bootDate,bootTime,timeElapsed")
	bootDate = bootTime[:10]
	bootTime = bootTime[11:]
	with open(f"{logPath}/data.csv", "a") as f:
		f.write(f"\n{bootDate},{bootTime},{timeElapsed}")
	print(f"Time log saved as {logPath}/log.csv")

t = 5
user = os.getlogin()
global logPath
logPath = f"/home/{user}/Documents/pybye"

print("\nPress \033[1mENTER\033[0m to cancel")
print(f"Shutdown in {t} seconds")

i, o, e = select.select([sys.stdin], [], [], t)
if i:
	print("Shutdown cancelled")
else:
	bootTime, timeElapsed = timer()
	write_csv(bootTime, timeElapsed)
	print("Shutdown initiated")
	os.system("shutdown now")
