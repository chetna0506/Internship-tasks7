import sqlite3

# Connect (or create) database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Insertng data
data = [
    ('Apples', 10, 0.5),
    ('Oranges', 5, 0.7),
    ('Apples', 15, 0.5),
    ('Bananas', 20, 0.3),
    ('Oranges', 10, 0.7),
    ('Bananas', 5, 0.3)
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", data)
conn.commit()
conn.close()
