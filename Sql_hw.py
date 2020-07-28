# Download this database: Chinook.sqlite
from smartninja_sql.sqlite import SQLiteDatabase
db = SQLiteDatabase("Chinook_Sqlite.sqlite")

db.print_tables(verbose=True)

# This database has many tables. Write an SQL command that will print Name from the table Artist (for all the database entries)
db.pretty_print("SELECT Name from Artist;")

# Print all data from the table Invoice where BillingCountry is Germany
db.pretty_print("SELECT * FROM Invoice WHERE BillingCountry = 'Germany';")

# Count how many albums are in the database. Look into the SQL documentation for help. Hint: look for Min&Max and Count, Avg, Sum.
db.pretty_print("SELECT COUNT(*) AS 'COUNT' FROM Album;")

# How many customers are from France?
result= db.execute("SELECT COUNT(*) FROM Customer WHERE Country = 'France';")
print(result)