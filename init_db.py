import sqlite3

conn = sqlite3.connect("users.db")
c = conn.cursor()

# Create users table
c.execute("""
CREATE TABLE users (
    username TEXT PRIMARY KEY,
    password TEXT,
    email TEXT
)
""")

# Insert admin user
c.execute("""
INSERT INTO users VALUES (?, ?, ?)
""", ("admin", "password", "admin@example.com"))

conn.commit()
conn.close()

print("Database created successfully.")
