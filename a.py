import pyodbc

conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=LAPTOP-HFO4K8AP\MYSQL;'
    'Database=pythonweekend;'
    'Trusted_Connection=yes;')


cursor = conn.cursor()
# cursor.execute(
#     'CREATE TABLE EMP_INFO(PersonID int not null,LastName varchar(255), FirstName varchar(255),Address varchar(255),City varchar(255))')

cursor.execute(
    "insert into EMP_INFO(PersonID,LastName,FirstName,Address,City)values(1,'yadav','verma','rahul vihar','gzb')")

# # # # for i in cursor:
# # # #     print(i)
conn.commit()

# import mysql.connector

# mydb = mysql.connector.connect(
#     host='localhost', user='root', password="", database='customers')

# cursor = mydb.cursor()

# cursor.execute(
# 'CREATE TABLE Persons( PersonID int,LastName varchar(255),FirstName varchar(255), Address varchar(255), City varchar(255))')
# cursor.execute('select * from customers ')
# cursor.execute('select name from customers order by name DESC Limit 2 ')
# try:
#     # cursor.execute(
#     #     'CREATE TABLE EMP( PersonID int,LastName varchar(255))')
#     # cursor.execute("insert into emp(PersonID,LastName)values(1,'yadav')")
# except:
#     print("not working")

# # sel = cursor.fetchone()
# sels = cursor.fetchall()
# # print(sel, sels)
# for i in sels:
#     print(i)
# # cursor.execute(
# #     "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# cursor.commit()

# # sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# # val = [
# #     ('Peter', 'Lowstreet 4'),
# #     ('Amy', 'Apple st 652'),
# #     ('Hannah', 'Mountain 21'),
# #     ('Michael', 'Valley 345'),
# #     ('Sandy', 'Ocean blvd 2'),
# #     ('Betty', 'Green Grass 1'),
# #     ('Richard', 'Sky st 331'),
# #     ('Susan', 'One way 98'),
# #     ('Vicky', 'Yellow Garden 2'),
# #     ('Ben', 'Park Lane 38'),
# #     ('William', 'Central st 954'),
# #     ('Chuck', 'Main Road 989'),
# #     ('Viola', 'Sideway 1633')
# # ]

# # cursor.executemany(sql, val)

# # mydb.commit()

# # print(cursor.rowcount, "was inserted.")
