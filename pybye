#!/usr/bin/env python3

import sys
import select
import os
import psutil
import datetime
import termplotlib as tpl

def timer():
	bootTime = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%d-%m-%Y %H:%M:%S")
	timeElapsed = round(datetime.datetime.now().timestamp() - psutil.boot_time())
	return bootTime, timeElapsed

def write_csv(bootTime, timeElapsed):
	if "pybye" not in os.listdir(f"/home/{user}/Documents"):
		os.mkdir(logPath)
		with open(f"{logPath}/log.csv", "a") as f:
			f.write("bootDate,timeElapsed")
	bootDate = bootTime[:10]
	with open(f"{logPath}/log.csv", "r") as f:
		logs = f.readlines()
	lastLog = logs[-1].split(",")
	if lastLog[0] == bootDate:
		lastLog[-1] = str(int(lastLog[-1]) + timeElapsed)
		logs[-1] = ",".join(lastLog)
	else:
		logs.append(f"\n{bootDate},{timeElapsed}")
	with open(f"{logPath}/log.csv", "w") as f:
		f.writelines(logs)
	print(f"Time log saved as {logPath}/log.csv")

def pybye_graph():
	print("\033[1mDate\033[0m\t\t\033[1mTime (in seconds)\033[0m")
	with open(f"{logPath}/log.csv", "r") as f:
		logs = f.readlines()[1:]
	dates = [log[:10] for log in logs]
	time = [int(log[11:]) for log in logs]
	fig = tpl.figure()
	fig.barh(time, dates, force_ascii=False)
	fig.show()

global user
user = os.getlogin()
global logPath
logPath = f"/home/{user}/Documents/pybye"

if len(sys.argv) > 1:
	if sys.argv[1] == "graph":
		pybye_graph()
else:
	t = 5
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
