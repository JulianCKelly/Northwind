import sqlite3


# Connect to the Northwind database
conn = sqlite3.connect('northwind_small.sqlite3')
c = conn.cursor()

# Query 1: Expensive items
EXPENSIVE_ITEMS_QUERY = '''
    SELECT *
    FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10
'''

# Query 2: Average age at the time of hiring
AVG_HIRE_AGE_QUERY = '''
    SELECT AVG(HireDate - BirthDate) AS AvgHireAge
    FROM Employee
'''

# Save the queries to the specified variables
expensive_items = EXPENSIVE_ITEMS_QUERY
avg_hire_age = AVG_HIRE_AGE_QUERY


# Query 3: Ten most expensive items with suppliers
TEN_MOST_EXPENSIVE_QUERY = '''
    SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName
    FROM Product
    JOIN Supplier ON Product.SupplierId = Supplier.Id
    ORDER BY Product.UnitPrice DESC
    LIMIT 10
'''

# Query 4: Largest category by number of unique products
LARGEST_CATEGORY_QUERY = '''
    SELECT Category.CategoryName, COUNT(DISTINCT Product.Id) AS UniqueProducts
    FROM Category
    JOIN Product ON Category.Id = Product.CategoryId
    GROUP BY Category.Id
    ORDER BY UniqueProducts DESC
    LIMIT 1
'''

# Save the queries to the specified variables
ten_most_expensive = TEN_MOST_EXPENSIVE_QUERY
largest_category = LARGEST_CATEGORY_QUERY


# Close the connection
conn.close()


# Print the queries for reference
print(expensive_items)
print(avg_hire_age)
print(ten_most_expensive)
print(largest_category)
