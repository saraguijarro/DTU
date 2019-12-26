#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 17:59:58 2018

@author: sara
"""

import numpy as np
from dataLoad import dataLoad
from dataPlot1 import dataPlot1
from dataPlot2 import dataPlot2
from dataStatistics import dataStatistics

def menu():
    print("************MAIN MENU**************")

    choice = input("""
                      1: Load data
                      2: Filter data
                      3: Display statistics
                      4: Generate plots
                      5: Quit

                      Please enter your choice: """)

while True:
    try:
# Load data
        if choice == "1":
            filename=input("Please input the filename:") # ask the user for an input
            data=dataLoad(filename)
            break


# -------------------------------------------------
# Filter data
        elif choice == "2": 
            if data.size == 0:
                print("No data loaded") # Display a message if no data has been loaded, to draw the plots
            else:
                DataChoice = input("""
                      1: Bacteria type
                      2: Growth rate range
                      3: Temperature range
                      4: Exit

                      Please enter your choice: """)

            # Bacteria type filter
                if DataChoice == 1:
                    BacteriaType=input("""
                                       
                        1: Salmonella enterica
                        2: Bacillus cereus
                        3: Listeria
                        4: Brochothrix thermosphacta
                        
                        Please choose a Bacteria Type: """)

                #??????, We don't know how to modify the program to only take into account a certain type of bacteria
                
            # Growth rate range filter
                elif DataChoice == 2:
                    MaximumGrowthRate = float(input("Please input a maximum value for the growth rate: "))
                    MinimumGrowthRate = float(input("Please input a minimum value for the growth rate: "))
                    
                    if MaximumGrowthRate < MinimumGrowthRate:
                        print("The minimum value of the growth rate must be lower than the Maximum value of the growth rate")
                    else:
                        toRemove = np.array(np.where(((unfilteredData[:,1] > minimumGrowthRate) & (unfilteredData[:,1] < maximumGrowthRate)) == False))
                        filteredData = np.delete(data, toRemove, axis=0)
                        data = FilteredData
                        break
                        
            # Temperature range filter 
                elif DataChoice == 3:
                    MaximumTemperature = float(input("Please input a maximum value for the temperature: "))
                    MinimumTemperature = float(input("Please input a minimum value for the temperature: "))
                    
                    if MaximumTemperature < MinimumTemperature:
                        print("The minimum value of the temperature must be lower than the Maximum value of the temperature")
                    else:
                        toRemove = np.array(np.where(((unfilteredData[:,1] > minimumGrowthRate) & (unfilteredData[:,1] < maximumGrowthRate)) == False))
                        filteredData = np.delete(data, toRemove, axis=0)
                        data = FilteredData
                        break
                            
            #Exit
                elif DataChoice == 4:
                    break

# -------------------------------------------------
# Display statistics
        elif choice == "3":
            if data.size == 0:
                print("No data loaded") # Display a message if no data has been loaded, to draw the plots
            else:
                StatisticChoice = input("""
                      1: Mean Temperature
                      2: Mean Growth Rate
                      3: Standard deviation of Temperature
                      4: Standard deviation of Growth rate
                      5: Rows
                      6: Mean Cold Growth rate
                      7: Mean Hot Growth rate
                      8: Exit

                      Please enter your choice: """)

            # Mean Temperature
                if StatisticChoice == 1:
                    print(dataStatistics(data,"Mean Temperature"))
                
                # Mean Growth Rate
                elif StatisticChoice == 2:
                    print(dataStatistics(data,"Mean Growth Rate"))
            
            # Standard deviation of Temperature
                elif StatisticChoice == 3:
                    print(dataStatistics(data,"Standard deviation of Temperature"))
            
            # Standard deviation of Growth rate
                elif StatisticChoice == 4:
                    print(dataStatistics(data,"Standard deviation of Growth rate"))
            
            # Rows
                elif StatisticChoice == 5:
                    print(dataStatistics(data,"Rows"))
                
            # Mean Cold Growth rate
                elif StatisticChoice == 6:
                    print(dataStatistics(data,"Mean Cold Growth rate"))
        
            # Mean Hot Growth rate
                elif StatisticChoice == 7:
                    print(dataStatistics(data,"Mean Hot Growth rate"))
                
            # Exit
                elif StatisticChoice == 8:
                    break

# -------------------------------------------------
# Generate plots
        elif choice=="4":
            if data.size == 0:
                print("No data loaded") # Display a message if no data has been loaded, to draw the plots
            else:
                PlotChoice = input("""
                      1: Plot1 : Number of Bacteria
                      2: Plot2 : Bacteria Growth / Temperature
                      3: Exit

                      Please enter your choice: """)

            # Draw Plot 1
                if PlotChoice == 1:
                    print(dataPlot(data))
                
            # Draw Plot 2
                elif PlotChoice == 2:
                    print(dataPlot2(data))
            
            # Exit 
                elif PlotChoice == 3:
                    break

# -------------------------------------------------
# Quit
        elif choice=="5":
            break