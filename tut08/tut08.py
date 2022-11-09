from datetime import datetime
start_time = datetime.now()

import csv

f = open("pak_inns1.txt","r",newline='') 
file = csv.DictReader(f,fieldnames=["from-to","runs"],restkey="alpha")

from_to=[]
data=[]
datax=[]
for col in file:
    from_to.append(col["from-to"])
    data.append(col["runs"])

for i in data:
    x=i.split(" ",maxsplit=1)
    datax.append(x[1])

pak_team={'Babar Azam(c)':'Babar Azam', 'Mohammad Rizwan(w)':'Rizwan', 'Fakhar Zaman':'Fakhar Zaman', 'Iftikhar Ahmed':'Iftikhar Ahmed', 'Khushdil Shah':'Khushdil', 'Asif Ali':'Asif Ali', 'Shadab Khan':'Shadab Khan', 'Mohammad Nawaz':'Mohammad Nawaz', 'Naseem Shah':'Naseem Shah', 'Haris Rauf':'Haris Rauf', 'Shahnawaz Dahani':'Dahani'}
ind_team={'Rohit Sharma(c)':'Rohit', 'KL Rahul':'Rahul', 'Virat Kohli':'Kohli', 'Suryakumar Yadav':'Suryakumar Yadav', 'Dinesh Karthik(w)':'Karthik', 'Hardik Pandya':'Hardik Pandya', 'Ravindra Jadeja':'Jadeja', 'Bhuvneshwar Kumar':'Bhuvneshwar', 'Avesh Khan':'Avesh Khan', 'Yuzvendra Chahal':'Chahal', 'Arshdeep Singh':'Arshdeep Singh'}
pak=[]
ind=[]
overs=[]
tmp=[]
for i in from_to:
    a=i.split(" to ")
    tmp.append(a[0])
    pak.append(a[1])
    
for i in tmp:
    b=i.split(" ",maxsplit=1)
    overs.append(b[0])
    ind.append(b[1])
    
pak_s=set(pak)
pak_s=list(pak_s)
ind_s=set(ind)
ind_s=list(ind_s)

runf=[]
runs=[]
for i in datax:
    c=i.split(" ",maxsplit=2)
    if len(c)==1:
        runf.append(c[0])
        runs.append(" ")
    if len(c)>1:
        runf.append(c[0])
        runs.append(c[1])
    
c=[]
for i in pak_team.keys():
    c_0=0
    c_1=0
    c_2=0
    c_3=0
    c_4=0
    c_5=0
    c_6=0
    c_wic=0
    c_wide=0
    c_bye=0
    c_lb=0
    c_nb=0
    for j in range(0,len(overs)):
        if pak[j]==pak_team[i]:
            if runf[j]=="no":
                if runs[j]=="ball":
                    c_nb+=1
                if runs[j]=="run":
                    c_0+=1
            if runf[j]=="1":
                if runs[j]=="run":
                    c_1+=1
            if runf[j]=="2":
                if runs[j]=="runs":
                    c_2+=1
            if runf[j]=="3":
                if runs[j]=="runs":
                    c_3+=1
            if runf[j]=="5":
                if runs[j]=="runs":
                    c_5+=1
            if runf[j]=="FOUR":
                c_4+=1
            if runf[j]=="SIX":
                c_6+=1
            if runf[j]=="out":
                c_wic+=1
            if runf[j]=="wide":
                c_wide+=1
            if runs[j]=="wides":
                c_wide+=int(runf[j])
            if runs[j]=="byes":
                try:
                    c_bye+=int(runf[j])
                except:
                    pass
            if runs[j]=="legbyes" or runs[j]=="legbye":
                try:
                    c_lb+=int(runf[j])
                except:
                    pass
    d=[c_0,c_1,c_2,c_3,c_4,c_5,c_6,c_wic,c_wide,c_bye,c_lb,c_nb]
    c.append(d)

cc=[]
for i in ind_team.keys():
    c_0=0
    c_1=0
    c_2=0
    c_3=0
    c_4=0
    c_5=0
    c_6=0
    c_wic=0
    c_wide=0
    c_bye=0
    c_lb=0
    c_nb=0
    for j in range(0,len(overs)):
        if ind[j]==ind_team[i]:
            if runf[j]=="no":
                if runs[j]=="ball":
                    c_nb+=1
                if runs[j]=="run":
                    c_0+=1
            if runf[j]=="1":
                if runs[j]=="run":
                    c_1+=1
            if runf[j]=="2":
                if runs[j]=="runs":
                    c_2+=1
            if runf[j]=="3":
                if runs[j]=="runs":
                    c_3+=1
            if runf[j]=="5":
                if runs[j]=="runs":
                    c_5+=1
            if runf[j]=="FOUR":
                c_4+=1
            if runf[j]=="SIX":
                c_6+=1
            if runf[j]=="out":
                c_wic+=1
            if runf[j]=="wide":
                c_wide+=1
            if runs[j]=="wides":
                c_wide+=int(runf[j])
            if runs[j]=="byes":
                try:
                    c_bye+=int(runf[j])
                except:
                    pass
            if runs[j]=="legbyes" or runs[j]=="legbye":
                try:
                    c_lb+=int(runf[j])
                except:
                    pass
    d=[c_0,c_1,c_2,c_3,c_4,c_5,c_6,c_wic,c_wide,c_bye,c_lb,c_nb]
    cc.append(d)
    
f2 = open("india_inns2.txt","r",newline='') 
file2 = csv.DictReader(f2,fieldnames=["from-to","runs"],restkey="alpha")

from_to2=[]
data2=[]
datax2=[]
for col in file2:
    from_to2.append(col["from-to"])
    data2.append(col["runs"])

for i in data2:
    x=i.split(" ",maxsplit=1)
    datax2.append(x[1])
    
ind2=[]
pak2=[]
tmp2=[] 
for i in from_to2:
    a=i.split(" to ")
    tmp2.append(a[0])
    ind2.append(a[1])
    
for i in tmp2:
    b=i.split(" ",maxsplit=1)
    pak2.append(b[1])
    
runf2=[]
runs2=[]
for i in datax2:
    c=i.split(" ",maxsplit=2)
    if len(c)==1:
        runf2.append(c[0])
        runs2.append(" ")
    if len(c)>1:
        runf2.append(c[0])
        runs2.append(c[1])
        
c2=[]
for i in ind_team.keys():
    c_0=0
    c_1=0
    c_2=0
    c_3=0
    c_4=0
    c_5=0
    c_6=0
    c_wic=0
    c_wide=0
    c_bye=0
    c_lb=0
    c_nb=0
    for j in range(0,len(overs)):
        if ind2[j]==ind_team[i]:
            if runf2[j]=="no":
                if runs2[j]=="ball":
                    c_nb+=1
                if runs2[j]=="run":
                    c_0+=1
            if runf2[j]=="1":
                if runs2[j]=="run":
                    c_1+=1
            if runf2[j]=="2":
                if runs2[j]=="runs":
                    c_2+=1
            if runf2[j]=="3":
                if runs2[j]=="runs":
                    c_3+=1
            if runf2[j]=="5":
                if runs2[j]=="runs":
                    c_5+=1
            if runf2[j]=="FOUR":
                c_4+=1
            if runf2[j]=="SIX":
                c_6+=1
            if runf2[j]=="out":
                c_wic+=1
            if runf2[j]=="wide":
                c_wide+=1
            if runs2[j]=="wides":
                c_wide+=int(runf2[j])
            if runs2[j]=="byes":
                try:
                    c_bye+=int(runf2[j])
                except:
                    pass
            if runs2[j]=="legbyes" or runs2[j]=="legbye":
                try:
                    c_lb+=int(runf2[j])
                except:
                    pass
    d2=[c_0,c_1,c_2,c_3,c_4,c_5,c_6,c_wic,c_wide,c_bye,c_lb,c_nb]
    c2.append(d2)

cc2=[]
for i in pak_team.keys():
    c_0=0
    c_1=0
    c_2=0
    c_3=0
    c_4=0
    c_5=0
    c_6=0
    c_wic=0
    c_wide=0
    c_bye=0
    c_lb=0
    c_nb=0
    for j in range(0,len(overs)):
        if pak2[j]==pak_team[i]:
            if runf2[j]=="no":
                if runs2[j]=="ball":
                    c_nb+=1
                if runs2[j]=="run":
                    c_0+=1
            if runf2[j]=="1":
                if runs2[j]=="run":
                    c_1+=1
            if runf2[j]=="2":
                if runs2[j]=="runs":
                    c_2+=1
            if runf2[j]=="3":
                if runs2[j]=="runs":
                    c_3+=1
            if runf2[j]=="5":
                if runs2[j]=="runs":
                    c_5+=1
            if runf2[j]=="FOUR":
                c_4+=1
            if runf2[j]=="SIX":
                c_6+=1
            if runf2[j]=="out":
                c_wic+=1
            if runf2[j]=="wide":
                c_wide+=1
            if runs2[j]=="wides":
                c_wide+=int(runf2[j])
            if runs2[j]=="byes":
                try:
                    c_bye+=int(runf2[j])
                except:
                    pass
            if runs2[j]=="legbyes" or runs2[j]=="legbye":
                try:
                    c_lb+=int(runf2[j])
                except:
                    pass
    d2=[c_0,c_1,c_2,c_3,c_4,c_5,c_6,c_wic,c_wide,c_bye,c_lb,c_nb]
    cc2.append(d2)
    
#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
