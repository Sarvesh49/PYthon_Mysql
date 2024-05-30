#write a program to drop the table
'''import mysql.connector
try:
    connection=mysql.connector.connect(user="root",password="Sarvesh@2379",host="loaclhost",database="test2")
    cursor = connection.cursor()
    
    sql = "drop table emp2"
    cursor.execute(sql)
    print("table created successfully...." )

except mysql.connector.DatabaseError as e:
    if connection:
        connection.rollback()
        print("There is a problem with sql:",e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("mysql connection is closed")'''      

#=====================================================================
'''import mysql.connector

#establishing the connection conn = mysql.connector.connect(
connection=mysql.connector.connect(user="root",password="2379",host="localhost",database="test2")

#Creating a cursor object using the cursor() method 
cursor = connection.cursor()

#Retrieving the list of tables print("List of tables in the database: ") 
cursor.execute("SHOW Tables")
print(cursor.fetchall())

#Doping EMPLOYEE table if already exists cursor.execute
("DROP TABLE emp3") 
print("Table dropped... ")

#Retrieving the list of tables print(
"List of tables after dropping the emp3 table: " 
cursor.execute("SHOW Tables") 
print(cursor.fetchall())

#Closing the connection connection.close'''
#==========================================================================================
#incement all employes salaries by 700 whoses salary <4000
import mysql.connector

con=mysql.connector.connect(user="root",password="2379",host="localhost",database="test4")
cursor = con.cursor()
increment = float(input("Enter increment salary:") )
salrange=float(input("Enter salary range :"))
sql="update emp3 set esal=esal+%f where esal<%f"
cursor.execute(sql %(increment,salrange))
print("Record updated")
connection.commit()
