import mysql.connector

# sql username and password
mydb = mysql.connector.connect(host="LocalHost", user="root", passwd="aishu@1234", database="jdbc")

# to fetch all dbs in the mysql
# cursor, a function are used as pointing something that connects with db and fetch the required details

mycursor = mydb.cursor()

# To execute sql statement, have to use execute method
# Inside the double quotes can write the sql query

mycursor.execute("select * from students")
# if we run here it will just stop in cursor to print it we use for loop
for i in mycursor:
    print(i)

# to insert the value got from the user in the db
# we need to declare query in a String sql and the values to be inserted in the separate String as val
# and declare them in the separate execution
name = input("Enter name:")
age = input("Enter age:")
# to insert specific values we use the below format
s = {"Name": name}  # it is changes to dict and appended as the tuple for the query execution
sql = "insert into students ({}) values ({})".format(", ".join(s.keys()), ", ".join(["%s"] * len(s)))
val = tuple(s.values())
mycursor.execute(sql, val)

# update specific values in column
sql2 = "update students set Name='Aish' where Id=20"
mycursor.execute(sql2)
for i in mycursor:
    print(i)
