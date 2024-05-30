# WPA  to create tables,data and display data by using database

import mysql.connector
try:
    con=mysql.connector.connect(user="root",password="2379",host="localhost",database="test4")
    cursor=con.cursor()
    cursor.execute( "create table emp3(eno int(5) primary key,ename varchar(255),esal double(10,2),eaddr varchar(255))")
    print("Table created...")
    sql ="insert  into emp3(eno, ename, esal, eaddr) VALUES(%s, %s, %s, %s)"
    records=[(10,'sachin', 1000, 'mumbai'), 
            (200,'Dhoni', 2000, "ranchi" ), 
            (300,'kohli', 3000, 'Delhi')]
    cursor.executemany(sql,records)
    con.commit()
    print("Records Inserted successfully....")
    cursor.execute(" select * from emp3")
    data=cursor.fetchall() #--- all data is fetch by using this function
    for row in data:
        print("Employee Number :",row[0])
        print("Employee Name :",row[1])
        print("Employee salary :",row[2])
        print("Employee Address :",row[3])

except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()  # --- data wiil not be commited if database error occuros
        print("There is a problem with mysql: ",e)
finally:
    if cursor:
    # if cursor:user="root",password="2379",host="localhost",database="test4")
        cursor.close()
    if con:
        con.close()