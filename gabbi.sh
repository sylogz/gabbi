#!/bin/sh -e

## BSD-3
# (c) 2013 - Jonas Zetterberg
# 
# Authors: 
# * Jonas Zetterberg
# * Per Hallsmark

RCFILE="$HOME/.gabbirc"

! [ -f $HOME/.mkrrc ] || mv $HOME/.mkrrc $RCFILE
! [ -f $RCFILE ] || . $RCFILE

if [ -z "$1" ] ; then
	echo "Add an argument to skip these questions."
	echo "Enter the name that the email should end with (or leavel empty)"
	echo -n "Name ($tname):" ; read name
	echo "Enter the username to your TRACE3 account"
	echo -n "User ($tuser):" ; read user
	echo "Enter the password to your TRACE3 account"
	echo -n "Pass ($(echo $tpass | sed -r 's/./\*/g')):" ; read pass
	echo "Enter the mail-recipiant you want to send your report to (or leave empty)"
	echo -n "Mail ($tmail):" ; read mail
fi	
[ -n "$name" ] || name=$tname
[ -n "$user" ] || user=$tuser
[ -n "$pass" ] || pass=$tpass
[ -n "$mail" ] || mail=$tmail

[ -d tmp ] || mkdir tmp

echo -n "Logging in ... "
wget -q --cookies=on --keep-session-cookies --save-cookies=tmp/cookie.txt \
	--post-data='username='$user'&password='$pass'&login="Log in"' \
	'https://trace3.windriver.com/index-action.php' \
	-O tmp/login.php
echo "Done"

echo -n "Getting csv report ... "
wget -q --cookies=on --keep-session-cookies --load-cookies=tmp/cookie.txt \
	'https://trace3.windriver.com/filters/export.php?project_id=1241&filter_id=9239&export=2&count=4&format_id=4773' \
	-O tmp/me.csv
echo "Done"

echo -n "Logging out ... "
wget -q --cookies=on --keep-session-cookies --load-cookies=tmp/cookie.txt \
	'https://trace3.windriver.com/logout.php' \
	-O tmp/logout.php
echo "Done"

echo -n "Saving info ... "
echo "tuser='$user'" > $RCFILE
echo "tpass='$pass'" >> $RCFILE
echo "tmail='$mail'" >> $RCFILE
echo "tname='$name'" >> $RCFILE
chmod 600 $RCFILE
echo "Done"

echo ""
echo ""
python csv2rep.py "tmp/me.csv" "$name" | tee mail
echo ""
echo ""

if [ -n "$mail" ] ; then
	echo -n "Mailing $mail (bcc $user) ... "
	sleep 1.0 # give user a chance to exit 
	mail -b $user -s "report E///projects" $mail < mail
	echo "Done"
fi

echo -n "Clean up ... "
rm -r tmp
echo "Done"
