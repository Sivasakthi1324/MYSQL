import mysql.connector
mydb=mysql.connector.connect(
       host="localhost",
       user="root",
       password="Sakthi@123",
       database="sakthi"
       )
mycursor=mydb.cursor()
mycursor.execute("select max(rollno) from students")
myresult=mycursor.fetchall()
for x in myresult:
       rno=int(x[0]+1)
sname=input("What is your name")
course=input("Enter the course name")
fees=int(input("What is the fees for the course"))
address =input("Enter your address")
mycursor.execute("insert into students values("+str(rno)+",'"+str(sname)+"','"+str(course)+"',"+str(fees)+",'"+str(address)+"')")
mydb.commit()
print("Record inserted successfully")
mycursor.execute("select*from students where rollno="+str(rno))
myresult=mycursor.fetchall()
print("The details of students are:")
for x in myresult:
       print(x)
