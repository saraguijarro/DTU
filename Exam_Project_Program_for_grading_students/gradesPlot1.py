# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:57:21 2018

@author: Miguel
"""
#made by Miguel (s184468)
#GRADESPLOT: Creates 2 plots based on the grades in the "grades" matrix
#The Plot:“Final grades” is a bar plot of the number of students who have received each of possible final grades on the 7-step-scale

#input argument: "grades": An N×M matrix containing grades on the 7-step-scale given to N students on M different assignments.
#screen output: the plots described above


import numpy as np
import matplotlib.pyplot as plt
from FinalGradeFunction import computeFinalGrades

def gradesPlot1(grades):
    
    Simplegrades=np.delete(computeFinalGrades(grades), 0,0).astype(np.float) 
    
    finalGrades = Simplegrades.flatten().tolist() #now we get the "finalGrades" vector
    print(finalGrades)
    xlabels=np.array([-3,0,2,4,7,10,12]) #these are gonna be the only values that appear on the x-axis
                                         #I will use "plt.xticks" to define them
    
    #here I define the number of students that got each grade
    twelve=finalGrades.count(12)
    ten=finalGrades.count(10)
    seven=finalGrades.count(7)
    four=finalGrades.count(4)
    two=finalGrades.count(2)
    zero=finalGrades.count(0)
    mthree=finalGrades.count(-3)
    
    #then I plot each value bar
    plt.bar(-3,mthree,color='blue')
    plt.bar(0,zero,color='blue')
    plt.bar(2,two,color='blue')
    plt.bar(4,four,color='blue')
    plt.bar(7,seven,color='blue')
    plt.bar(10,ten,color='blue')
    plt.bar(12,twelve,color='blue')
    
    #finally I just give names to the axises, to the plot and make sure that only the possible values appear on the x-axis
    plt.xlabel('Grades')
    plt.ylabel('Number of students')
    plt.title("FINAL GRADES")
    plt.xticks(xlabels, xlabels)
    plt.show()
     
    
