import mysql.connector
mydb=mysql.connector.connect(
       host="localhost",
       user="root",
       password="Sakthi@123",
       database="sakthi"
       )
mycursor=mydb.cursor()
rno=input("Enter the Roll no:")
mycursor.execute("select*from students where rollno="+(rno))
myresult=mycursor.fetchall()
print("*"*50)
print("STUDENTS LISTS".center(50))
print("*"*50)
print()
print("No. \tName \tCourse \tFees \tAddress")
print()
for x in myresult:
       for r in x:
              print(str(r)+"\t",end="")
       print()
print()
print("*"*50)
