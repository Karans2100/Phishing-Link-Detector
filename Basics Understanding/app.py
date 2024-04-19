from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

#Returns the root directory with the return statement in it
@app.route("/")
def index():
    return render_template("index.html", content="Testing")

@app.route("/login/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>/")
def user(usr):
    return f"<h1>Hello {usr}</h1>"

#Dynamically creating webpages as you search
# @app.route("/<name>/")
# def user(name):
#     return f"Hello {name}"

#Rendering variable in python file to html file
# @app.route("/<name>/")
# def user(name):
#     return render_template("index.html", content=name, r=2)

# @app.route("/admin/")
# def admin():
#     return redirect(url_for("index"))

app.run(debug=True)