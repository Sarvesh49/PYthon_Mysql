import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2379",
  database="sarvesh"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE abc (eno VARCHAR(255), ename VARCHAR(255),esal VARCHAR(255), eaddr VARCHAR(255))") 