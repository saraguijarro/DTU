#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 19:20:39 2018

@author: sara
"""

import csv
import numpy as np

def dataLoad(filename):
        
    
    
    #Initial variables
    data = [0,0,0]
    read = True
    
    #Append each row to dataRaw
    with open(filename, newline='') as inputfile:
        for line,row in enumerate(csv.reader(inputfile)):
            
            arr = np.array(row[0].split(" "), dtype=float) #Creating an array of row
            #Only read line if len is three 
            if len(arr) == 3:                
                #Checking for error conditions
                if ((10 >= arr[0]) or (arr[0] >= 60)): #We check if Temperature is in the right range
                    read = False #Do not read line
                    print("Problem with line:",line+1,"Temperature is not between 10 and 60")
                    
                if (arr[1]<0): #We check if Growth rate is positive
                    read = False #Do not read line
                    print("Problem with line:",line+1,"Growth rate is negative")
                
                
                if ((0 >= arr[2]) or (arr[2] > 4)): #We check if the Bacteria type is 1,2,3 or 4
                    read = False #Do not read line
                    print("Problem with line:",line+1,"Bacteria type is not 1,2,3 or 4")
                
                if read:
                    data = np.vstack((data,arr)) #Stack row into N x 3 matrix
                
                read = True #reset read
                
            else:
                print("Problem with line:",line+1,"Length of row was not 3")
                
    data = data[1:len(data)] #Remove placeholder of [0,0,0]

    return data