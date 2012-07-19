#! /usr/bin/python

import urllib
import sys
import time

# Currently on release 3.1180.719
CEF_OSX_URL = "http://chromiumembedded.googlecode.com/files/cef_binary_3.1180.719_macosx.zip"
CEF_WIN_URL = "http://chromiumembedded.googlecode.com/files/cef_binary_3.1180.719_windows.zip"

class Reporter:
	def __init__(self):
		self._last_report_length = 0
		self._start_time = -1.0

	def report(self, blocks, blocksize, filesize):
		if self._start_time < 0:
			self._start_time = time.time()

		downloaded = blocks*blocksize
		percent = int(downloaded*100/filesize)
		elapsed = time.time() - self._start_time
		speed = downloaded / 1024 / elapsed
		message = "{0}% [{1}/{2} bytes, {3:.3f} KB/s]".format(percent, downloaded, filesize, speed)

		sys.stdout.write("\b" * self._last_report_length)
		sys.stdout.write(message)
		sys.stdout.flush()

		self._last_report_length = len(message)

def download(url, filename):
	r = Reporter()
	urllib.urlretrieve(url, filename, r.report)

download(CEF_OSX_URL, 'joel')
