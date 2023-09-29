import mysql.connector
mydb=mysql.connector.connect(
       host="localhost",
       user="root",
       password="Sakthi@123",
       database="sakthi"
       )
mycursor=mydb.cursor()
rno=input("Enter the roll no to delete:")
mycursor.execute("select*from students where rollno="+rno)
cnt=mycursor.fetchall()
if(len(cnt)>0):
       mycursor.execute("delete from students where rollno="+rno)
       mydb.commit()
       print()
       print("Record deleted successfully")
       mycursor.execute("select*from students")
       myresult=mycursor.fetchall()
       print("*"*50)
       print("STUDENTS LIST AFTER DELETION".center(50))
       print("*"*50)
       print()
       print("No.\tName \tCourse \tFees \tAddress")
       print()
       for x in myresult:
              for r in x:
                     print(str(r)+"\t",end="")
              print()
       print()
       print("*"*50)
else:
       print("Record not found")
       
       
