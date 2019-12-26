#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 19:33:52 2018

@author: sara
"""

import matplotlib.pyplot as plt
import numpy as np
from sortTemperatureGrowthRate import sortTemperatureGrowthRate



def dataPlot(data):
#PLOT1: “Number of bacteria”
    
    #We take the 3rd column of the data matrix, and convert it to a list in order to use .count(), this counts how many times a certain element appears in a list
    #Then we know how many times each bacteria is used
    numberSalmonellaenterica=np.ndarray.tolist(data[:,2]).count(1)
    numberBacilluscereus=np.ndarray.tolist(data[:,2]).count(2)
    numberListeria=np.ndarray.tolist(data[:,2]).count(3)
    numberBrochothrixthermosphacta=np.ndarray.tolist(data[:,2]).count(4)
    
    #We plot 4 bars with different colors, each represents the amount of times a certain bacteria is used
    plt.bar(1,numberSalmonellaenterica)
    plt.bar(2,numberBacilluscereus)
    plt.bar(3,numberListeria)
    plt.bar(4,numberBrochothrixthermosphacta)

    #This is some basic information about the plot
    plt.title('Number of Bacteria per type')
    plt.xlabel('Type of Bacteria')
    plt.ylabel('Number of Bacteria')

    #this is the Legend Data - We use color patches to represent the bars, and give the name of the bacteria
    blue_patch = mpatches.Patch(color='blue', label='Salmonella enterica')
    orange_patch = mpatches.Patch(color='orange', label='Bacillus cereus')
    green_patch = mpatches.Patch(color='green', label='Listeria')
    red_patch = mpatches.Patch(color='red', label='Brochothrix thermosphacta')
    plt.legend(handles=[blue_patch,orange_patch,green_patch,red_patch])
    
    
        