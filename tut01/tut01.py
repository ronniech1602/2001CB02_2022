import os
import csv
os.system("cls")

#CREATING 3 EMPTY LISTS TO STORE VALUES OF U',V',W'
LIST1=[]
LIST2=[]
LIST3=[]

#OPENING THE OCTANT_INPUT.CSV FILE IN READ MODE 
with open('octant_input.csv','r') as file:
    reader = csv.reader(file)
    
    #DEFINING SUMMATION VARIABLES WITH INITIAL VALUES OF 0 
    U_SUMMATION=0
    V_SUMMATION=0
    W_SUMMATION=0

    #CALCULATING SUMMATION OF U,V AND W VALUES 
    for row in reader:
        if (row[1]!='U'): #TO SKIP THE HEADER ROW
            U_SUMMATION+=float(row[1]) #ADDING THE FLOAT VALUE OF ROW ELEMENTS AT INDEX POSITION 1 UNTIL THE ROWS END
        if (row[2]!='V'): 
            V_SUMMATION+=float(row[2]) 
        if (row[3]!='W'): 
            W_SUMMATION+=float(row[3]) 

n=29745 #NUMBER OF ROWS EXCEPT HEADER

#CALCULATION OF AVERAGES
u_average=U_SUMMATION/n
v_average=V_SUMMATION/n
w_average=W_SUMMATION/n