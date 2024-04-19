from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h2>Karan Shah</h2>"

@app.route("/about")
def about():
    return "<h2>Hello I am Karan</h2>"

if __name__ == "__main__":
    app.run(debug=True)