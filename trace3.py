#!/usr/bin/env python2
import urllib2
import urllib
import cookielib

class Trace3():
	""" Trace3 module used to login to the external trace3 module and extract the work csv file """
	def __init__(self, user, password, baseurl='https://trace3.windriver.com/'):
		cj = cookielib.CookieJar()
		self.baseurl = baseurl
		self.user = user
		self.password = password
		self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
		self.opener.addheaders = [('User-agent', 'Tester')]
		urllib2.install_opener(self.opener)

	def _req(self, url, payload=None):
		url = self.baseurl + url
		req=None
		if payload != None:
			data = urllib.urlencode(payload)
			req = urllib2.Request(url, data)
		else:
			req = urllib2.Request(url)
		return urllib2.urlopen(req)

	def login(self):
		payload = {
   			'username': self.user,
  			'password': self.password,
		 	'login': 'Log in'
		}
		ret = self._req('index-action.php', payload)
		return ret.read().find('success') > 0

	def getcsv(self):
		ret = self._req('filters/export.php?project_id=1241&filter_id=9239&export=2&count=40&format_id=4773')
		return ret
	
	def logout(self):
		self._req('logout.php')


if __name__=="__main__":
	import sys
	print "Login"
	t = Trace3(sys.argv[1], sys.argv[2])
	if not t.login():
		print "Could not login"
		exit(1)
	print t.getcsv().read()
	t.logout()

