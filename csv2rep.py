#!/usr/bin/python
import sys
import os
import random

if len(sys.argv) <= 1:
	print ""
	print "Usage", sys.argv[0], " [cvs-file] <name>"
	print
	exit(1)

def mk():
	DELIVERED = ["Completed", "Delivered", "Done with"]
	WORKING_ON = ["Working on", "Working with", "Not done with"]
	
	INTERNAL = ["my", "internal"]
	EXTERNAL = ["external", "ericsson"]
	
	ASSIGNMENT= ["task", "assignment"]
	
	ADD_LINK=False
	
	rc = random.choice
	wl=0
	
	f = open(sys.argv[1])
	
	print "1) What tasks I worked on during this week?"
	for line in f:
		parts=[ p.strip("\" \\\n") for p in line.split(",") ]
		if parts[2] == "Status":
			continue
		print "    ",
		if parts[2] == "Delivered":
			print rc(DELIVERED),
		elif parts[2] == "In Progress":
			print rc(WORKING_ON),
		else:
			print parts[2]
			raise 
		if parts[3] == "0":
			print rc(INTERNAL),
		else:
			print rc(EXTERNAL),
		print rc(ASSIGNMENT), "to", parts[6].lower(),
		if ADD_LINK:
			print "(%s)" % parts[4]
		else:
			print "."
		wl = wl+1;
	
	print "2) Anything preventing me to accomplish the tasks?"
	print "     Not that I know of."
	
	print "3) My workload (I am working more than normal time? Less?)"
	if wl <= 4:
		print "     Normal workload"
	elif wl <= 6:
		print "     High workload"
	elif wl <= 8:
		print "     Very high workload"
	else:
		print "     I am hitting the wall!"
	
	print "4) Any new opportunity for business I have heard?"
	if wl < 5:
		print "     No" 
	else:
		print "     There seems to be a need for more consultants at my workplace"
	
	if len(sys.argv) >= 3:
		print ""
		print "//", sys.argv[2]

try:
	mk()
except:
	print "Unexpected error:", sys.exc_info()[0]
	exit(1)
