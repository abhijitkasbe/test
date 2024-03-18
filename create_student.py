import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="test")
mycursor=mydb.cursor()
mycursor.execute("create table student(name varchar(200),password varchar(40 ))")

