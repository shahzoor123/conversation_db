import sqlite3


user_data = [
    ("mohsin", 28, "9292-3232-23"),
    ("ahsan", 22, "192-132-23"),
    ("shahzoor", 25, "782-3232-23"),
    ("ammar", 35, "782-3232-23"),

    ]



 # connect to db
conn = sqlite3.connect('conversation.db')

# Create table
conn.execute('''CREATE TABLE IF NOT EXISTS users 
                (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, phone TEXT)''')

# Insert data 
conn.executemany("INSERT INTO users (name, age, phone) VALUES (?, ?, ?)",user_data)    


user_info = conn.execute("SELECT * FROM users ORDER BY name")
res = user_info.fetchall()

for row in res:
    print(f' "Name" : {row[1]}')
    print(f' "Age" : {row[2]}')
    print(f' "Phone no" : {row[3]}')
    print(" ")

#write data
conn.commit()
#close connection
conn.close()

