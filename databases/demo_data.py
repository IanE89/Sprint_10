import sqlite3

# Open a connection to the database
conn = sqlite3.connect('demo_data.sqlite3')

# Create a cursor to connect to
cursor = conn.cursor()

# Query: How many rows are in the table?
row_count_query = 'SELECT COUNT(*) FROM demo'
cursor.execute(row_count_query)
row_count = cursor.fetchall()

# Query: How many rows are there where both x and y are at least 5?
xy_at_least_5_query = 'SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5'
cursor.execute(xy_at_least_5_query)
xy_at_least_5 = cursor.fetchall()

# Query: How many unique values of y are there?
unique_y_query = 'SELECT COUNT(DISTINCT y) FROM demo'
cursor.execute(unique_y_query)
unique_y = cursor.fetchall()

# Close the connection
conn.close()

# Print the results
print('Row count:', row_count)
print('Rows with x and y at least 5:', xy_at_least_5)
print('Unique values of y:', unique_y)

# Assign the values to variables (outside of if __name__ == '__main__')
row_count_value = row_count[0][0]
xy_at_least_5_value = xy_at_least_5[0][0]
unique_y_value = unique_y[0][0]
