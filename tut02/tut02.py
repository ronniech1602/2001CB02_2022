from openpyxl import load_workbook
import pandas as pd
import numpy as np

wb=load_workbook(r"C:\Users\Acer\Documents\GitHub\CS384_2022\tut02\input_octant_transition_identify.xlsx")
df=pd.read_excel(r"C:\Users\Acer\Documents\GitHub\CS384_2022\tut02\input_octant_transition_identify.xlsx")
ws=wb.worksheets[0]

list1=df.U
list2=df.V
list3=df.W

totalu=0
for x in range(0,len(list1)):
    totalu=totalu+list1[x]

Uavg=totalu/len(list1)

totalv=0
for x in range(0,len(list2)):
    totalv=totalv+list2[x]

Vavg=totalv/len(list2)

totalw=0
for x in range(0,len(list3)):
    totalw=totalw+list3[x]
    
Wavg=totalw/len(list3)

Ua=["Uavg",Uavg]
Va=["Vavg",Vavg]
Wa=["Wavg",Wavg]
for i in range(1,3):
    ws.cell(row=i,column=5).value=Ua[i-1]

for i in range(1,3):
    ws.cell(row=i,column=6).value=Va[i-1]
    
for i in range(1,3):
    ws.cell(row=i,column=7).value=Wa[i-1]

list4=[]
for i in list1:
    tmp=i-Uavg
    list4.append(tmp)
    
ws.cell(row=1,column=8).value="U'"
for i in range(2,len(list4)+2):
    ws.cell(row=i,column=8).value=list4[i-2]
    
list5=[]
for i in list2:
    tmp=i-Vavg
    list5.append(tmp)
    
ws.cell(row=1,column=9).value="V'"
for i in range(2,len(list5)+2):
    ws.cell(row=i,column=9).value=list5[i-2]
    
list6=[]
for i in list3:
    tmp=i-Wavg
    list6.append(tmp)
    
ws.cell(row=1,column=10).value="W'"
for i in range(2,len(list6)+2):
    ws.cell(row=i,column=10).value=list6[i-2]
    
ws.cell(row=1,column=11).value="Octants"
list7=[]
for i in range (0,len(list1)):
    if list4[i]>0 and list5[i]>0:
        if list6[i]>0:
            list7.append(+1)
        else:
            list7.append(-1)
        
    if list4[i]>0 and list5[i]<0:
        if list6[i]>0:
            list7.append(+4)
        else:
            list7.append(-4)
        
    if list4[i]<0 and list5[i]>0:
        if list6[i]>0:
            list7.append(+2)
        else:
            list7.append(-2)
        
    if list4[i]<0 and list5[i]<0:
        if list6[i]>0:
            list7.append(+3)
        else:
            list7.append(-3)
        

for i in range(2,len(list7)+2):
    ws.cell(row=i,column=11).value=list7[i-2]
    
ws.cell(row=2,column=13).value="Overall Count"
ws.cell(row=3,column=12).value="User Input"
list8=[+1,-1,+2,-2,+3,-3,+4,-4]
for i in range(0,8):
    ws.cell(row=1,column=i+14).value=list8[i]
   
ws.cell(row=2,column=14).value=list7.count(+1)
ws.cell(row=2,column=15).value=list7.count(-1)
ws.cell(row=2,column=16).value=list7.count(+2)
ws.cell(row=2,column=17).value=list7.count(-2)
ws.cell(row=2,column=18).value=list7.count(+3)
ws.cell(row=2,column=19).value=list7.count(-3)
ws.cell(row=2,column=20).value=list7.count(+4)
ws.cell(row=2,column=21).value=list7.count(-4)

mod=5000
ws.cell(row=3,column=13).value="Mod"+str(mod)

mod_ranges=[]
p=(len(list1)//mod)+1
cl=[]
for i in range(0,p):
    l=[]
    cl.append(l)

a=0

for y in range(0,p):
    for x in range(a,a+mod):
        if x<=len(list1)-1:
            cl[y].append(list7[x])
    a=a+mod

for i in range(0,p): 
    ws.cell(row=4+i,column=13).value=str(mod*i+1)+"-"+str(mod*(i+1))
    ws.cell(row=4+i,column=14).value=cl[i].count(+1)
    ws.cell(row=4+i,column=15).value=cl[i].count(-1)
    ws.cell(row=4+i,column=16).value=cl[i].count(+2)
    ws.cell(row=4+i,column=17).value=cl[i].count(-2)
    ws.cell(row=4+i,column=18).value=cl[i].count(+3)
    ws.cell(row=4+i,column=19).value=cl[i].count(-3)
    ws.cell(row=4+i,column=20).value=cl[i].count(+4)
    ws.cell(row=4+i,column=21).value=cl[i].count(-4)

    

    


