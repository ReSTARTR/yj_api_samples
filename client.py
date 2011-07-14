#!/usr/bin/python
# -*- coding: utf-8 -*-

from yahooapi import yahoo_api
yahoo_api.YahooApi.appid="MOrzLIKxg67mBHMbU1E260ye7dxgd6hCfHBGd6oGRVimzf_4qa_EntfgSLZNIk6KJg--"

############################################
from yahooapi import shinsai
# shinsai/volunteers
def test_volunteers():
  vol = shinsai.Volunteers()
  vol.query()
  print "%s\t%s" % ('count' , vol.count())
  print "%s\t%s" % ('hits'  , vol.hits())
  print "%s\t%s" % ('offset', vol.offset())
  for m in vol.rowset():
    print m["Id"]
    print m["Status"] 
    print m["RegTime"]
    print m["UpdateTime"]
    print m["Title"]
    print m["Url"]
    print m["Summary"]
    print m["Lat"]
    print m["Lon"]
    print m["Pref"]
    print m["Address"]
    print m["Organization"]
    print m["Contact"]
    print m["ContactPerson"]

# archive/search
def test_shinsai_archive_search():
  # main
  photos=shinsai.ArchiveSearch()
  photos.query([('query', "思い出"), ('st_org_date', '1299769200'), ("en_org_date", '1300201199')])
  print "%s\t%s" % ('count' , photos.count())
  print "%s\t%s" % ('hits'  , photos.hits())
  print "%s\t%s" % ('offset', photos.offset())
  for p in photos.rowset():
    print p[u'Id']
    print p[u'Type'] 
    print p[u'Guid']
    print p[u'Nickname'] 
    print p[u'Created'] 
    print p[u'OrgDate']
    print p[u'Description']
    print p[u'Lat']
    print p[u'Lon']
    print p[u'Address']
    print p[u'HardFlag']
    print p[u'Tag']
    print p[u'PhotoData']
    print p['PhotoData']['OriginalUrl']
    print p['PhotoData']['OriginalHeight']
    print p['PhotoData']['OriginalWidth']
    print p['PhotoData']['ThumbnailUrl']
    print p['PhotoData']['ThumbnailHeight']
    print p['PhotoData']['ThumbnailWidth']
    print p['PhotoData']['SquareUrl']
    print p['PhotoData']['SquareHeight']
    print p['PhotoData']['SquareWidth']

# shinsai/Archive/area
def test_shinsai_archive_area():
  aa = shinsai.ArchiveArea()
  aa.query([
    ('jis', '07')]
  ) # 07=岩手県
  print "%s\t%s" % ('count' , aa.count())
  print "%s\t%s" % ('hits'  , aa.hits())
  print "%s\t%s" % ('offset', aa.offset())
  for row in aa.rowset():
    print row[u"Id"]
    print row[u"TotalCount"]
    print row[u"CountBefore"]
    print row[u"CountAfter"]
    print row[u"Name"]
    print row[u"NameKana"]
    print row[u"Lat"] 
    print row[u"Lon"]
  
  aa.query([
    ('ld_lat' , 39.38279616808606), 
    ('ld_lon' , 139.83389951500007),
    ('ru_lat' , 40.023066400461516),
    ('ru_lon' , 142.47061826500007),
    ('level'  , 2)]
  ) # 岩手県盛岡市 中心
  print "%s\t%s" % ('count' , aa.count())
  print "%s\t%s" % ('hits'  , aa.hits())
  print "%s\t%s" % ('offset', aa.offset())
  for row in aa.rowset():
    print row[u"Id"]
    print row[u"TotalCount"]
    print row[u"CountBefore"]
    print row[u"CountAfter"]
    print row[u"Name"]
    print row[u"NameKana"]
    print row[u"Lat"] 
    print row[u"Lon"]

############################################
from yahooapi import setsuden
# setuden/LatestPowerUsage
def test_setsuden_latest_power_usage():
  pow = setsuden.LatestPowerUsage()
  pow.query()
  row = pow.row()
  print "%s\t%s %s" % ('Usage: ', row['Usage']['$'], row['Usage']['@unit'])
  print "%s\t%s %s" % ('Capacity: ', row['Capacity']['$'], row['Capacity']['@unit'])
  rate = (row['Usage']['$'] / (row['Capacity']['$'] * 1.0))*100
  print rate
  print "%s\t%s" % ('Date: '    , row['Date'])
  print "%s\t%s" % ('Hour: '    , row['Hour'])
  print "%s\t%s" % ('Area: '    , row['Area'])

# setuden/ElectricPowerForecast
def test_setsuden_electric_power_usage():
  pow = setsuden.ElectricPowerForecast()
  pow.query([('date','20110712')])
  row = pow.row()
  print "%s\t%s" % ('CurrentTime: ' , row['CurrentTime'])
  print "%s\t%s" % ('UpdateTime: '  , row['UpdateTime'])
  print "%s\t%s" % ('Forecast:'     , row['Forecast'])
  print "%s\t%s" % ('count:'        , pow.count())
  print "%s\t%s" % ('hits:'         , pow.hits())
  print "%s\t%s" % ('offset:'       , pow.offset())

############################################
# main
functions = [
 test_volunteers
,test_shinsai_archive_search
,test_shinsai_archive_area
,test_setsuden_latest_power_usage
,test_setsuden_electric_power_usage
]
for f in functions:
  print "#########################"
  print "# %s" % f.__name__
  f()
