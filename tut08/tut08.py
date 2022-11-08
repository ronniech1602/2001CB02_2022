from datetime import datetime
start_time = datetime.now()

import csv

f = open("pak_inns1.txt","r",newline='') 
file = csv.DictReader(f,fieldnames=["from-to","runs"],restkey="alpha")

from_to=[]
runs=[]

for col in file:
    from_to.append(col["from-to"])
    runs.append(col["runs"])

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
pak_s=list(pak)
ind_s=set(ind)
ind_s=list(ind)



#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
