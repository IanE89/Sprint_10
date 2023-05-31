import sqlite3

# Connect to the Northwind database
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# Query: Ten most expensive items
expensive_items_query = """
SELECT *
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
"""
# Execute the query
expensive_items = curs.execute(expensive_items_query).fetchall()

# Query: Average age of employee at the time of hiring
avg_hire_age_query = """
SELECT AVG(HireDate - BirthDate) AS avg_hire_age
FROM Employee;
"""
# Execute the query
avg_hire_age = curs.execute(avg_hire_age_query).fetchall()

# Close the connection
conn.close()
