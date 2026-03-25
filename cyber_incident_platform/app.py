from flask import Flask, render_template, request, redirect, session, flash, jsonify
import sqlite3
import os
import re
from werkzeug.utils import secure_filename

DATABASE = os.path.join(os.getcwd(), "database.db")
UPLOAD_FOLDER = os.path.join('static', 'uploads', 'evidence')

app = Flask(__name__)
app.secret_key = "secretkey"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# -------------------- DATABASE INIT --------------------
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT,
        role TEXT DEFAULT 'user'
    )
    """)

    # Scam Alerts table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scam_alerts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        date_posted DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    cursor.execute("INSERT OR IGNORE INTO scam_alerts(title, description) VALUES (?, ?)", 
               ("New Netflix Phishing Link", "Users are receiving emails asking to 'Update Payment' via a fake netflix-verify.xyz link."))

    # Incidents table - UPDATED with evidence_path and is_anonymous
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS incidents(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        incident_type TEXT,
        title TEXT,
        incident_date TEXT,
        severity TEXT,
        affected_system TEXT,
        reporter TEXT,
        description TEXT,
        status TEXT DEFAULT 'Open',
        evidence_path TEXT,
        is_anonymous INTEGER DEFAULT 0
    )
    """)

    # Default admin
    cursor.execute("""
    INSERT OR IGNORE INTO users(name,email,password,role)
    VALUES('Admin','admin@gmail.com','admin123','admin')
    """)

    conn.commit()
    conn.close()

# -------------------- ROUTES --------------------

@app.route("/")
@app.route("/index")
def index():
    if "user" not in session:
        return redirect("/login")

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM incidents")
    total_incidents = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM incidents WHERE status='Open'")
    open_incidents = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM incidents WHERE status='Resolved'")
    resolved_incidents = cursor.fetchone()[0]
    conn.close()
    
    return render_template("index.html", total_incidents=total_incidents, 
                           open_incidents=open_incidents, resolved_incidents=resolved_incidents)

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email,password))
        user = cursor.fetchone()
        conn.close()
        if user:
            session["user"] = user[2]
            session["role"] = user[4]
            return redirect("/admin_dashboard") if user[4] == "admin" else redirect("/")
        flash("Invalid Credentials")
    return render_template("login.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        try:
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users(name,email,password) VALUES(?,?,?)", (name,email,password))
            conn.commit()
            conn.close()
            flash("Registration Successful!")
            return redirect("/login")
        except sqlite3.IntegrityError:
            flash("Email already exists!")
    return render_template("register.html")

# --- COMBINED REPORT ROUTE ---
@app.route("/report", methods=["GET","POST"])
def report():
    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":
        incident_type = request.form.get("incident_type")
        title = request.form.get("title")
        incident_date = request.form.get("incident_date")
        severity = request.form.get("severity")
        affected_system = request.form.get("affected_system")
        description = request.form.get("description")
        
        # Handle Anonymous Toggle
        is_anon = 1 if request.form.get("anonymous") == "on" else 0
        reporter = "Anonymous" if is_anon else request.form.get("reporter")

        # Handle File Upload
        file = request.files.get("evidence")
        filename = None
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO incidents(incident_type, title, incident_date, severity, affected_system, reporter, description, evidence_path, is_anonymous)
            VALUES (?,?,?,?,?,?,?,?,?)
        """, (incident_type, title, incident_date, severity, affected_system, reporter, description, filename, is_anon))
        conn.commit()
        conn.close()

        flash("Incident Report Submitted Successfully!")
        return redirect("/dashboard")
        
    return render_template("report.html")

@app.route("/dashboard", methods=["GET","POST"])
def dashboard():
    if "user" not in session:
        return redirect("/login")
    search_term = request.form.get("search", "") if request.method == "POST" else ""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    if search_term:
        cursor.execute("SELECT * FROM incidents WHERE title LIKE ? OR incident_type LIKE ?", ('%'+search_term+'%', '%'+search_term+'%'))
    else:
        cursor.execute("SELECT * FROM incidents")
    incidents = cursor.fetchall()
    conn.close()
    return render_template("dashboard.html", incidents=incidents, search_term=search_term)

@app.route("/admin_dashboard", methods=["GET","POST"])
def admin_dashboard():
    if "user" not in session or session.get("role") != "admin":
        return redirect("/login")
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM incidents")
    incidents = cursor.fetchall()
    
    # Statistics logic (simplified for brevity)
    cursor.execute("SELECT severity, COUNT(*) FROM incidents GROUP BY severity")
    severity_counts = {row[0]: row[1] for row in cursor.fetchall()}
    
    conn.close()
    return render_template("admin_dashboard.html", incidents=incidents, severity_counts=severity_counts)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "").lower().strip()
    # ... (Your existing chatbot logic) ...
    return jsonify({"reply": "I am your security assistant. How can I help?"})

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
