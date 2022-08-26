import mysql.connector as connection

mydb = connection.connect(host = "localhost", user = "root", passwd = "Root@123")


cursor = mydb.cursor()
#cursor.execute("create database Naveen")
#cursor.execute("show databases")
s = "create table Naveen.navdetails(employee_id int(10), employee_name varchar(80) , emp_mailid varchar(80), emp_salary int(6))"

q1 = cursor.execute(s)

#q2 = cursor.execute("select * from Naveen.navdetails ")
#print(q2)
