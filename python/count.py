# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 18:06:28 2016

@author: martin
"""
years = list(range(1976,2016))

import os
import pandas as pd
os.chdir("C:\\Users\\martin\\Desktop\\portfolio")

for i in years:
    uus=open(str(i)+'.txt').readlines()

    a = list(set(uus))

    count = [0] * len(a)

    for j,line in enumerate(a):
        count[j] = uus.count(a[j])

    intermed = pd.DataFrame(count)
    result = intermed[intermed[0]>100].sort_values([0])
    result.columns = ['Count']

    locations = [0] * len(result)
    for z,line in enumerate(list(result.index)):
        locations[z] = a[line].replace("\n","")
    
    result['City'] = locations

    result.to_csv(str(i)+".csv")