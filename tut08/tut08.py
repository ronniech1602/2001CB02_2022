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
    p=i.split(" ",maxsplit=2)
    if len(p)==1:
        runf2.append(p[0])
        runs2.append(" ")
    if len(p)>1:
        runf2.append(p[0])
        runs2.append(p[1])
        
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

def totalscore(x):
    y=0
    for i in x:
        y=y+i[1]+i[2]*2+i[3]*3+i[4]*4+i[5]*5+i[6]*6+i[8]+i[9]+i[10]+i[11]
    return(y)

def wickets(z):
    y2=0
    for i in z:
        y2=y2+i[7]
    return(y2) 

pak_list=list(pak_team.keys())
ind_list=list(ind_team.keys())
with open('scorecard.txt','w') as op:
    print('Pakistan Batting',file=op)
    print("Total score : "+str(totalscore(c))+'-'+str(wickets(c)),file=op)
    print(f"{'Player':<25}{'Runs Scored':<15}{'Balls Faced':<15}{'4s':<10}{'6s':<10}",file=op)
    for i in range(0,len(pak_team)):
        print(f"{pak_list[i]:<25}{str(c[i][1]+c[i][2]*2+c[i][3]*3+c[i][4]*4+c[i][5]*5+c[i][6]*6):<15}{str(c[i][0]+c[i][1]+c[i][2]+c[i][3]+c[i][4]+c[i][5]+c[i][6]+c[i][7]):<15}{str(c[i][4]):<10}{str(c[i][6]):<10}",file=op)
    print("",file=op)
    print("Indian bowling",file=op)
    print(f"{'Player':<25}{'Runs conceeded':<15}{'Wickets':<15}{'Balls bowled':<15}{'4s hit':<10}{'6 hit':<10}",file=op)
    for i in range(0,len(ind_team)):
        print(f"{ind_list[i]:<25}{str(cc[i][1]+cc[i][2]*2+cc[i][3]*3+cc[i][4]*4+cc[i][5]*5+cc[i][6]*6+cc[i][8]+cc[i][9]+cc[i][10]+cc[i][11]):<15}{str(cc[i][7]):<15}{str(cc[i][0]+cc[i][1]+cc[i][2]+cc[i][3]+cc[i][4]+cc[i][5]+cc[i][6]+cc[i][7]+cc[i][9]+cc[i][10]):<15}{str(cc[i][4]):<10}{str(cc[i][6]):<10}",file=op)
    print('',file=op)
    print('',file=op)
    print('Indian Batting',file=op)
    print("Total score : "+str(totalscore(c2))+'-'+str(wickets(c2)),file=op)
    print(f"{'Player':<25}{'Runs Scored':<15}{'Balls Faced':<15}{'4s':<10}{'6s':<10}",file=op)
    for i in range(0,len(ind_team)):
        print(f"{ind_list[i]:<25}{str(c2[i][1]+c2[i][2]*2+c2[i][3]*3+c2[i][4]*4+c2[i][5]*5+c2[i][6]*6):<15}{str(c2[i][0]+c2[i][1]+c2[i][2]+c2[i][3]+c2[i][4]+c2[i][5]+c2[i][6]+c2[i][7]):<15}{str(c2[i][4]):<10}{str(c2[i][6]):<10}",file=op)
    print("",file=op)
    print("Pakistan bowling",file=op)
    print(f"{'Player':<25}{'Runs conceeded':<15}{'Wickets':<15}{'Balls bowled':<15}{'4s hit':<10}{'6 hit':<10}",file=op)
    for i in range(0,len(pak_team)):
        print(f"{pak_list[i]:<25}{str(cc2[i][1]+cc2[i][2]*2+cc2[i][3]*3+cc2[i][4]*4+cc2[i][5]*5+cc2[i][6]*6+cc2[i][8]+cc2[i][9]+cc2[i][10]+cc2[i][11]):<15}{str(cc2[i][7]):<15}{str(cc2[i][0]+cc2[i][1]+cc2[i][2]+cc2[i][3]+cc2[i][4]+cc2[i][5]+cc2[i][6]+cc2[i][7]+cc2[i][9]+cc2[i][10]):<15}{str(cc2[i][4]):<10}{str(cc2[i][6]):<10}",file=op)    
    
#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
