import sqlite3
import csv
conn = sqlite3.connect("test.db")

c = conn.cursor()

c.execute("drop table posts")

c.execute("drop table comments")

q = "CREATE TABLE posts(title text, post text, id integer)"

result = c.execute(q)

q = "CREATE TABLE comments(comment text, id integer)"

result = c.execute(q)

BASE="insert into posts values('%(title)s','%(post)s',%(id)s)"
for line in csv.DictReader(open("posts.csv")):
    q = BASE%line
    print q
    c.execute(q)


BASE="insert into comments values('%(comment)s',%(id)s)"
for line in csv.DictReader(open("comments.csv")):
    q = BASE%line
    print q
    c.execute(q)

conn.commit()
