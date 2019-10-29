import os
import csv
import psycopg2
conn = psycopg2.connect("host=localhost dbname=book user=postgres password=root")
cur = conn.cursor()

with open("books.csv", 'r') as f:
  reader = csv.reader(f)
  next(reader)
  for row in reader:
    cur.execute("INSERT INTO books (isbn, title, author, year) VALUES (%s, %s, %s, %s)",(row[0],row[1],row[2], int(row[3])))
  conn.commit()
