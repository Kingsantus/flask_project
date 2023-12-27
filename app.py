import sqlite3
from flask import Flask, render_template, request, redirect, g

app = Flask(__name__)
DATABASE = "flask_project.db"

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS registers (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          name TEXT,
                          sport TEXT
                      )""")
        db.commit()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    sports = ["Basketball", "Soccer", "Ultimate Frisbee"]
    return render_template("index.html", sports=sports)

@app.route('/deregister', methods=["POST"])
def deregister():
    with get_db() as conn:
        id = request.form.get("id")
        if id:
            conn.execute("DELETE FROM registers WHERE id = ?", (id,))
            conn.commit()
    return redirect("/registers")

@app.route("/register", methods=["POST"])
def register():
    with get_db() as conn:
        name = request.form.get("name")
        sport = request.form.get("sport")
        if not name or sport not in ["Basketball", "Soccer", "Ultimate Frisbee"]:
            return render_template('failure.html')
        
        conn.execute("INSERT INTO registers(name, sport) VALUES(?, ?)", (name, sport))
        conn.commit()
    return redirect('/registers')

@app.route("/registers")
def registers():
    with get_db() as conn:
        registers = conn.execute("SELECT * FROM registers").fetchall()
        print(registers)
    return render_template("registers.html", registers=registers)

# Initialize the database when the app starts
init_db()
