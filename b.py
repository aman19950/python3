import mysql.connector
# pip install mysql-connector-python
try:

    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password="",
        database='python2408'

    )

    cursor = mydb.cursor()
    # cursor.execute('create database python2408')

    # cursor.execute('create ')

    # que = "create database customers"
    # cursor.execute(que)
    # mydb.commit()
    # cursor.execute("use customers")
    # cursor.execute(
    #     "create table customers_dtls(id int not null,name varchar(20),email varchar(50),salary int not null)")
    # cursor.execute(
    #     "insert into customers_dtls(id, name,email,salary)values( 1,'sonu','sonu@gmail.com',3000)")
    # mydb.commit()
    # cursor.execute(
    #     "insert into customers_dtls(id, name,email,salary)values( 1,'monu','monu@gmail.com',2000); ")
    # mydb.commit()
    # sql = "INSERT INTO customers_dtls (id, name,email,salary) VALUES (%s, %s,%s,%s)"
    # val = [
    #     (2, 'Peter', 'aa@gmail.com', 2000),
    #     (3, 'Amy', 'b@gmail.com', 4000),
    #     (4, 'Hannah', 'c@gmail.com', 1000),
    #     (5, 'Michael', 'd@gmail.com', 5000),
    #     (6, 'Sandy', 'e@gmail.com', 6000)
    # ]

    # cursor.executemany(sql, val)
    # mydb.commit()

    # cursor.execute(
    #     "insert into customers_dtls(id, name,email)values( 4,'sohan','s@gmail.com'); ")
    # cursor.execute("insert into customers_dtls(id, name)values( 4,'sohan'); ")

    cursor.execute(
        "select * from customers_dtls")

    # dtls = cursor.fetchall()
    # # print(dtls)
    # # # # # # print(dtls)
    # for i in dtls:
    #     print(i)
    print(cursor.fetchone())
    # print(cursor.fetchone())
    # print(cursor.fetchone())
    # print(cursor.fetchone())
    # print(cursor.fetchone())
    # print(cursor.fetchone())
    # print(cursor.fetchone())
    # print(dtls)
    # for i in dtls:
    #     print(i)

    # for i in dtls:
    #     print(i)
    # cursor.execute(
    #     "select name,salary from customers_dtls limit 5")
    # dtls = cursor.fetchall()
    # # print(dtls)
    # for i in dtls:
    #     print(i)
    # cursor.execute("select * from customers_dtls where id = 4")

    # cursor.execute("select * from customers_dtls order by id DESC  ")
    # cursor.execute("select * from customers_dtls order by id DESC limit 2")
    # cursor.execute("update customers_dtls set name = 'rohan' where id = 1")
    # cursor.execute("SELECT salary,name FROM customers_dtls WHERE salary = (SELECT max(salary) from customers_dtls)")
    # # cursor.execute("select max(salary) from customers_dtls")
    # cursor.execute("select count(salary) from customers_dtls")
    # cursor.execute("select avg(salary) from customers_dtls")
    # cursor.execute("select sum(salary) from customers_dtls")
    # cursor.execute("select * from customers_dtls group by name")
    # cursor.execute("select id, name from customers_dtls where id = 1 or 1=1; ")

    # dtls = cursor.fetchall()
    # print(dtls)
    # for i in dtls:
    #     print(i)
    # mydb.commit()
    # print(cursor.rowcount, "Record inserted successfully into customers_dtls table")
    # cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))
