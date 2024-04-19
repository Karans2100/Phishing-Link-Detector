from flask import Flask, render_template, request
from ExtractingFeatures import urlFeatures
from phishing_model import model

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        URL = request.form["url"]
        characteristics = urlFeatures(URL)
        result = model.predict(characteristics)
        if result == 0:
            font_color = "rgb(35, 217, 35)"
            return render_template("result.html", result="Link is safe to use", font_color=font_color, URL=URL)
        else:
            font_color = "rgb(240, 19, 19)"
            return render_template("result.html", result="Link is unsafe", font_color=font_color, URL=URL)
    else:
        return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)