from flask import Flask, render_template, request

app = Flask(__name__)

REGISTERS = {}

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
    name = request.form.get("name")
    sport = request.form.get("sport")
    REGISTERS[name] = sport
    return render_template("success.html")


@app.route("/registers")
def registers():
    return render_template("registers.html", registers=REGISTERS)