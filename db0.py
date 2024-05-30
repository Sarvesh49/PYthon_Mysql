import mysql.connector

con = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2379"
)

mycursor = con.cursor()

mycursor.execute("CREATE DATABASE test4")