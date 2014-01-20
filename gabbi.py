#!/usr/bin/env python2

from trace3 import Trace3
from csv2rep import Csv2Rep
import sys
import csv
import os

conffile='gabbi.csv'
conf={
	'user' : "", 
	'pass' : "",
	'name' : "",
	'mail' : "",
}

if os.path.isfile(conffile):
	f = open(conffile, "r")
	r = csv.reader(f, delimiter=',', quotechar='"')
	for row in r:
		conf[row[0]] = row[1]
	f.close()

print ""
print "Current configuration:"
print ""
for row in conf:
	print " " + row.title() + " : " + conf[row]
print ""
print "Use this configuration (Y/n)? ",
ok=sys.stdin.readline().strip()

if len(ok) != 0 and ok.lower()[0] != "y":
	print "Your name ("+conf['name']+")"
	print ":",
	conf['name'] = sys.stdin.readline().strip()

	print "Trace3 User ("+conf['user']+")"
	print ":",
	conf['user'] = sys.stdin.readline().strip()

	print "Trace3 Password ("+conf['user']+")"
	print ":",
	conf['pass'] = sys.stdin.readline().strip()

	print "Auto mail to ("+conf['user']+")"
	print ":",
	conf['mail'] = sys.stdin.readline().strip()

	f = open(conffile, "w+")
	w = csv.writer(f, delimiter=',', quotechar='"')
	for c in conf:
		w.writerow([c, conf[c]])
	f.close()

print ""
print "Logging in to trace3"
t3 = Trace3(conf['user'], conf['pass'])
if not t3.login():
	raise "Could not login"
	exit(1)
print "Getting csv report"
r = csv.reader(t3.getcsv(), delimiter=',', quotechar='"')
print "Logging out from trace3"
t3.logout()
print "Generating report"
ret = Csv2Rep(r)
print ""
print ""
print ret
print ""
print ""
