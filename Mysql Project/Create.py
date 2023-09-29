import mysql.connector
mydb=mysql.connector.connect(
       host="localhost",
       user="root",
       password="Sakthi@123",
       database="sakthi"
       )
mycursor=mydb.cursor()
mycursor.execute("create table students(rollno int primary key auto_increment, sname varchar(20),course varchar(20),fees int, address varchar(100))")
mydb.commit()
print("Table created successfully")
mycursor.close()
mydb.close()
