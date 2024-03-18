import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="test")
mycursor=mydb.cursor()
sql="delete from customer where name='hanna'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record deleted")
