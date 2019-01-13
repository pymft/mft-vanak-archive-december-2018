import sqlite3


conn = sqlite3.connect("my-db.sqlite")
conn.execute('INSERT INTO student (firstname, lastname, age) VALUES ("Emma", "Watson", 28);')
# conn.commit()