from flask import Flask, render_template, request

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

conn.commit()

app = Flask(__name__)

result = c.execute("SELECT title FROM posts")
for row in result:
        print row

@app.route("/", methods=["POST", "GET"])
def home():
        dic = c.execute("SELECT title FROM posts")
        #dic is just for testing so yeah
        if request.method == "GET":
                return render_template("index.html",thing=thing, postBoolean = False)
        else: #post
                postTitle = request.args.get("title")
                postText = request.args.get("posttxt")
                i=0
                q = "insert into posts values(" + postTitle + ", " + postText + ", i)"
                i=i+1
                c.execute(q)
                conn.commit()
                return render_template("index.html",postBoolean = True)

    
@app.route("/<title>",methods=["POST", "GET"])
def blogPage():
        if request.method == "GET":
                return render_template("post.html",title=title)
        else:#I think this should be different if you just added a comment
                comment = request.args.get("comment")
                id = request.args.get("post.id") #this may be way off
                j=0
                q = "insert into comments values(" + comment + ", " + post.id + ", j)"
                j=j+1
                c.execute(q)
                conn.commit()
                return render_template("post.hmtl",title=title)

if __name__ == "__main__":
    app.debug=True
    app.run();
