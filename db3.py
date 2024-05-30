
#write a program  to insert data by dynamic input

import mysql.connector
try: 
    con=mysql.connector.connect(user="root", password="2379",host="localhost",database="sarvesh")
    cursor=con.cursor()

    while True:
        eno=int(input("enter employee Number  : "))
        ename=input("enter employee Name:")
        esal=int(input("enter the Empolyee salary:"))
        eaddr=input("enter the Empolyee Address:")
        
        sql = "insert into abc values (%d, '%s', %d, '%s')"
        cursor.execute(sql %(eno,ename,esal,eaddr))
        con.commit()
        print("1 row inseted successfully...")
        op=input('Do you want to inset one more record (yes/no) ')
        if op=='no':
           break

except mysql.connector.DatabaseError as e :
    if con:
        con.rollback()
        print("There is a problem with sql:",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()     
       