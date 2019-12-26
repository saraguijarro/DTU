#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 14:57:19 2018

@author: sara
"""

import numpy as np

def dataStatistics(data,statistic):
    
# First of all, make sure that the lenght of data is different from 0:
    len(data) != 0

# Mean (average) Temperature : Addition of all temperatures, divided by the number of temperatures taken into account
    T = np.sum(data[:,0]) # returns the first column, and sums the values of that first column
    MeanTemperature = T / (len(data[:,0]))
    
# Mean (average) Growth rate : Addition of all growth rate values, divided by the number of growth rate values taken into account
    G = np.sum(data[:,1]) # returns the second colum, and sums the values of that second column
    MeanGrowthRate = G / (len(data[:,1]))
    
# Standard deviation of Temperature : 
    StdTemperature = np.std(data[:,0]) # returns the standard deviation, meaning the  square root of the average of the squared deviations from the mean temperature
    
# Standard deviation of Growth rate :
    StdGrowthRate = np.std(data[:,1]) # returns the standard deviation, meaning the  square root of the average of the squared deviations from the mean growth rate

# Rows : The total number of rows in the data
    Rows = len(data)
    
# Mean Cold Growth rate : Mean (average) Growth rate when Temperature is less than 20 degrees
    MeanColdGrowthRate = np.empty((0,3)) # creates an empty array with the correct dimentions
    for i in range (len(data)):
        if(data[i,0] < 20):
            MeanColdGrowthRate = np.append(MeanColdGrowthRate, [data[i]], 0) # add the rows in which the temperature is less than 20 degrees
    print(MeanColdGrowthRate)
    if len(MeanColdGrowthRate)>0:
        G = np.sum(MeanColdGrowthRate[:,1]) # returns the second colum, and sums the values of that second column
        MeanColdGrowthRate = G / (len(MeanColdGrowthRate[:,1]))
    else:
        MeanColdGrowthRate = None
            
# Mean Hot Growth rate : Mean (average) Growth rate when Temperature is greater than 50 degrees
    MeanHotGrowthRate = np.empty((0,3)) # creates an empty array with the correct dimentions
    for i in range (len(data)):
        if(data[i,0] > 50):
            MeanHotGrowthRate = np.append(MeanHotGrowthRate, [data[i]], 0) # add the rows in which the temperature is greater than 50 degrees
    print(MeanHotGrowthRate)
    if len(MeanHotGrowthRate)>0:
        G = np.sum(MeanHotGrowthRate[:,1]) # returns the second colum, and sums the values of that second column
        MeanHotGrowthRate = G / (len(MeanHotGrowthRate[:,1]))
    else:
        MeanHotGrowthRate = None

# Statistic : A string specifying the statistic that should be calculated
    if statistic=="Mean Temperature":
        return MeanTemperature
    elif statistic=="Mean Growth rate":
        return MeanGrowthRate
    elif statistic=="Std Temperature":
        return StdTemperature
    elif statistic=="Std Growth rate":
        return StdGrowthRate
    elif statistic=="Rows":
        return Rows
    elif statistic=="Mean Cold Growth rate":
        return MeanColdGrowthRate
    elif statistic=="Mean Hot Growth rate":
        return MeanHotGrowthRate
        
# Result : A scalar containing the calculated statistics
    result = np.asscalar(np.array([statistic]))
    return result