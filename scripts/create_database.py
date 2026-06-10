import sqlite3

conn = sqlite3.connect("Data/Db/bluestock_mf.db")


with open("SQL/schema.sql", "r") as file:
    schema = file.read()


conn.executescript(schema)

print("Database and tables created successfully!")

conn.commit()
conn.close()