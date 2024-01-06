# import a modules (this one is a basic database)
import sqlite3

# how to load data as object into the database 
class Person: 
    def __init__(self, id_number = -1, first = '' , last = '', age = -1):
        self.id_number = id_number 
        self.first = first 
        self.last = last 
        self.age = age
        self.connection = sqlite3.connect('myfirst.db') 
        self.cursor = self.connection.cursor()
 

        # working with a offline file database not connect to online 

# specifiying the connection between the sql database 
    # using the methid connect
        # self.connection = sqlite3.connect('myfirst.db')
        #  cursor is allowing more or less the object or the interface 
        # self.cursor = self.connection.cursor()
    def load_person(self, id_number):
        cursor.execute("""
        SELECT*FROM persons
        WHERE id = {}
        """.format(id_number))

        results = self.cursor.fetchone()

        self.id_number = id_number 
        self.first = results[1]
        self.last = results[2]
        self.age  = results[3]

    def insert_person(self):
        self.cursor.execute("""
        INSERT INTO persons VALUES 
        ({}, '{}', '{}', {})               
        """.format(self.id_number, self.first, self.last, self.age))
        
        self.connection.commit()
        self.connection.close()

p1 = Person( 7, 'Alex', 'Robin', 30)
p1.insert_person()


connection = sqlite3.connect('myfirst.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM persons")
results = cursor.fetchall()
print(results)

connection.close

 #    creating table and loading data
'''
connection = sqlite3.connect('myfirst.db')
cursor = connection.cursor()

# creating a new table 
        # if not exists is to make sure your not duplicating any queries 
cursor.execute("""
CREATE TABLE  IF NOT EXISTS persons (
                                                     
               id INTERGER PRIMARY KEY,     
               first_name TEXT,
               last_name TEXT,
               age INTEGER
)
""")

# putting values into the table 

cursor.execute("""
        INSERT INTO persons VALUES 
            (1,'Paul', 'Smith', 24),
            (2,'Mark', 'Johnson', 42),
            (3,'Anna', 'Smith', 34)

""")



# to see results your going to use the select query like sql for printing 
cursor.execute("""
SELECT * FROM persons
    WHERE last_name= 'Smith'
""")

rows = cursor.fetchall()
print(rows)
# must commit to see results after running 
    # when running the first time you will get error 
connection.commit()

connection.close()
'''