from week2.connector import MySqlConnector

try:
    connector = MySqlConnector(host="localhost", port=8889, user="root", password="root", db="mydb")
    connection = connector.get_connection()
    cursor = connection.cursor()

    # print("attempting to create a database ...")
    # cursor.execute("CREATE DATABASE mydb")
    # print("db creation succeeded")

    # print("attempting to create a table ...")
    # cursor.execute("CREATE TABLE friends (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT(10))")
    # print("table creation succeeded")

    # print("attempting to add record to the table ...")
    # cursor.execute("INSERT INTO friends (name, age) VALUES ('Prabhjot', 23)")
    # connection.commit()
    # print(cursor.rowcount, "record added")

    print("attempting to fetch data from the table ...")
    cursor.execute("SELECT * FROM friends")
    print(cursor.fetchall())
    print("data fetched")

except Exception as e:
    print(e)

