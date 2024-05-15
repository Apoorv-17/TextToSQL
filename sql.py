import sqlite3


## Connect to sqlite
connection=sqlite3.connect("student.db")

## Create a cursor object to insert record, create table, retrieve
cursor=connection.cursor()

## Create the table
table_info="""
CREATE TABLE Student(
    Name VARCHAR(25),
    Class VARCHAR(25),
    Section VARCHAR(25),
    Marks INT);
"""

cursor.execute(table_info)

## Insert some more records

cursor.execute('''INSERT INTO Student VALUES('Apoorv', 'Data Science', 'A', 91);''')
cursor.execute('''INSERT INTO Student VALUES('Shubham', 'Data Science', 'C', 72);''')
cursor.execute('''INSERT INTO Student VALUES('Divyanu', 'Data Science', 'B', 86);''')
cursor.execute('''INSERT INTO Student VALUES('Shushant', 'Data Science', 'A', 92);''')
cursor.execute('''INSERT INTO Student VALUES('Ashish', 'Data Science', 'B', 83);''')

## DisPlay all the records

print("The inserted records are: ")

data = cursor.execute('''SELECT * FROM Student;''')

for row in data:
    print(row)

connection.commit()
connection.close()