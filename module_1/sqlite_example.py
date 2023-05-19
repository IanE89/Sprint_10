import sqlite3
import queries as q

# Step 1 - connect to the database
connection = sqlite3.connect('rpg_db.sqlite3')

# Step 2 - Make the "cursor"
cursor = connection.cursor()

# Step 3 - Write a query
# (See the queries.py file, moved query there)

# Step 4 - Execute the query on the cursor and fetch the results
# "pulling results" from the cursor
results = cursor.execute(q.SELECT_ALL).fetchall()

if __name__ == '__main__':
    print(results[:5])