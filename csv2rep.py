#!/usr/bin/python
import os
import random

## BSD-3
# (c) 2013 - Jonas Zetterberg
# 
# Authors: 
# * Jonas Zetterberg
# * Per Hallsmark

def Csv2Rep(csv):
	ret = ""
	DELIVERED = ["Completed", "Delivered", "Done with"]
	WORKING_ON = ["Working on", "Working with", "Not done with"]
	
	NOT_STARTED = ["Retrived task", "New task", "Starting with"]

	INTERNAL = ["my", "internal"]
	EXTERNAL = ["external", "ericsson"]
	
	ASSIGNMENT= ["task", "assignment"]
	
	ADD_LINK=False
	
	rc = random.choice
	wl=0
	
	ret += "1) What tasks I worked on during this week?\n"
	for row in csv:
		if row[2] == "Status":
			continue # Skip first row FIXME: use as dict
		ret += "    "
		if row[2] == "Delivered" or row[2] == "Deleted":
			ret += rc(DELIVERED)
		elif row[2] == "In Progress":
			ret += rc(WORKING_ON)
		elif row[2] == "Not Started":
			ret += rc(NOT_STARTED)
		else:
			print "AAARGH: Status type not found, please add and submit"
			print row[2]
			raise 
		if row[3] == "1":
			ret += rc(INTERNAL)
		else:
			ret += rc(EXTERNAL)
		ret += rc(ASSIGNMENT) + "to" + row[5].lower()
		if ADD_LINK:
			ret += "(%s)" % row[4]
		else:
			ret += "."
		ret += "\n"
		wl = wl+1;
	
	ret += "2) Anything preventing me to accomplish the tasks?\n"
	ret += "     Not that I know of.\n"
	
	ret += "3) My workload (I am working more than normal time? Less?)\n"
	if wl <= 4:
		ret += "     Normal workload\n"
	elif wl <= 6:
		ret += "     High workload\n"
	elif wl <= 8:
		ret += "     Very high workload\n"
	else:
		ret += "     I am hitting the wall!\n"
	
	ret += "4) Any new opportunity for business I have heard?\n"
	if wl < 5:
		ret += "     No\n" 
	else:
		ret += "     There seems to be a need for more consultants at my workplace"
	
	return ret
