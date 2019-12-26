#made by Suzan
#imports librarires for performing several commands in it;
import numpy as np
#defines the data that should be rounded,here it's grades;
def roundGrade(grades):
    #sc is the seven step scale in which the data should be rounded to;
    ss=([12,10,7,4,2,0,-3])
    rounded=np.zeros(len(grades))
    #performs the operation using for loop for each grades and stores each value in the array called rounded;
    for i in range(len(grades)):
      
        rounded[i]= min(ss,key=lambda x:abs(x-grades[i]))#for i element in grades the temporary function lambda finds the absolute value of diff. betweenseven scale and grades i;
    return rounded
        

