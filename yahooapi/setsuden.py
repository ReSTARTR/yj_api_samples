#!/usr/bin/python
# -*- coding: utf-8 -*-

from yahoo_api import YahooApi

class LatestPowerUsage(YahooApi):
  entry_point="http://setsuden.yahooapis.jp/v1/Setsuden/latestPowerUsage"
  query_strings=[
    ('area'     , 'tokyo')
   ,('datetime' , False)
   ,('output'   , 'json')
   ,('callback' , False)
  ]
  response_fields = [
  	 "Area", "Usage", "Capacity", "Date", "Hour"
  ]

class ElectricPowerForecast(YahooApi):
  entry_point="http://setsuden.yahooapis.jp/v1/Setsuden/electricPowerForecast"
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
# LatestPowerUsage
