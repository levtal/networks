#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 9 -
# using the 'verbose_handler.py' to prints requests and responses.
#

url ='http://www.ietf.org/rfc/rfc2616.txt'
from verbose_handler import VerboseHTTPHandler
import urllib, urllib2
opener = urllib2.build_opener(VerboseHTTPHandler)
info = opener.open(url)# open and print verbose massages
code = info.code
print("Code = '%s'." % code)
msg = info.msg
print("msg = '%s'." % msg)
#page 143
keys = sorted(info.headers.keys())# key is alist of key headers

print (keys)

