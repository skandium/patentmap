# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 13:53:57 2016

@author: martin
"""
import pandas
#from geopy.geocoders import Nominatim
#from geopy.geocoders import GoogleV3
from geopy.geocoders import GeoNames

test = pandas.read_csv("citydbimpr5.csv")
#test['lons'] = [0]*len(test)
#test['lats'] = [0]*len(test)
#geolocator = Nominatim()
#geolocator = GoogleV3()
geolocator = GeoNames(username='skandium')
#geolocator = GoogleV3(api_key='AIzaSyAqGHy5SDEIET0iD_FRiQ5rThXkGiDJQFs')


items = list(range(0,len(test)))
#test['lons'] = [0]*len(items)
#test['lats'] = [0]*len(items)
#sum = 0
for i,j in enumerate(items):
    if (test.loc[i,'lons'] == 0 and test.loc[i,'lats'] == 0) or (pandas.isnull(test.loc[i,'lons']) == True and pandas.isnull(test.loc[i,'lats']) == True):
#        sum = sum + 1
        try:

            loca = geolocator.geocode(test['City'][i])
            test.loc[i,'lons'] = loca.longitude
            test.loc[i,'lats'] = loca.latitude
            print(i)
            #test['lons'][i] = loca.longitude
            #test['lats'][i] = loca.latitude
            #test.loc['lons'][i] = loca.longitude
            #test.loc['lats'][i] = loca.latitude
        except:
            print("fail"+str(i))
            pass

test.to_csv("citydbimpr6.csv")
