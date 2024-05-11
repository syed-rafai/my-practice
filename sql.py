import mysql.connector as conn
mydb=conn.connect(host="localhost",user="root",password="Syh6798")
print("connection created",mydb)

# create a database 
# import mysql.connector as conn
# mydb=conn.connect(host="localhost",user="root",password= "Syh6798")
# cursor=mydb.cursor()
# cursor.execute("Create database db1")
# print("database created")

#create table 
# import mysql.connector as conn
# mydb=conn.connect(host="localhost",user="root",password="Syh6798",database="db1")
# cursor=mydb.cursor()
# cursor.execute("create table student(F_name varchar(10),L_name varchar(20), stu_id int)")
# print("table created")

# to check the table
# import mysql.connector as conn
# mydb=conn.connect(host="localhost",user="root",password="Syh6798",database="db1")
# cursor=mydb.cursor()
# cursor.execute("show tables")
# for i in cursor:
#     print(i)

#To insert the values
# import mysql.connector as conn
# mydb=conn.connect(host="localhost",user="root",password="Syh6798",database="db1")
# cursor=mydb.cursor()
# cursor.execute("insert into student(F_name,L_name,stu_id) values(%s,%s,%s)",("amar","raj",1))
# mydb.commit()# save
# print(cursor.rowcount,"record inserted")

# #to insert multiple values at a time
# import mysql.connector as conn
# mydb=conn.connect(host="localhost",user="root",password="Syh6798",database="db1")
# cursor=mydb.cursor()
# insert_may="insert into student(F_name,L_name,stu_id) values(%s,%s,%s)"
# values=[("ajay","raj",1),("raj","raj",2),("yash","raj",3)]
# cursor.executemany(insert_may,values)#variable
# mydb.commit()
# print(cursor.rowcount,"record inserted")

##to select n rows of database from python
# import mysql.connector as conn
# mydb=conn.connect(host="localhost",user="root",password="Syh6798",database="db1")
# cursor=mydb.cursor()
# cursor.execute("select *from db1.student")
# for content in cursor.fetchall():
#     print(content)
# content=cursor.fetchall()
# content=cursor.fetchone()
# print(content)

## to update data
# import mysql.connector as conn
# mydb=conn.connect(host="localhost",user="root",password="Syh6798",database="db1")
# cursor=mydb.cursor()
# updatedata="update db1.student set stu_id=%s where F_name=%s"
# value=(20,"ajay")
# cursor.execute(updatedata,value)
# mydb.commit()
# print(cursor.rowcount,"data update")

## to delet single row data
# import mysql.connector as conn
#mydb=conn.connect(host="localhost",user="root",password="Syh6798",database="db1")
#cursor=mydb.cursor()
#deldata="delete from db1.student where F_name=%s"
#value=("ajay",)
#cursor.excute(deldata,value)
#mydbcommit()
#print(cursor.rowcount,"record deleted")

## to delete all data present in the table
# import mysql.connector as conn
# mydb=conn.connect(host="localhost",user="root",password="Syh6798",database="db1")
# cursor=mydb.cursor()
# truncdata="truncate table db1.student"
# cursor.execute(truncdata)
# mydb.commit()
# print("all data deleted")

import mysql.connector as conn
# myap=conn.connect(host="localhost",user="root",password="Syh6798")
# print("connection created",myap)

# cursor=myap.cursor()
# cursor.execute("create database name")
# print("database created")
mydb=conn.connect(host="localhost",user="root",password="Syh6798",database="name")# to coonnect connection b/w data base to py
# cursor=mydb.cursor()
# cursor.execute("create table student(F_name varchar(10),L_name varchar(20), stu_id int)")
# print("table created")
cursor=mydb.cursor()
# cursor.execute("insert into student(F_name,L_name,stu_id) values(%s,%s,%s)",("amar","raj",1))
# mydb.commit()# save
# print(cursor.rowcount,"record inserted")

# insert_may="insert into student(F_name,L_name,stu_id) values(%s,%s,%s)"
# values=[("ajay","raj",1),("raj","raj",2),("yash","raj",3)]
# cursor.executemany(insert_may,values)#variable
# mydb.commit()
#print(cursor.rowcount,"record inserted")
# deldata="delete from name.student where F_name=%s"
# value=("ajay",)
# cursor.execute(deldata,value)
# mydb.commit()
# print(cursor.rowcount,"record deleted")
truncdata="truncate table name.student"
cursor.execute(truncdata)
mydb.commit()
print("all data deleted")
