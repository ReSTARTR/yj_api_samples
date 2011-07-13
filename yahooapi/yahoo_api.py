#!/usr/bin/python
# -*- coding: utf-8 -*-

import pycurl
import json
import urllib
import time

class YahooApi:
  appid="<YOUR_APP_ID>"
  entry_point=""
  query_strings=[]
  response_fields=[]
  _result_buffer=[]
  def __init__(self):
    self.query_strings.append(('appid', self.appid))
  
  def body_callback(self, buf_):
    self._result_buffer.append(buf_)
  
  def _query(self, args=[]):
    self._result_buffer = []
    curl = pycurl.Curl()
    qs = [q for q in self.query_strings if q[1]!=False]
    for a in args:
      qs.append((a[0], a[1]))
    url = self.entry_point + "?"+ urllib.urlencode(qs, 'UTF-8')

    curl.setopt(curl.URL, url)
    curl.setopt(curl.WRITEFUNCTION, self.body_callback)
    curl.setopt(curl.MAXREDIRS,5)
    curl.setopt(curl.CONNECTTIMEOUT,30)
    curl.setopt(curl.TIMEOUT,300)
    curl.setopt(curl.NOSIGNAL,1)

    try:
      curl.perform()
      curl.close()
      rows = json.loads("".join(self._result_buffer))
      return rows
    except ValueError, err:
      print "[ERROR]", err
    return False
	
  def query(self, cf, args=[]):
    for i in range(0,3):
      rows = self._query(args)
      if rows != False:
        cf(rows)
        break
      else:
        time.sleep(1)
        print "retry"
