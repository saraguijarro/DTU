#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 22:37:38 2018

@author: sara
"""
import numpy as np
import pandas as pd
from FinalGradeFunction import computeFinalGrades

def displayGrades(grades):
    
    gradesFinal = computeFinalGrades(grades)
    
    # Concatenate grades and gradesFinal in gradesList, and then store all grades with column names in a pandas element
    # Finally sort all lines by the name of the students
    gradesList = np.concatenate((grades,gradesFinal), 1)
    gradesList = pd.DataFrame(gradesList[1:,:], columns=gradesList[0,:])
    gradesList = gradesList.sort_values(by='Name')

    return gradesList

print(computeFinalGrades(np.array([['StudentID','Name','Assignment1','Assignent2','Assignement3'],['s12','Michael',7,12,2],['s13','Jo',4,-3,0],['s56','Ila',2,12,12],['s34','Susi',4,10,7]])))
