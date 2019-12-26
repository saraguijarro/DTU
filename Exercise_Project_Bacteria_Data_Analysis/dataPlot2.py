#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 19:32:58 2018

@author: sara
"""

import matplotlib.pyplot as plt
import numpy as np
from sortTemperatureGrowthRate import sortTemperatureGrowthRate



def dataPlot2(data):



#PLOT2:  “Growth rate by temperature”
    #first we define empty arrays that will be used later as storage arrays to separate data from each type of bacteria
    Temperature1=np.array([])
    Temperature2=np.array([])
    Temperature3=np.array([])
    Temperature4=np.array([])
    #we will store the Temperature values in 4 arrays, 1 per bacteria type.
    #the loop is used to check every value and store it in the right array
    for i in range (len(data[:,0])):
        if data[i,2]==1:
            Temperature1=np.append(Temperature1,np.array([data[i,0]]))
        elif data[i,2]==2:
            Temperature2=np.append(Temperature2,np.array([data[i,0]]))
        elif data[i,2]==3:
            Temperature3=np.append(Temperature3,np.array([data[i,0]]))
        elif data[i,2]==4:
            Temperature4=np.append(Temperature4,np.array([data[i,0]]))
    #once again we define empty arrays for the same reason
    GRate1=([])
    GRate2=([])
    GRate3=([])
    GRate4=([])
    #we will store the GrowthRate values in 4 arrays, 1 per bacteria type.
    #the loop is used to check every value and store it in the right array
    for i in range(len(data[:,1])):
        if data[i,2]==1:
            GRate1=np.append(GRate1,np.array([data[i,1]]))
        elif data[i,2]==2:
            GRate2=np.append(GRate2,np.array([data[i,1]]))
        elif data[i,2]==3:
            GRate3=np.append(GRate3,np.array([data[i,1]]))
        elif data[i,2]==4:
            GRate4=np.append(GRate4,np.array([data[i,1]]))
            
    #Now we plot lines that show the variation of GrowthRate through the evolution of Temperature for each bacteria
    #for the x and y axis we will use the function "sortTemperatureGrowthRate" to ensure that the data is used in the right order
    #inputs: 2 arrays (Temperature and Growthrate, where which value of the first corresponds to the value in the second)
    #output: 2 arrays (sortedTemperature and sortedGrowthrate), the first array is the Temperature values, sorted from lowest to highest and the second array 
    #this function is used to ensure that the x axis is in the right order and so we plot from the lowest until the highest temperature
    #that way, the lines will go from the left to the right, and not back and forth
    plt.plot((sortTemperatureGrowthRate(Temperature1,GRate1)[0]),(sortTemperatureGrowthRate(Temperature1,GRate1)[1]),color='green')
    plt.plot((sortTemperatureGrowthRate(Temperature2,GRate2)[0]),(sortTemperatureGrowthRate(Temperature2,GRate2)[1]), color='orange')
    plt.plot((sortTemperatureGrowthRate(Temperature3,GRate3)[0]),(sortTemperatureGrowthRate(Temperature3,GRate3)[1]), color='red')
    plt.plot((sortTemperatureGrowthRate(Temperature4,GRate4)[0]),(sortTemperatureGrowthRate(Temperature4,GRate4)[1]), color='yellow')
    plt.xlabel('Temperature') #we name the axis
    plt.ylabel('Growth Rate')
    plt.title('Graph for bacteria growth with Temperature') #and give a title to the plot
    plt.show()