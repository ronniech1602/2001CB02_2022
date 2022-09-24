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

