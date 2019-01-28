#made by Miguel, Sara and Suzan

# Import libraries
import numpy as np

import pandas as pd
pd.options.display.max_columns = 999
pd.options.display.max_rows = 999
#we ensure that the table in "display final grades" shows all the values

import displayMenu as m
from LoadData import LoadData
from gradesPlot1 import gradesPlot1
from gradesPlot2 import gradesPlot2
from FinalGradeFunction import computeFinalGrades


# Define menu items
menuItems = np.array(["Load data", "Error Handling", "Generate plots","Display list of grades", "Quit"])
# Define all unfiltered data as an array
grades = np.array([])
# Start
while True:
    # Display menu options and ask user to choose a menu item
    choice = m.displayMenu(menuItems)
    # ------------------------------------------------------------------
     #Made by Suzan
    # 1. Load data
    if choice == 1: 
       
        while True:
            try:
                filename = input("Please input the filename: ")
                # Asking the user for an input
                grades = LoadData(filename)
                # Loading data if filename is correct
                print("Data succesfully loaded")
                break
            except OSError:
                # Printing error message if file is not in the folder
                print("File not found, please try again with a valid filename")
                break
                
        
    # ------------------------------------------------------------------
    #made by Suzan 
    # 2. Check for Data Errors
    elif choice == 2:
        # Display error message if no data was loaded earlier
        if grades.size == 0:
            print("No data loaded")
        else:
            # Defining filter menu items
            errorchoice = m.displayMenu(np.array(["Student ID", "Grades","Quit"]))
            # Checking errors in Student IDs
            if errorchoice == 1:
                grade=grades
                    
                StudentId=np.array(grade[:,0])
                names=np.sort(StudentId)
                for i in range (len(names)):
                    if names[i]==names[i-1]:
                        print('Error studentid of',names[i] ,'is repeated, kindly requested to correct it')
                    
                        
            # Checking errors in the grades    
            elif errorchoice == 2:
                grade=grades
                ss=np.array([12,10,7,4,2,0,-3])
                for j in range (len(grade[0,:])-2):
                    for i in range (len(grade[:,0])):
                            
                        if (grades[i,j+2]) not in (ss):
                            print('Error grade',grade[i,j+2] ,', for',grade[i,0],' is not standard') 
                            
    
                        
                    # Clearing filter by setting the filtered data back to unfiltered data
            elif errorchoice == 3:
                    break
   # ------------------------------------------------------------------
   #made by Miguel  
   # 3. Generate plots
    elif choice == 3:
       # Display error message if no data was loaded earlier
       if grades.size == 0:
            print("No data loaded")
       # Displaying plots
       else:
           print("Which plot do you want to display?")
           
           plotchoice = m.displayMenu(np.array(["Final Grades", "Grades per Assignment","Both","Cancel"]))
           if plotchoice == 1:
               print(gradesPlot1(grades))
              
           elif plotchoice == 2:
               print(gradesPlot2(grades))
           elif plotchoice == 3:
               print(gradesPlot1(grades))
               print(gradesPlot2(grades))
           elif plotchoice == 4:
            break
           
           
         
         
         
    # ------------------------------------------------------------------
     #Made by Sara
    # 4. Display list of grades, done by s184484 (Sara Maria Guijarro Heeb)
    elif choice == 4:
        # Display error message if no data was loaded earlier
        if grades.size == 0:
            print("No data loaded")
        # Display list of grades    
        else:
            gradesFinal = computeFinalGrades(grades)
            # Concatenate grades and gradesFinal in gradesList, and then store all grades with column names in a pandas element
            # Finally sort all lines by the name of the students
            gradesList = np.concatenate((grades,gradesFinal), 1)
            gradesList = pd.DataFrame(gradesList[1:,:], columns=gradesList[0,:])
            gradesList = gradesList.sort_values(by='Name')
            print(gradesList)
    
    # ------------------------------------------------------------------
     # 5. Quit
    elif choice == 5:
        # End
        break
    
