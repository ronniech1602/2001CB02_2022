from datetime import datetime
start_time = datetime.now()
import pandas as pd

dt=pd.read_csv("input_attendance.csv")
dtx=pd.read_csv("input_registered_students.csv")
dt=dt.dropna()
dt["Timestamp"]=pd.to_datetime(dt["Timestamp"],dayfirst=1)

timestamp=list(dt["Timestamp"])
attendance=list(dt["Attendance"])
roll_no=list(dtx["Roll No"])
name=list(dtx["Name"])

comp_time=["14:00","15:00"]
for i in range(0,len(comp_time)):
    comp_time[i]=datetime.strptime(comp_time[i],'%H:%M')

attendance_roll=[]
attendance_name=[]
for i in attendance:
    j=i.split(" ")
    attendance_roll.append(j[0])
    attendance_name.append(j[1])
    
list_tmp=[]
c=0
for i in range(c,len(timestamp)):
    if timestamp[i].weekday()==0 or timestamp[i].weekday()==3:
        if comp_time[0].time()<=timestamp[i].time()<=comp_time[1].time():
            for j in range(c,len(timestamp)):
                if timestamp[i].date()==timestamp[j].date() and attendance_roll[i]==attendance_roll[j]:
                    if comp_time[0].time()<=timestamp[j].time()<=comp_time[1].time():
                        if j!=i:
                            list_tmp.append(j)
            c=j+1            
                
dt=dt.drop(index=list_tmp)
    
Actual_attendance=[]
Fake_attendance=[]
for i in range(0,len(roll_no)):
    a=0
    b=0
    for j in range(0,len(attendance_roll)):
        if roll_no[i]==attendance_roll[j]:
            if timestamp[j].isoweekday()==1 or timestamp[j].isoweekday()==4:
                if timestamp[j].time()>=comp_time[0].time() and timestamp[j].time()<=comp_time[1].time():
                    a+=1
                else:
                    b+=1
            else:
                b+=1
    Actual_attendance.append(a)
    Fake_attendance.append(b)

#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))