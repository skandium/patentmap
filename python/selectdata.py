# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 20:39:41 2016

@author: martin
"""
#This is for extracting data 1976-2001

#years = [1976]
years = list(range(1976,2002))

import os
os.chdir("C:\\Users\\martin\\Desktop\\patents")

for i in years:
    dat=open(str(i)+'.dat').readlines()
    testime=open(str(i)+'.dat','r')
    data = [""] * len(dat)
    for n,line in enumerate(testime):
        if line.startswith("CTY"):
            newstr = line + next(testime)     
            newstr = newstr.replace("\n","")
            newstr = newstr.replace("  ","")
            newstr = newstr.replace("CTY","")
            newstr = newstr.replace("STA",", ")
            newstr = newstr.replace("CNT",",")
            newstr = newstr.replace("both of","")
            newstr = newstr.replace("BOTH OF","")
            newstr = newstr.strip()        
            data[n] = "\n"+newstr
        
    file = open("C:\\Users\\martin\\Desktop\\portfolio\\"+str(i)+".txt","w")
    file.write("".join(data))
    file.close()