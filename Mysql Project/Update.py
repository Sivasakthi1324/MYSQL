import mysql.connector
mydb=mysql.connector.connect(
       host="localhost",
       user="root",
       password="Sakthi@123",
       database="sakthi"
       )
mycursor=mydb.cursor()
pro="y"
while(pro=='y' or pro=='Y'):
       rno=input("Enter The Rollno To Edit details:")
       mycursor.execute("select*from students where rollno="+rno)
       cnt=mycursor.fetchall()
       for r in cnt:
              print("Current Details For The Rollno:"+rno)
              print()
              print("\t"+str(r)+"\t",end="")
              print()
              if(len(cnt)>0):
                     print("\t1-Name")
                     print("\t2-Course")
                     print("\t3-Fees")
                     print("\t4-Address")
                     ch=int(input("Select Your Choice To Update:"))
                     if ch==1:
                            data=input("Enter the new name to update:")
                            sql="update students set sname='"+data+"' where rollno="+rno
                     elif ch==2:
                            data=input("Enter the new course to update:")
                            sql="update students set course='"+data+"' where rollno="+rno
                     elif ch==3:
                            data=input("Enter the new fees to update:")
                            sql="update students set fees='"+data+"' where rollno="+rno
                     elif ch==4:
                            data=input("Enter the new address to update:")
                            sql="update students set address='"+data+"' where rollno="+rno
                     else:
                            print("You have entered wrong choice")
                     mycursor.execute(sql)
                     mydb.commit()
                     print()
                     print("Record updated successfully")
                     mycursor.execute("select*from students")
                     myresult=mycursor.fetchall()
                     print("*"*50)
                     print("STUDENTS LIST AFTER DELETION".center(50))
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
else:
       print("Record not found")
pro=input("Do you want to continue(Y/N)")
