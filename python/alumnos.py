import sqlite3

conn = sqlite3.connect('alumnos.db')
cursor = conn.cursor()

query = 'select * from alumno where nombre = "pedro"'

rows = cursor.execute(query)

for row in rows:
    print(row)

cursor.close()
conn.close()
