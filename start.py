import sqlite3

conn = sqlite3.connect("test.db")

c = conn.cursor()

q = "CREATE TABLE posts(title text, post text, id integer)"

result = c.execute(q)

q = "CREATE TABLE comments(comment text, postid text, commentid integer)"

result = c.execute(q)

conn.commit()
