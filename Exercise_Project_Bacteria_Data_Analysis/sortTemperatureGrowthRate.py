#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 19:21:36 2018

@author: sara
"""

def sortTemperatureGrowthRate(Temperature, GrowthRate):
    import numpy as np

    sortedTemperature=[]
    sortedGrowthrate=[]
    T1=[]
    dtype=[('temperature',int),('GRate',float)]



    for i in range (len(Temperature)):
        T1.append((Temperature[i],GrowthRate[i]))
        
    TemperatureGrowthrate1=np.array(T1, dtype=dtype)
    TemperatureGrowthrate1=np.sort(TemperatureGrowthrate1, order='temperature')

    for i in range (len(TemperatureGrowthrate1)):
        sortedTemperature.append(TemperatureGrowthrate1[i][0])
        sortedGrowthrate.append(TemperatureGrowthrate1[i][1])
    
    return(sortedTemperature,sortedGrowthrate)