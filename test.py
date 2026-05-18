import sqlite3
db = sqlite3.connect('countries.db')
cursor = db.cursor()
cursor.execute("SELECT * FROM cities_list LIMIT 5")
print(cursor.fetchall())