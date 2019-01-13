import sqlite3


conn = sqlite3.connect("my-db.sqlite")
fname = input("what's your first name? ")
lname = input("what's your last name? ")
age = input("how old are you? ")
# fname = 'john", "smith", 20); ....; INSERT INTO student (firstname, lastname, age) VALUES ("John'
cmd = 'INSERT INTO student (firstname, lastname, age) VALUES ("' + fname + '", "' + lname + '", ' + age + ');'
conn.execute(cmd)

conn.commit()