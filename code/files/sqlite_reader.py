import sqlite3

conn = sqlite3.connect("people.db")
cursor = conn.cursor()
people = cursor.execute("SELECT * FROM people")
print(people.fetchall()) # prints [('Alice', 30)]
conn.commit()
conn.close()
