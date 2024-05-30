'''Python MySQL Create Database
Creating a Database
To create a database in MySQL, use the "CREATE DATABASE" statement:

Example
create a database named "mydatabase1":'''

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2379"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE test4")


'''Check if Database Exists
You can check if a database exist by listing all databases in your system by using the "SHOW DATABASES" 
statement:

Example

Return a list of your system's databases:

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2379"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

--------------------------------------------------------------------------------------
Or you can try to access the database when making the connection:


Example
Try connecting to the database "mydatabase":

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2379",
  database="mydatabase1"
)
If the database does not exist, you will get an error.

'''

