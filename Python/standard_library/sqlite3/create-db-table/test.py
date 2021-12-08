import sqlite3
import os 


if os.path.isfile('bd1.bd'):
	print("Database already exists!")

else:
	conexion = sqlite3.connect("bd1.bd")
	conexion.execute("""CREATE TABLE IF NOT EXISTS article(
						code INTEGER PRIMARY KEY AUTOINCREMENT,
						desc TEXT,
						price REAL)""")
	print("Database created successfully!")
	conexion.close()

	

