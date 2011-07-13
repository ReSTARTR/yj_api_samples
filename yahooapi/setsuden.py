#!/usr/bin/python
# -*- coding: utf-8 -*-

from yahoo_api import YahooApi

class Setsuden(YahooApi):
  def rowset(self):
    raise Exception, "method unexists."

class LatestPowerUsage(Setsuden):
  entry_point="http://setsuden.yahooapis.jp/v1/Setsuden/latestPowerUsage"
  root_key = 'ElectricPowerUsage'
  row_key = "Usage"
  query_strings=[
    ('area'     , 'tokyo')
   ,('datetime' , False)
   ,('output'   , 'json')
   ,('callback' , False)
  ]
  response_fields = [
  	 "Area", "Usage", "Capacity", "Date", "Hour"
  ]

class ElectricPowerForecast(Setsuden):
  entry_point="http://setsuden.yahooapis.jp/v1/Setsuden/electricPowerForecast"
  root_key = 'ElectricPowerForecasts'
  query_strings=[
     ('output'  , 'json')
    ,('callback', False)
    ,('area'    , 'tokyo')
    ,('date'    , False) # YYYYMMDD 
    ,('results' , 10) # max 169
    ,('start'   , 1) # max 169
  ]
  response_fields = [
  	 "CurrentTime", "UpdateTime", "Forecast"
  ]
  forecast_fields = [
    "Usage", "Capacity", "Date", "Hour"
  ]
  attributes_fields = [
    "totalForecastsAvailable", "totalForecastsReturned", "firstForecastsPosition"
  ]
  def hits(self):
    return self._result_object[self.root_key]['@totalForecastsReturned']
  def count(self):
    return self._result_object[self.root_key]['@totalForecastsAvailable']
  def offset(self):
    return self._result_object[self.root_key]['@firstForecastsPosition']
# LatestPowerUsage
