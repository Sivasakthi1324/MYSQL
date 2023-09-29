import mysql.connector
mydb=mysql.connector.connect(
       host="localhost",
       user="root",
       password="Sakthi@123",
       database="sakthi"
       )
mycursor=mydb.cursor()
mycursor.execute( " insert into students values(1,'Aarthy','Java',10000,'Thirumangalam')")
mydb.commit()
print("Record Inserted Successfully")
mycursor.close()
mydb.close()
