from flask import Flask, render_template, request

import sqlite3
import csv


app = Flask(__name__)

<<<<<<< HEAD
=======
result = c.execute("SELECT title FROM posts")
for row in result:
        print row

thing = []

>>>>>>> f6954f61fc31c3469a303a6f5ce6f3c3ce90f221
@app.route("/", methods=["POST", "GET"])
def home():
        conn = sqlite3.connect("test.db")
        c = conn.cursor()
        #dic is just for testing so yeah
        if request.method == "GET":
<<<<<<< HEAD
                q = "SELECT * FROM posts"
                result = c.execute(q)
                postList = result.fetchall()
                return render_template("index.html",pl = postList)
        else: #post
                title = request.form["postTitle"]
                text = request.form["postText"]
                q = "SELECT count(*) FROM posts" 
                result = c.execute(q)
                i = str(result.fetchone()[0])
                q = "INSERT INTO posts VALUES(?,?,?)"
                c.execute(q,[title,text,i])
                conn.commit()
                q = "SELECT * FROM posts"
                result = c.execute(q)
                postList = result.fetchall()
                return render_template("index.html",pl = postList)
=======
                print thing
                if len(thing)==0:
                        print "nope"
                return render_template("index.html",thing=thing, postBoolean = False)
        else: #post
                postTitle = request.args.get("title")
                postText = request.args.get("post")
                i=0
                q = "insert into posts values(" + postTitle + ", " + postText + ", i)"
                i=i+1
                c.execute(q)
                conn.commit()
                print thing
                if len(thing) == 0:
                        print "nope"
                return render_template("index.html",postBoolean = True)
>>>>>>> f6954f61fc31c3469a303a6f5ce6f3c3ce90f221

@app.route("/run", methods=["POST", "GET"])
def run():
        i=0
        "INSERT into posts values(" + postTitle + "," + postText + "i)"
        i=i+1
        for row in result:
                thing.append(row)
                print thing
        return render_template("index.html", postBoolean=true)
    
@app.route("/<title>",methods=["POST", "GET"])
def blogPage(title):
        conn = sqlite3.connect("test.db")
        c = conn.cursor()
        if request.method == "GET":
                q = "SELECT * FROM posts WHERE title=?"
                result = c.execute(q,[title])
                p = result.fetchone()
                q = "SELECT * FROM comments WHERE postid=?"
                result = c.execute(q,[title])
                comments = result.fetchall()
                return render_template("post.html",title=title,post=p,cl=comments)
        else:
                comment = request.form["comment"]
                q = "SELECT count(*) FROM comments WHERE postid=?"
                result = c.execute(q,[title])
                i = str(result.fetchone()[0])
                q = "INSERT INTO comments VALUES(?,?,?)"
                c.execute(q,[comment,title,i])
                conn.commit()
                q = "SELECT * FROM comments WHERE postid=?"
                result = c.execute(q,[title])
                comments = result.fetchall()
                q = "SELECT * FROM posts WHERE title=?"
                result = c.execute(q,[title])
                p = result.fetchone()
                return render_template("post.html",title=title,cl = comments,post=p)

if __name__ == "__main__":
    app.debug=True
    app.run();
