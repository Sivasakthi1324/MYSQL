import mysql.connector
mydb=mysql.connector.connect(
       host="localhost",
       user="root",
       password="Sakthi@123",
       database="sakthi"
       )
mycursor=mydb.cursor()
mycursor.execute("select*from students")
myresult=mycursor.fetchall()
print("*"*50)
print("STUDENTS LISTS".center(50))
print("*"*50)
print()
for x in myresult:
       print(x)
       print()
print()
print("*"*50)
