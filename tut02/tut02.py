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
    if mod*(i+1)<=len(list1):
        ws.cell(row=4+i,column=13).value=str(mod*i+1)+"-"+str(mod*(i+1))
    else:
        ws.cell(row=4+i,column=13).value=str(mod*i+1)+"-"+str(len(list1))
    ws.cell(row=4+i,column=14).value=cl[i].count(+1)
    ws.cell(row=4+i,column=15).value=cl[i].count(-1)
    ws.cell(row=4+i,column=16).value=cl[i].count(+2)
    ws.cell(row=4+i,column=17).value=cl[i].count(-2)
    ws.cell(row=4+i,column=18).value=cl[i].count(+3)
    ws.cell(row=4+i,column=19).value=cl[i].count(-3)
    ws.cell(row=4+i,column=20).value=cl[i].count(+4)
    ws.cell(row=4+i,column=21).value=cl[i].count(-4)

ws.cell(row=p+7,column=13).value="Overall Count Transition"
ws.cell(row=p+8,column=14).value="To"
ws.cell(row=p+10,column=12).value="From"
ws.cell(row=p+9,column=13).value="Count"
for i in range(0,8):
    ws.cell(row=p+9,column=14+i).value=list8[i]
    ws.cell(row=p+10+i,column=13).value=list8[i]
   
a1=b1=c1=d1=e1=f1=g1=h1=0
a2=b2=c2=d2=e2=f2=g2=h2=0
a3=b3=c3=d3=e3=f3=g3=h3=0
a4=b4=c4=d4=e4=f4=g4=h4=0
a5=b5=c5=d5=e5=f5=g5=h5=0
a6=b6=c6=d6=e6=f6=g6=h6=0
a7=b7=c7=d7=e7=f7=g7=h7=0
a8=b8=c8=d8=e8=f8=g8=h8=0

for i in range(0,len(list7)-1):
    if list7[i]==1:
        if list7[i+1]==1:
            a1+=1
        elif list7[i+1]==-1:
            b1+=1
        elif list7[i+1]==2:
            c1+=1
        elif list7[i+1]==-2:
            d1+=1
        elif list7[i+1]==3:
            e1+=1
        elif list7[i+1]==-3:
            f1+=1
        elif list7[i+1]==4:
            g1+=1
        elif list7[i+1]==-4:
            h1+=1
    if list7[i]==-1:
        if list7[i+1]==1:
            a2+=1
        elif list7[i+1]==-1:
            b2+=1
        elif list7[i+1]==2:
            c2+=1
        elif list7[i+1]==-2:
            d2+=1
        elif list7[i+1]==3:
            e2+=1
        elif list7[i+1]==-3:
            f2+=1
        elif list7[i+1]==4:
            g2+=1
        elif list7[i+1]==-4:
            h2+=1
    if list7[i]==2:
        if list7[i+1]==1:
            a3+=1
        elif list7[i+1]==-1:
            b3+=1
        elif list7[i+1]==2:
            c3+=1
        elif list7[i+1]==-2:
            d3+=1
        elif list7[i+1]==3:
            e3+=1
        elif list7[i+1]==-3:
            f3+=1
        elif list7[i+1]==4:
            g3+=1
        elif list7[i+1]==-4:
            h3+=1
    if list7[i]==-2:
        if list7[i+1]==1:
            a4+=1
        elif list7[i+1]==-1:
            b4+=1
        elif list7[i+1]==2:
            c4+=1
        elif list7[i+1]==-2:
            d4+=1
        elif list7[i+1]==3:
            e4+=1
        elif list7[i+1]==-3:
            f4+=1
        elif list7[i+1]==4:
            g4+=1
        elif list7[i+1]==-4:
            h4+=1
    if list7[i]==3:
        if list7[i+1]==1:
            a5+=1
        elif list7[i+1]==-1:
            b5+=1
        elif list7[i+1]==2:
            c5+=1
        elif list7[i+1]==-2:
            d5+=1
        elif list7[i+1]==3:
            e5+=1
        elif list7[i+1]==-3:
            f5+=1
        elif list7[i+1]==4:
            g5+=1
        elif list7[i+1]==-4:
            h5+=1
    if list7[i]==-3:
        if list7[i+1]==1:
            a6+=1
        elif list7[i+1]==-1:
            b6+=1
        elif list7[i+1]==2:
            c6+=1
        elif list7[i+1]==-2:
            d6+=1
        elif list7[i+1]==3:
            e6+=1
        elif list7[i+1]==-3:
            f6+=1
        elif list7[i+1]==4:
            g6+=1
        elif list7[i+1]==-4:
            h6+=1
    if list7[i]==4:
        if list7[i+1]==1:
            a7+=1
        elif list7[i+1]==-1:
            b7+=1
        elif list7[i+1]==2:
            c7+=1
        elif list7[i+1]==-2:
            d7+=1
        elif list7[i+1]==3:
            e7+=1
        elif list7[i+1]==-3:
            f7+=1
        elif list7[i+1]==4:
            g7+=1
        elif list7[i+1]==-4:
            h7+=1
    if list7[i]==-4:
        if list7[i+1]==1:
            a8+=1
        elif list7[i+1]==-1:
            b8+=1
        elif list7[i+1]==2:
            c8+=1
        elif list7[i+1]==-2:
            d8+=1
        elif list7[i+1]==3:
            e8+=1
        elif list7[i+1]==-3:
            f8+=1
        elif list7[i+1]==4:
            g8+=1
        elif list7[i+1]==-4:
            h8+=1    

A1=[a1,b1,c1,d1,e1,f1,g1,h1]
A2=[a2,b2,c2,d2,e2,f2,g2,h2]
A3=[a3,b3,c3,d3,e3,f3,g3,h3]
A4=[a4,b4,c4,d4,e4,f4,g4,h4]
A5=[a5,b5,c5,d5,e5,f5,g5,h5]
A6=[a6,b6,c6,d6,e6,f6,g6,h6]
A7=[a7,b7,c7,d7,e7,f7,g7,h7]
A8=[a8,b8,c8,d8,e8,f8,g8,h8]

for i in range(0,8):
    ws.cell(row=p+10,column=14+i).value=A1[i]
    ws.cell(row=p+11,column=14+i).value=A2[i]
    ws.cell(row=p+12,column=14+i).value=A3[i]
    ws.cell(row=p+13,column=14+i).value=A4[i]
    ws.cell(row=p+14,column=14+i).value=A5[i]
    ws.cell(row=p+15,column=14+i).value=A6[i]
    ws.cell(row=p+16,column=14+i).value=A7[i]
    ws.cell(row=p+17,column=14+i).value=A8[i]

for x in range(0,p):
    if x<p:
        ws.cell(row=p+21+13*x,column=13).value="Mod Transition Count"
        if mod*(x+1)<=len(list1):
            ws.cell(row=p+22+13*x,column=13).value=str(mod*x+1)+"-"+str(mod*(x+1))
        else:
            ws.cell(row=p+22+13*x,column=13).value=str(mod*x+1)+"-"+str(len(list1))
        ws.cell(row=p+22+13*x,column=14).value="To"
        ws.cell(row=p+24+13*x,column=12).value="From"
        ws.cell(row=p+23+13*x,column=13).value="Count"
        for i in range(0,8):
            ws.cell(row=p+23+13*x,column=14+i).value=list8[i]
            ws.cell(row=p+24+13*x+i,column=13).value=list8[i]

    


