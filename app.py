from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        return render_template("index.html",postBoolean = "false")
    else: #post
        postTitle = request.args.get("title")
        postText = request.args.get("posttxt")
        
        return render_template("index.html",postBoolean = "true")
    
    
#@app.route("/post/<blog_post>",methods=["POST", "GET"])
#def blogPage():
 #   if 

if __name__ == "__main__":
    app.debug=True
    app.run();
