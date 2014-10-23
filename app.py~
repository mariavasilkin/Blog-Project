from flask import Flask, render_template, request

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

conn.commit()

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        return render_template("index.html",postBoolean = False)
    else: #post
        postTitle = request.args.get("title")
        postText = request.args.get("posttxt")
        q = "insert into posts values(" + postTitle + ", " + postText + ", 0)"
        c.execute(q)
        conn.commit()
        return render_template("index.html",postBoolean = True)
    
    
#@app.route("/post/<blog_post>",methods=["POST", "GET"])
#def blogPage():
 #   if 

if __name__ == "__main__":
    app.debug=True
    app.run();
