#made by Suzan
#imports pandas library which we are gona use later; 
import pandas as pd
import numpy as np

#we define function to load data as LoadData;
def LoadData(filename):
    #grade is the variable which stores all the data from the file which we enter as filename;
    #.values is the attribute that helps us to store data in the matrix structure e.g.rows*column in our case;
    
    grades=pd.read_csv(filename)
    columns = pd.DataFrame(np.array(grades.columns)).T
    
    return np.array(columns.append(pd.DataFrame(grades.values), ignore_index=True))
