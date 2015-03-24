# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
from lxml import etree
import urllib2

url = 'http://www.google.com'
req = urllib2.Request(url)
response = urllib2.urlopen(req).read()
response = unicode(response,'GBK')

d = pq(response)
print d('.tr3 h3 a')
