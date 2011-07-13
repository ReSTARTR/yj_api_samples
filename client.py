#!/usr/bin/python
# -*- coding: utf-8 -*-

from yahooapi import setsuden
from yahooapi import shinsai
import urllib

# shinsai/volunteers
def test_volunteers():
  def vol_(rows):
    print "%s:\t%s" % ('totalResultsReturned', rows['Messages']['attributes']['totalResultsReturned'])
    print "%s:\t%s" % ('totalResultsAvailable', rows['Messages']['attributes']['totalResultsAvailable'])
    print "%s:\t%s" % ('firstResultPosition', rows['Messages']['attributes']['firstResultPosition'])
    for row in rows['Messages']['Message']:
      for f in vol.response_fields:
        print f + " : \t" + row[f]
  # main
  vol = shinsai.Volunteers()
  rows=vol.query(vol_)

# archive/search
def test_shinsai_archive_search():
  def archive_search(rows):
    print "%s:\t%s" % ('totalResultsReturned', rows['ArchiveData']['attributes']['totalResultsReturned'])
    print "%s:\t%s" % ('totalResultsAvailable', rows['ArchiveData']['attributes']['totalResultsAvailable'])
    print "%s:\t%s" % ('firstResultPosition', rows['ArchiveData']['attributes']['firstResultPosition'])
    for row in rows['ArchiveData']['Result']:
      print row.keys()
      for f in photos.response_fields:
        if f in ["PhotoData", "Tag"]:
          print row[f]
        elif f == "Id":
          print row[f]
        else:
          print f + "\t" + row[f]
  # main
  photos=shinsai.ArchiveSearch()
  rows=photos.query(archive_search, [('query', "思い出"), ('st_org_date', '1299769200'), ("en_org_date", '1300201199')])

# shinsai/Archive/area
def test_shinsai_archive_area():
  def archive_area(rows):
    print "%s:\t%s" % ('totalResultsReturned', rows['AreaData']['attributes']['totalResultsReturned'])
    print "%s:\t%s" % ('totalResultsAvailable', rows['AreaData']['attributes']['totalResultsAvailable'])
    print "%s:\t%s" % ('firstResultPosition', rows['AreaData']['attributes']['firstResultPosition'])
    for row in rows['AreaData']['Result']:
      for f in shinsai.ArchiveArea.response_fields:
        print "%s:\t%s" % (f, row[f])
  # main
  aa = shinsai.ArchiveArea()
  rows=aa.query(archive_area, [
    ('jis', '07')]
  ) # 07=岩手県
  rows=aa.query(archive_area, [
    ('ld_lat' , 39.38279616808606), 
    ('ld_lon' , 139.83389951500007),
    ('ru_lat' , 40.023066400461516),
    ('ru_lon' , 142.47061826500007),
    ('level'  , 2)]
  ) # 岩手県盛岡市 中心

# setuden/LatestPowerUsage
def test_setsuden_latest_power_usage():
  def lpu(rows):
    for f in pow.response_fields:
      print "%s\t%s" % (f , str(rows['ElectricPowerUsage'][f]))
  # main
  pow = setsuden.LatestPowerUsage()
  rows=pow.query(lpu)

# setuden/ElectricPowerForecast
def test_setsuden_electric_power_usage():
  def epu(rows):
    for f in pow.response_fields:
      print "%s\t%s" % (f , str(rows['ElectricPowerForecasts'][f]))
  # main
  pow = setsuden.ElectricPowerForecast()
  rows=pow.query(epu,[('date','20110712')])


# main
test_volunteers()
test_shinsai_archive_search()
test_shinsai_archive_area()
test_setsuden_latest_power_usage()
test_setsuden_electric_power_usage()
