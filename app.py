from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    title = None
    blog_post = None
    if request.method == 'POST':
        title = request.form["title"].strip()
        blog_post = request.form["blog_post"].strip()
    if (title is not None):
        return render_template("index.html", title = title, blog_post = blog_post)

    return render_template("index.html")
@app.route("/post/<blog_post>",methods=["POST", "GET"])
def blogPage():
    if 

