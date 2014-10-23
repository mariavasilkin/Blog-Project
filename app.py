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
        dic = {"key1":"value1","key2":"value2","key3":"value3"}
        #dic is just for testing so yeah
        if request.method == "GET":
                return render_template("index.html",dic=dic,postBoolean = False)
        else: #post
                postTitle = request.args.get("title")
                postText = request.args.get("posttxt")
                q = "insert into posts values(" + postTitle + ", " + postText + ", 0)"
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
                q = "insert into posts values(" + comment + ", " + post.id + ", 0)"
                c.execute(q)
                conn.commit()
                return render_template("post.hmtl",title=title)

if __name__ == "__main__":
    app.debug=True
    app.run();
