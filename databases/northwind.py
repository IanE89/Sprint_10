import sqlite3

# Connect to the Northwind database
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# Query: Ten most expensive items
expensive_items = """
SELECT *
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
"""

# Execute the query
# curs.execute(expensive_items_query).fetchall()

# Query: Average age of employee at the time of hiring
avg_hire_age = """
SELECT AVG(HireDate - BirthDate) AS avg_hire_age
FROM Employee;
"""
# Execute the query
# curs.execute(avg_hire_age_query).fetchall()

# Query: Ten most expensive items and their suppliers
ten_most_expensive = """
SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName
FROM Product
INNER JOIN Supplier ON Product.SupplierId = Supplier.Id
ORDER BY Product.UnitPrice DESC
LIMIT 10;
"""
# Execute the query
# curs.execute(ten_most_expensive_query).fetchall()

# Query: Largest category by number of unique products
largest_category = """
SELECT Category.CategoryName, COUNT(DISTINCT Product.Id) AS num_products
FROM Category
INNER JOIN Product ON Category.Id = Product.CategoryId
GROUP BY Category.Id
ORDER BY num_products DESC
LIMIT 1;
"""
# Execute the query
# curs.execute(largest_category_query).fetchall()

# Close the connection
conn.close()
