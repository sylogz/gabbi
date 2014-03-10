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
"""Converts a csv file from trace3 to the stated report format"""
	ret = ""
	status = {
		"Delivered"   : ["Completed", "Delivered", "Done with"],
		"Blocked"     : ["Blocked", "Could not work with"],
		"Deleted"     : ["Done with"],
		"Completed"   : ["Completed", "Finished"],
		"In Progress" : ["Working on", "Working with", "Not done with"],
		"Not Started" : ["Retrived task", "New task", "Starting  with"],
		"On Hold"     : ["On hold", "Background working", "When I feel for it"],
	}
	internal = { 
		"0" : ["external", "ericsson"],
		"1" : ["my", "internal"],
	}
	
	ASSIGNMENT= ["task", "assignment"]
	
	ADD_LINK=False
	
	rc = random.choice
	wl=0
	
	ret += "1) What tasks I worked on during this week?\n"
	for row in csv:
		if row[2] == "Status":
			continue # Skip first row FIXME: use as dict
		ret += " ".join(["    ",
			rc(status[row[2]]),
			rc(internal[row[3]]),
			rc(ASSIGNMENT),
			"to",
			row[5].lower()]
		)
		if ADD_LINK:
			ret += "(%s)" % row[4]
		else:
			ret += "."
		ret += "\n"
		if row[2] == "In Progress":
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
