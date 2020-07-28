from smartninja_sql.sqlite import SQLiteDatabase
db = SQLiteDatabase("Student.sqlite")

db.execute("CREATE TABLE IF NOT EXISTS Student (id integer primary key autoincrement, name text, grade text);")

#db.execute("INSERT INTO Student(name, grade) VALUES ('TEENA', 'A');")
#db.execute("INSERT INTO Student(name, grade) VALUES ('ETHAN', 'A');")

#result= db.execute("SELECT * FROM Student;")
#print(result)

#db.execute("UPDATE Student SET grade='A+' WHERE id=2;")

#db.execute("ALTER TABLE Student ADD age text;")

#db.execute("UPDATE Student SET age=20 WHERE id=2;")

db.execute("DROP TABLE Student;")

db.pretty_print("SELECT * FROM Student;")

db.print_tables(verbose=True)