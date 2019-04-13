#By Vipin Yadav
import cx_Oracle
import time
from datetime import datetime

today = datetime.today()
d1 = today.strftime("%d/%m/%Y")
now = datetime.now()
dt_st=now.strftime("Date :%d/%m/%Y   Time :%H:%M:%S")
print(dt_st)	
dsn_tns = cx_Oracle.makedsn(host='localhost', port='1521', service_name='orcl')
conn = cx_Oracle.connect(user='hr', password='hr', dsn=dsn_tns)

def detail():
    
    start=time.time()
    c = conn.cursor()
    c.execute('select * from hr.student')
    for row in c:
        print (row[0], '-', row[1], '-', row[2])
    elapsed=(time.time() - start)
    print(elapsed , " Second")
    c.close()    


def insert():
    #name=str(input("Enter Name:"))
    #ide=int(input("Enter ID:"))
    row=[(110,'Vipin','BCA')]
    c.bindarraysize=1
    c.setinputsizes(int,'20')
    #course=str(input("Enter Course:"))
    c = conn.cursor()
    c.execute('insert into student(S_id,S_Name,cours) values(:1, :2 ,:3)',row)
    


def orderByName():
    start=time.time()
    c = conn.cursor()
    c.execute("select * from student order by S_Name")
    res=c.fetchall()
    print(res)
    #for row in c:
    #    print(row[0], '|', row[1], '|', row[2])
    elapsed=(time.time() - start)
    print(elapsed , " Second")
    c.close()


def SearchBy():
    Y=True
    start=time.time()
    c = conn.cursor()
    while Y:
        a=int(input("Enter ID for search:"))
        c.prepare("select * from student where S_ID= :id")
        c.execute(None,{'id':a})
        res=c.fetchall()
        print("ID : ",res[0][0],"\nName : ",res[0][1],"\nCourse : ",res[0][2])
        elapsed=(time.time() - start)
        print(elapsed , " Second")
        z=input("For More Search Enter Y:")
        if z=='Y' or z=='y':
            Y=True
        else:
            Y=False 
    c.close()
    
    
             
    

##############################################################Call#############################
SearchBy()
detail()
orderByName()
insert()
