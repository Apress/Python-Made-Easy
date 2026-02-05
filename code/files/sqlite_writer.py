import sqlite3

conn = sqlite3.connect("people.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE people (name TEXT, age INTEGER)")
cursor.execute("INSERT INTO people (name, age) VALUES ('Alice', 30)")
conn.commit()
conn.close()
