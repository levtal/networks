#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 9 - url_anatomy.py
# python 2.7
from urlparse import urlparse, urldefrag, parse_qs, parse_qsl

#parse the complex URL to its parts
u = 'http://example.com:8080/Nord%2FLB/logo?shape=square&dpi=96'
p = urlparse(u)
print("URL: %s" % u)

print(p)

#line 162
print(parse_qs(p.query))# {'shape': ['square'], 'dpi': ['96']}
print("Parmeters:  ")
r = parse_qs('mode=topographic&pin=Boston&pin=San%20Francisco')
print(r)