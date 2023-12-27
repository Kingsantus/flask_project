from flask import Flask, render_template, request

app = Flask(__name__)

REGISTERS = {}

SPORTS = [
    "Basketball",
    "Soccer",
    "Ultimate Frisbee"
]

"""@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index1.html')
    elif request.method == "POST":
        return render_template("greet.html", name=request.form.get("name", "World"))"""

@app.route('/')
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    if not name:
        return render_template('failure.html')
    sport = request.form.get("sport")
    if sport not in SPORTS:
        return render_template('failure.html')
    REGISTERS[name] = sport
    return render_template("success.html")


@app.route("/registers")
def registers():
    return render_template("registers.html", registers=REGISTERS)