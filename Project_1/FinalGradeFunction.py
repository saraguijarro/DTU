#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:50:28 2018

@author: sara
"""

import numpy as np

def computeFinalGrades(grades):
    
# COMPUTEFINALGRADE According to the number of grades given and the grade itself, the program will either calculate the average to return the final grade, or return directly the grade as the final grade. 
# Computes the final grade based on preset conditions.
    #
    # Usage : gradesFinal = computeFinalGrades(grades)
    #
    # Input    grades           N x M matrix
    # Output   gradesFinal      Vector of length n
    #
    # Author: Sara Maria Guijarro-Heeb (s184484), 2018

# Check for the length of grades
    if len(grades) != 0:

        # Creating a matrix SimpleGrades for which we only take into account the grades (and not the other annotations from the grades -matrix)
        SimpleGrades = np.delete(grades, 0,0)
        SimpleGrades = np.delete(SimpleGrades, np.s_[:2], 1).astype(np.float)
        
        # Defining gradesFinal as a matrix with the same shape as grades (same number of dimension to be able to concatenate them later)
        # Later on, we will construct a matrix by using the different values found when the grades have fulfilled the conditions given
        # We set the first element to be the column title 'finalgrades'
        gradesFinal = np.empty_like(grades[:,0:1])
        gradesFinal[0][0] = 'finalgrades'
        
        # Computing the final grades, when the student has received the grade -3 at least once
        # Checking elements in the grades' matrix (if there is any grades equal to-3)
        # If there is any grade equal to -3, we replace the set of grades in the Final grade by the value -3
        for i in range (len(SimpleGrades[:,0])):
            if -3 in SimpleGrades[i,:]:
                gradesFinal[i+1][0] = -3

            else:
                    
        # Computing the final grades, when there is only one assignment
        # If there is only one grade per student, we consider the Final grade as that only grade given
                if len(SimpleGrades[i,:]) == 1:
                    gradesFinal[i+1][0] = SimpleGrades[i,:]
        
        # Computing the final grades, when there is more than one grade
        # If there is more than one grade per student, we firstly discard the lowest grade
        # And, in a second place compute the mean of those grades (without taking into account the lowest grade, of course)
        # Finally, we round the values computed previously, so that the Final grades respect the 7-step-scale logistic
                if len(SimpleGrades[i,:]) > 1:
                        GradesPerStudent1 = SimpleGrades[i,:]
                        GradesPerStudent2 = np.delete(GradesPerStudent1, np.argmin(GradesPerStudent1))
                        MeanGrades = np.mean(GradesPerStudent2)
                        StepScale = ([12,10,7,4,2,0,-3])
                        gradesFinal[i+1][0] = min(StepScale, key=lambda x:abs(x-MeanGrades))
        
        return gradesFinal


