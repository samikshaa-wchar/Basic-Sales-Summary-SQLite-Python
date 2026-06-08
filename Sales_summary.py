import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Insert sample data
cursor.execute("DELETE FROM sales")

sales_data = [
    ('Laptop', 5, 50000),
    ('Mouse', 20, 500),
    ('Keyboard', 10, 1200),
    ('Laptop', 3, 50000),
    ('Mouse', 15, 500)
]

cursor.executemany(
    "INSERT INTO sales VALUES (?, ?, ?)",
    sales_data
)

conn.commit()

# SQL Query
query = """
SELECT
    product,
    SUM(quantity) AS total_qty,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""

df = pd.read_sql_query(query, conn)

print("Sales Summary")
print(df)

# Bar Chart
df.plot(
    kind='bar',
    x='product',
    y='revenue',
    legend=False
)

plt.title("Revenue by Product")
plt.ylabel("Revenue")
plt.tight_layout()

plt.savefig("sales_chart.png")
plt.show()

conn.close()
