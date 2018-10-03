#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 9 - url_anatomy.py
# python 2.7
from urlparse import urlparse, urldefrag, parse_qs, parse_qsl

#parse the complex URL to its parts
u = 'http://example.com:8080/Nord%2FLB/logo?shape=square&dpi=96'
p = urlparse(u)
print("URL: %s" % u)

print(p) #ParseResult(scheme='http', netloc='example.com:8080',
         #  path='/Nord%2FLB/logo', params='', query='shape=square&dpi=96',
         # fragment='')
print('scheme = ', p.scheme)
#line 140
print(parse_qs(p.query))# {'shape': ['square'], 'dpi': ['96']}
print("Parmeters:  ")
r = parse_qs('mode=topographic&pin=Boston&pin=San%20Francisco')
print(r)

#Remove the anchor (#),
u = 'http://docs.python.org/library/urlparse.html#item22'
udfrag= urldefrag(u)# the retrun type is a tuple
#('http://docs.python.org/library/urlparse.html', 'urlparse.urldefrag')


print("URL defrag :")

# Get the number of items in a udfrag Tuple
length =len(udfrag)
print("Tuple Length :", length)
print(udfrag)# ('http://docs.python.org/library/urlparse.html','item22'')
print(udfrag[0])  # http://docs.python.org/library/urlparse.html
print(udfrag[1])  # 'item22'

print("slice", udfrag[0:length])
print "this is a tuple: %s" % (udfrag,)# Another way to print a tuple