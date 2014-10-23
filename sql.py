import sqlite3
import csv
conn = sqlite3.connect("test.db")

c = conn.cursor()

c.execute("drop table posts")

c.execute("drop table comments")

q = "CREATE TABLE posts(title text, post text, id integer)"

result = c.execute(q)

q = "CREATE TABLE comments(comment text, postid integer, commentid integer)"

result = c.execute(q)

q = "insert into posts values('%(post)s',%(id)s)"

q = "insert into comments values('%(comment)s',%(id)s)"

p = "SELECT postTitle, postText FROM posts"

conn.commit()
