import mysql.connector
try:
	con=mysql.connector.connect(user="root",password="2379",host="localhost",database="mydatabase")
	mycursor=con.cursor()
	cursor.execute("CREATE table emp3(eno int(5) primary key,ename varchar(10),esal double(10,2)eaddr varchar(10))")
	print("Table created..")
	sql="insert into emp(eno,ename,esal,eaddr) VAULES(%s,%s,%s,%s)"
	records=[(10,'sachin',1000,'mumbai'),(200,'max',2000,'mumbai'),(300,'yash',1000,'Delhi')]
	cursor.executemany(sql,records)
	con.commit()
	print("records inserted successfully....")
	cursor.execute("Select * from emp")
	data=cursor.fetchall()
	for row in data:
		print("Employee Number :",row[0])
		print("Employee Name :",row[1])
		print("Employee salary :",row[2])
		print("Employee Address :",row[3])
except mysql.connector.connect.DatabaseError as e:
	if con:
		con.rollback()
		print("There is problem with mysql :",e)
finally:
	if cursor:
		cursor.close()
	if con:
		con.close()