import psycopg2

#establish connection
# conn = psycopg2.connect(
#     database_="postgres", user="sizwe", password="Siz@7834", host="127.0.0.1", port='5432'
# )

hostname = '127.0.0.1'
database = 'test_database'
username = 'postgres'
pwd = 'postgres'
port = 5432


cursor = None
conn = None

try:

    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port
    )

    cursor = conn.cursor()

    create_table = ''' CREATE TABLE IF NOT EXISTS test_employees (
    id serial primary key,
    name varchar(40) NOT NULL,
    surname varchar(40) NOT NULL,
    salary int ,
    occupation varchar(50)
    ) '''

    cursor.execute(create_table)
    conn.commit()
    print("Employee table created successfully...")

    insert_employees = ''' INSERT INTO test_employees (name, surname, salary, occupation) VALUES (%s, %s, %s, %s) '''
    values = ('Sizwe', 'Ncikana', 1234, 'Developer')

    cursor.execute(insert_employees, values)
    conn.commit()
    print("Employee Successfully Inserted into table")


except Exception as error:
    print(error)

finally:
    if cursor and conn is not None:
        # Close the cursor and connection
        cursor.close()
        conn.close()




# conn.autocommit = True
#
# #Creating a cursor object using the cursor() method
# cursor = conn.cursor()
#
# #Preparing query to create a database
# sql = ''' CREATE database eployees ''';
#
# #Creating the database
# cursor.execute(sql)
# print("Database created successfully")

