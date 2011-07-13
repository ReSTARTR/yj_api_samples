#!/usr/bin/python
# -*- coding: utf-8 -*-

from yahooapi import yahoo_api
yahoo_api.YahooApi.appid="<YOUR_APPID>"

############################################
from yahooapi import shinsai
# shinsai/volunteers
def test_volunteers():
  vol = shinsai.Volunteers()
  rows=vol.query()
  print "%s\t%s" % ('count', vol.count())
  print "%s\t%s" % ('hits', vol.hits())
  print "%s\t%s" % ('offset', vol.offset())
  for m in vol.rowset():
    print m['Title']
    print m['Url']

# archive/search
def test_shinsai_archive_search():
  # main
  photos=shinsai.ArchiveSearch()
  rows=photos.query([('query', "思い出"), ('st_org_date', '1299769200'), ("en_org_date", '1300201199')])
  print "%s\t%s" % ('count', photos.count())
  print "%s\t%s" % ('hits', photos.hits())
  print "%s\t%s" % ('offset', photos.offset())
  for p in photos.rowset():
    print p['Id']
    print p['PhotoData']['OriginalUrl']

# shinsai/Archive/area
def test_shinsai_archive_area():
  aa = shinsai.ArchiveArea()
  rows=aa.query([
    ('jis', '07')]
  ) # 07=岩手県
  print "%s\t%s" % ('count', aa.count())
  print "%s\t%s" % ('hits', aa.hits())
  print "%s\t%s" % ('offset', aa.offset())
  for row in aa.rowset():
    print row['Name']
    print row['TotalCount']
    print row['CountBefore']
    
  rows=aa.query([
    ('ld_lat' , 39.38279616808606), 
    ('ld_lon' , 139.83389951500007),
    ('ru_lat' , 40.023066400461516),
    ('ru_lon' , 142.47061826500007),
    ('level'  , 2)]
  ) # 岩手県盛岡市 中心
  print "%s\t%s" % ('count', aa.count())
  print "%s\t%s" % ('hits', aa.hits())
  print "%s\t%s" % ('offset', aa.offset())
  for row in aa.rowset():
    print row['Name']
    print row['TotalCount']
    print row['CountBefore']

############################################
from yahooapi import setsuden
# setuden/LatestPowerUsage
def test_setsuden_latest_power_usage():
  pow = setsuden.LatestPowerUsage()
  pow.query()
  row = pow.row()
  print "%s\t%s" % ('Usage: ', row['Usage'])
  print "%s\t%s" % ('Date: ', row['Date'])
  print "%s\t%s" % ('Capacity: ', row['Capacity'])
  print "%s\t%s" % ('Hour: ', row['Hour'])
  print "%s\t%s" % ('Area: ', row['Area'])

# setuden/ElectricPowerForecast
def test_setsuden_electric_power_usage():
  pow = setsuden.ElectricPowerForecast()
  pow.query([('date','20110712')])
  row = pow.row()
  print "%s\t%s" % ('CurrentTime: ' , row['CurrentTime'])
  print "%s\t%s" % ('UpdateTime: '  , row['UpdateTime'])
  print "%s\t%s" % ('Forecast:', row['Forecast'])
  print "%s\t%s" % ('count:'  , pow.count())
  print "%s\t%s" % ('hits:'   , pow.hits())
  print "%s\t%s" % ('offset:' , pow.offset())

############################################
# main
print "# shinsai ################"
print "# volunteer "
test_volunteers()
print "# Archive/search"
test_shinsai_archive_search()
print "# Archive/area"
test_shinsai_archive_area()

print "# setsuden ################"
print "# LatestPowerUsage"
test_setsuden_latest_power_usage()
print "# ElectricPowerUsage"
test_setsuden_electric_power_usage()
