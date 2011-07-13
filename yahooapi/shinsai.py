#!/usr/bin/python
# -*- coding: utf-8 -*-

from yahoo_api import YahooApi

class Volunteers(YahooApi):
  entry_point="http://shinsai.yahooapis.jp/v1/volunteers"
  root_key = "Messages"
  row_key = "Message"
  query_strings=[
    ('results' , 30)
   ,('start'   , 1)
   ,('lat'     , False)
   ,('lon'     , False)
   ,('sort'    , "date")
   ,('status'  , 1)
   ,('output'  , 'json')
   ,('callback', False)
  ]
  response_fields = [
  	 "Id", "Status", "RegTime", "UpdateTime", "Title", "Url", "Summary", 
     "Lat", "Lon", "Pref", "Address", "Organization", "Contact", "ContactPerson"
  ]
# ShinsaiVolunteers

class ArchiveSearch(YahooApi):
  entry_point="http://shinsai.yahooapis.jp/v1/Archive/search"
  # output = xml/php/json
  root_key = "ArchiveData"
  row_key = 'Result'
  query_strings=[
     ('output'  , 'json') # xml/php/json
    ,('callback', False)
    ,('start'   , 1)
    ,('results' , 20) # max 20
    ,('id'      , False)
    ,('query'   , False)
    ,('period'  , False) # before/after
    ,('tag'     , False) # person/scene/object/others (multiple with comma)
    ,('type'    , 'photo') # 
    ,('guid'    , False)
    ,('st_org_date' , False)
    ,('en_org_date' , False)
    ,('jis'     , False) # pref_code(2 digits) or city_code(5 digits) (multiple with comma)
    ,('lat'     , False)
    ,('lon'     , False)
    ,('scale'   , 500)
    ,('ld_lat'  , False)
    ,('ld_lon'  , False)
    ,('ru_lat'  , False)
    ,('ru_lon'  , False)
    ,('hard_flag'  , 'false')
    #,('sort'    , '+cre_time') # -cre_time / +cre_time / -org_time / +org_time

  ]
  attributes_fields = [
    u'totalResultsReturned', 
    u'totalResultsAvailable', 
    u'firstResultPosition'
  ]
  response_fields = [
    u'Id',
    u'Type', 
    u'Guid', 
    u'Nickname', 
    u'Created', 
    u'OrgDate', 
    u'Description', 
    u'Lat', 
    u'Lon', 
    u'Address', 
    u'HardFlag', 
    u'Tag', 
    u'PhotoData', 
  ]
  photoData_fileds = [
    "OriginalUrl", "OriginalHeight", "OriginalWidth",
    "ThumbnailUrl", "ThumbnailHeight", "ThumbnailWidth",
    "SquareUrl", "SquareHeight", "SquareWidth",
  ]
# ShinsaiVolunteers

class ArchiveArea(YahooApi):
  entry_point="http://shinsai.yahooapis.jp/v1/Archive/area"
  root_key = "AreaData"
  row_key = 'Result'
  query_strings=[
     ('output'  , 'json')
    ,('callback', False)
    ,('start'   , 1)
    ,('results' , 30)
    ,('level'   , False) # pref=>1, city=>2
    ,('period'  , False) # before/after
    ,('jis'     , False) # pref(2 digit) or city(5 digit) (multiple with comma)
    ,('lat'     , False)
    ,('lon'     , False)
    ,('ld_lat'  , False) # left down lat
    ,('ld_lon'  , False) # left down lon
    ,('ru_lat'  , False) # right upper lat
    ,('ru_lon'  , False) # right upper lon
  ]
  response_fields = [
  	 u"Id", 
  	 u"TotalCount", 
  	 u"CountBefore", 
  	 u"CountAfter", 
  	 u"Name", 
  	 u"NameKana", 
  	 u"Lat", u"Lon"
  ]
  attributes_fields = [
    u'totalResultsReturned', 
    u'totalResultsAvailable', 
    u'firstResultPosition'
  ]
# ShinsaiVolunteers
