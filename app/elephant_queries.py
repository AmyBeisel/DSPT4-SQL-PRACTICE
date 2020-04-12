
#app/elephant_queries.py


import os
from dotenv import load_dotenv
import psycopg2

load_dotenv() #> loads contents of the .env file into the script's environment

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")


conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print(type(conn)) #>

curs = conn.cursor()
print(type(curs)) #>

query = "SELECT * from test_table;"

# curs.execute(query)
# results = curs.fetchone()
# print(type(results))
# print(results)

curs.execute(query)
results = curs.fetchall()
print(type(results))
print(results)