from datetime import datetime
start_time = datetime.now()
import pandas as pd

#creating databases using pandas for both input csv files
dt=pd.read_csv("input_attendance.csv")
dtx=pd.read_csv("input_registered_students.csv")
dt=dt.dropna()
dt["Timestamp"]=pd.to_datetime(dt["Timestamp"],dayfirst=1) #coverting strings to datetime format

#coverting column wise database to lists 
timestamp=list(dt["Timestamp"])
attendance=list(dt["Attendance"])
roll_no=list(dtx["Roll No"])
name=list(dtx["Name"])

#creating a time interval for comparison
comp_time=["14:00","15:00"]
for i in range(0,len(comp_time)):
    comp_time[i]=datetime.strptime(comp_time[i],'%H:%M')

#creating two lists containing the roll no. and names seperately , and i will work with roll no.
attendance_roll=[]
attendance_name=[]
for i in attendance:
    j=i.split(" ")
    attendance_roll.append(j[0])
    attendance_name.append(j[1])
    
#dropping duplicates from the duplicates
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
  
#calculating actual and fake attendance  
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

#calculating the total number of lectures taken    
lec_date_data=[]
for i in range(0,len(attendance_roll)):
    if timestamp[i].isoweekday()==1 or timestamp[i].isoweekday()==4:
        lec_date_data.append(timestamp[i].date())

lec_taken=set(lec_date_data)
Total_lec_taken=len(lec_taken)

#calculating the count of absent (total lectures taken = actual attendance + absent count)
Absent_count=[]
for i in range(0,len(roll_no)):
    c=0
    c=Total_lec_taken-Actual_attendance[i]
    Absent_count.append(c)

#creating a folder 'output' to hold all the output files    
import os
os.mkdir('Output')

#writing to individual csv files    
import csv
for i in range(0,len(roll_no)):
    with open('Output/{}.csv'.format(str(roll_no[i])),'w',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(['Roll_No','Name','Total_lecture_taken','Attendance_count_actual','Attendance_count_fake','Attendance_count_absent','Percentage'])
        writer.writerow([roll_no[i],name[i],Total_lec_taken,Actual_attendance[i],Fake_attendance[i],Absent_count[i],'{0:.2f}'.format(Actual_attendance[i]*100/Total_lec_taken)])

#con contains the rows to be written on the consolidated csv file
con=[]
for i in range(0,len(roll_no)):
    l=[]
    l=[roll_no[i],name[i],Total_lec_taken,Actual_attendance[i],Fake_attendance[i],'{0:.2f}'.format(Actual_attendance[i]*100/Total_lec_taken)]
    con.append(l)
    
#writing to consolidated file
with open('Output/Attendance_report_consolidated.csv','w',newline='') as g:
    writer=csv.writer(g)
    writer.writerow(['Roll_No','Name','Total_lecture_taken','Attendance_count_actual','Attendance_count_fake','Attendance_count_absent','Percentage'])
    for i in range(0,len(roll_no)):
        writer.writerow(con[i])

#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))

#program completed to my best capacity ( made on SPYDER IDE 5.3.3 with PYTHON 3.8.10 64 BIT)