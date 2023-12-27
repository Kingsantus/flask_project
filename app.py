from flask import Flask, render_template, request

app = Flask(__name__)

"""@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index1.html')
    elif request.method == "POST":
        return render_template("greet.html", name=request.form.get("name", "World"))"""

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    return render_template("success.html")