# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 14:39:34 2018

@author: Miguel
"""
#made by Miguel (s184468)
#GRADESPLOT: Creates a plot based on the grades in the "grades" matrix
#The Plot:“Grades per assignment”: is a plot with the assignments on the x-axis and the grades on the y-axis, in addition to that, there is a line representing the average grade for each assignment

#input argument: "grades": An N×M matrix containing grades on the 7-step-scale given to N students on M different assignments.
#screen output: the plot described above

import numpy as np
import matplotlib.pyplot as plt

def gradesPlot2(grades):
    
    #"Simplegrades" is the "grades" matrix without the text columns and rows, so we only have the values we need
    Simplegrades=np.delete(grades, 0,0)
    Simplegrades=np.delete(Simplegrades, 0,1)
    Simplegrades=np.delete(Simplegrades, 0,1).astype(np.float) 
#Plot 2:
    
    #FIRST: Let's define all tool arrays we will be using:
    add=np.random.uniform(low=-0.1,high=0.1,size=len(Simplegrades[:,0])) 
    #The "add" vector has random values between -0.1 and 0.1. Its purpose is to ensure that we can distinguish 2 different points, whenever 2 students get the same grade for the same assignment
    #We will add one of its values to each x and y value of our plot
    x=np.arange(1,len(Simplegrades[0,:])+1) 
    #"x" are our x-values used in the dot plots
    y=np.array([-3,0,2,4,7,10,12])
    #"y" is an array with all the possible y-values, we use it latter with "yticks" to show only the interesting values on the left side of the plot
    average=np.array([])
    #"average" will be the y-values in the "average line" plot
    xnames=np.array([]) 
    #"xnames" are the names given in the x-axis (Assignment 1,2,...)
    
    
    
    for i in range(len(x)):
        xnames=np.append(xnames, "Assignment {}".format(i+1))
    
    
    
    #we use a "for" loop to plot each column of our "grade matrix" in the form of dots
    #here the "add" vector is used to add an insignificant value to each number, so that 2 points with supposedly identical position, don't fully overstep each other
    #the y-values are all the grades obtained by students for each assignment
    for i in range(len(Simplegrades[:,0])):
        plt.scatter(x+add[i], Simplegrades[i,:]+add[i], s=25)
    #I've set the size of the points a bit smaller than default to make sure we can see the difference between two identical values
    
    #Then we just add a legend to know which student is which color
    names=np.delete(grades[:,1],0)
    plt.legend(names,loc='upper right', bbox_to_anchor=(1.38, 1.02, 0., 0.))
    #the location of the legend is set to be next to the plot, on the top right 
        
    
    #We use a for loop to append the average of each column to the "average" vector
    for i in range(len(Simplegrades[0,:])):
        average=np.append(average, np.mean(Simplegrades[:,i]))
    #Then we simply plot the average line using the same x-values
    plt.plot(x,average)
    
    
    
        
    
    
    
    #Finally we choose the title, the name of the axises and the limit values for y
    plt.title("GRADES PER ASSIGNMENT")
    plt.ylabel("Grades")
    plt.ylim(-3.5,12.5)
    plt.xlabel("Assignments")
    plt.xticks(x, xnames)
    plt.yticks (y,y)
    plt.show()
    