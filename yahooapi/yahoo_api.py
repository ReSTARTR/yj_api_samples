#!/usr/bin/python
# -*- coding: utf-8 -*-

import pycurl
import json
import urllib
import time

class YahooApi:
  appid=""
  entry_point=""
  query_strings=[]
  response_fields=[]
  
  _result_object = {}
  
  root_key = ""
  row_key=''
  
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
      self._result_object = rows
      return rows
    except ValueError, err:
      print "[ERROR]", err
    return False
	
  def query(self, args=[]):
    for i in range(0,3):
      rows = self._query(args)
      if rows != False:
        break
      else:
        time.sleep(1)
        print "retry"
  
  def attributes(self, key=""):
    if self.root_key == "" or self.root_key not in self._result_object:
      return False
    
    root = self._result_object[self.root_key]
    if 'attributes' in root:
      if key != '' and key in root['attributes']:
        return root['attributes'][key]
      else:
        return root['attributes']
  
  def count(self):
    return self.attributes("totalResultsReturned")
  def hits(self):
    return self.attributes("totalResultsAvailable")
  def offset(self):
    return self.attributes("firstResultPosition")
  def rowset(self):
    return self._result_object[self.root_key][self.row_key]
  def row(self):
    return self._result_object[self.root_key]
