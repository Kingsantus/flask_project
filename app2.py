import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

conn = sqlite3.connect("flask_project.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS registers(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               sport TEXT
)""")

#REGISTERS = {}

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

@app.route('/deregister', methods=["POST"])
def deregister():
    #forget register
    id = request.form.get("id")
    if id:
        cursor.execute("DELETE FROM registers WHERE id = ?", id)
    return redirect("/registers")


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")
    if not name or sport not in SPORTS:
        return render_template('failure.html')
    #REGISTERS[name] = sport
    cursor.execute("INSERT INTO registers(name, sport) VALUES(?, ?)", (name, sport))
    conn.commit()
    return redirect('/registers')


@app.route("/registers")
def registers():
    cursor.execute("SELECT * FROM registers")
    registers = cursor.fetchall()
    return render_template("registers.html", registers=registers)


conn.close()