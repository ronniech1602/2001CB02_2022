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

X=Y=Z=0 #DECLARING 3 VARIABLES FOR THE PURPOSE OF COUNTING WITH INITIAL VALUE 0

with open('octant_input.csv','r') as file:
    reader = csv.reader(file)
    for rows in reader:
        if (rows[1]!='U'): #TO SKIP THE HEADER ROW
            LIST1.insert(X,float(rows[1])-u_average) #TO INSERT THE VALUES OF DIFFERENCE (U-U_AVG) INTO LIST 1
            X+=1
        if (rows[2]!='V'):
            LIST2.insert(Y,float(rows[2])-v_average)
            Y+=1
        if (rows[3]!='W'):
            LIST3.insert(Z,float(rows[3])-w_average)
            Z+=1

#OVCOUNT REFERS TO OVERALL COUNT , 1 REFERS TO OCTANT '1' AND NEG1 REFERS  TO OCTANT '-1'
a=ovcount_1=ovcount_2=ovcount_3=ovcount_4=ovcount_neg1=ovcount_neg2=ovcount_neg3=ovcount_neg4=0

#WHILE LOOP FOR CALCULATING OVERALL COUNT THROUGH IF-ELSE STATEMENTS
while(a<len(LIST1)):
    if(LIST1[a]>0 and LIST2[a]>0):
        if(LIST3[a]>0):
            ovcount_1+=1
        else:
            ovcount_neg1+=1
    elif(LIST1[a]<0 and LIST2[a]>0):
        if(LIST3[a]>0):
            ovcount_2+=1
        else:
            ovcount_neg2+=1
    elif(LIST1[a]<0 and LIST2[a]<0):
        if(LIST3[a]>0):
            ovcount_3+=1
        else:
            ovcount_neg3+=1
    elif(LIST1[a]>0 and LIST2[a]<0):
        if(LIST3[a]>0):
            ovcount_4+=1
        else:
            ovcount_neg4+=1
    a+=1

#DEFINING THE MOD FUNCTION 
def mod_func(mod):
    mod_1=mod_2=mod_3=mod_4=mod_neg1=mod_neg2=mod_neg3=mod_neg4=0
    m=n=0
    p=mod
    #WHILE LOOP , THE NUMBER OF TIMES IT RUNS DEPENDS ON 'p'
    while(m<len(LIST1)/p):
        #NESTED WHILE LOOP TO COUNT THE OCTANT NUMBER
        while(n<mod):
            if(LIST1[n]>0 and LIST2[n]>0):
                if(LIST3[n]>0):
                    mod_1+=1
                else:
                    mod_neg1+=1
            elif(LIST1[n]<0 and LIST2[n]>0):
                if(LIST3[n]>0):
                    mod_2+=1
                else:
                    mod_neg2+=1
            elif(LIST1[n]<0 and LIST2[n]<0):
                if(LIST3[n]>0):
                    mod_3+=1
                else:
                    mod_neg3+=1
            elif(LIST1[n]>0 and LIST2[n]<0):
                if(LIST3[n]>0):
                    mod_4+=1
                else:
                    mod_neg4+=1
            n+=1
        mod+=p
        m+=1
        print(mod_1,mod_neg1,mod_2,mod_neg2,mod_3,mod_neg3,mod_4,mod_neg4)
    return

mod=int(input('input the mod value: ')) #INPUT FROM USER
mod_func(mod) #FUNCTION CALL
     
    