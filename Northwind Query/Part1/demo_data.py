import sqlite3


# Open a connection to a new database file
conn = sqlite3.connect('demo_data.sqlite3')
c = conn.cursor()

# Create the 'demo' table
c.execute('''CREATE TABLE demo (
                s TEXT,
                x INTEGER,
                y INTEGER
            )''')

# Insert data into the 'demo' table
data = [('g', 3, 9),
        ('v', 5, 7),
        ('f', 8, 7)]

c.executemany('INSERT INTO demo VALUES (?, ?, ?)', data)

# Commit the changes and close the connection
conn.commit()
conn.close()

# Open a new connection to the existing database file
conn = sqlite3.connect('demo_data.sqlite3')
c = conn.cursor()

# How many rows are in the table?
c.execute('SELECT COUNT(*) FROM demo')
row_count = c.fetchall()

# How many rows are there where both x and y are at least 5?
c.execute('SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5')
xy_at_least_5 = c.fetchall()

# How many unique values of y are there?
c.execute('SELECT COUNT(DISTINCT y) FROM demo')
unique_y = c.fetchall()

# Print the results
print("Row count:", row_count)
print("xy at least 5 count:", xy_at_least_5)
print("Unique values of y:", unique_y)

# Close the connection
conn.close()
