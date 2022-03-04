import sqlite3


db = sqlite3.connect(database='sqlite.db')
cursor = db.cursor()

# INFO: Create table
# cursor.execute(
#     "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)"
# )

# INFO: Insert data
cursor.execute(
    "INSERT INTO books VALUES(1, 'Harry Potter', 'J.K. Rowling', '9.5')"
)
db.commit()