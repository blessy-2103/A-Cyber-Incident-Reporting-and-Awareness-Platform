
from flask import Flask, render_template, request, redirect, session, flash, jsonify
import sqlite3
import os
DATABASE = os.path.join(os.getcwd(), "database.db")
app = Flask(__name__)

app.secret_key = "secretkey"

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

    # Incidents table
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
        status TEXT DEFAULT 'Open'
    )
    """)

    # Default admin
    cursor.execute("""
    INSERT OR IGNORE INTO users(name,email,password,role)
    VALUES('Admin','admin@gmail.com','admin123','admin')
    """)

    conn.commit()
    conn.close()

# -------------------- HOME / INDEX --------------------
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
    return render_template(
        "index.html",
        total_incidents=total_incidents,
        open_incidents=open_incidents,
        resolved_incidents=resolved_incidents
    )

# -------------------- LOGIN --------------------
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
            session["user"] = user[2]      # email
            session["role"] = user[4]      # role
            return redirect("/admin_dashboard") if user[4] == "admin" else redirect("/")
        else:
            flash("Invalid Credentials")
            return redirect("/login")
    return render_template("login.html")

# -------------------- REGISTER --------------------
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
            flash("Registration Successful! Please login.")
            return redirect("/login")
        except sqlite3.IntegrityError:
            flash("Email already exists!")
            return redirect("/register")
    return render_template("register.html")

# -------------------- REPORT INCIDENT --------------------
@app.route("/report", methods=["GET","POST"])
def report():
    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":
        incident_type = request.form["incident_type"]
        title = request.form["title"]
        incident_date = request.form["incident_date"]
        severity = request.form["severity"]
        affected_system = request.form["affected_system"]
        reporter = request.form["reporter"]
        description = request.form["description"]

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO incidents(incident_type,title,incident_date,severity,affected_system,reporter,description)
            VALUES (?,?,?,?,?,?,?)
        """, (incident_type,title,incident_date,severity,affected_system,reporter,description))
        conn.commit()
        conn.close()

        flash("Incident Report Submitted Successfully!")
        return redirect("/dashboard")
    return render_template("report.html")

# -------------------- USER DASHBOARD --------------------
@app.route("/dashboard", methods=["GET","POST"])
def dashboard():
    if "user" not in session:
        return redirect("/login")

    query = "SELECT * FROM incidents"
    search_term = ""

    if request.method == "POST":
        search_term = request.form.get("search")
        query += " WHERE title LIKE ? OR incident_type LIKE ? OR reporter LIKE ?"
        params = ('%'+search_term+'%','%'+search_term+'%','%'+search_term+'%')
    else:
        params = ()

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query, params) if params else cursor.execute(query)
    incidents = cursor.fetchall()
    conn.close()

    return render_template("dashboard.html", incidents=incidents, search_term=search_term)

# -------------------- ADMIN DASHBOARD --------------------
@app.route("/admin_dashboard", methods=["GET","POST"])
def admin_dashboard():

    if "user" not in session or session.get("role") != "admin":
        return redirect("/login")

    query = "SELECT * FROM incidents"
    search_term = ""

    if request.method == "POST":
        search_term = request.form.get("search")
        query += " WHERE title LIKE ? OR incident_type LIKE ? OR reporter LIKE ?"
        params = ('%'+search_term+'%','%'+search_term+'%','%'+search_term+'%')
    else:
        params = ()

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # INCIDENT TABLE
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)

    incidents = cursor.fetchall()

    # ----------------------------
    # SEVERITY STATISTICS
    # ----------------------------
    cursor.execute("SELECT severity, COUNT(*) FROM incidents GROUP BY severity")
    stats = cursor.fetchall()

    severity_counts = {
        "Low":0,
        "Medium":0,
        "High":0,
        "Critical":0
    }

    for row in stats:
        severity_counts[row[0]] = row[1]

    # ----------------------------
    # STATUS STATISTICS
    # ----------------------------
    cursor.execute("SELECT status, COUNT(*) FROM incidents GROUP BY status")
    status_stats = cursor.fetchall()

    status_counts = {
        "Open":0,
        "Investigating":0,
        "Resolved":0
    }

    for row in status_stats:
        status_counts[row[0]] = row[1]

    # ----------------------------
    # ATTACK TYPE STATISTICS
    # ----------------------------
    cursor.execute("SELECT incident_type, COUNT(*) FROM incidents GROUP BY incident_type")
    attack_stats = cursor.fetchall()

    attack_counts = {}

    for row in attack_stats:
        attack_counts[row[0]] = row[1]

    conn.close()

    return render_template(
        "admin_dashboard.html",
        incidents=incidents,
        search_term=search_term,
        severity_counts=severity_counts,
        status_counts=status_counts,
        attack_counts=attack_counts
    )
# -------------------- UPDATE STATUS --------------------
@app.route("/update_status/<int:id>", methods=["POST"])
def update_status(id):
    status = request.form["status"]
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("UPDATE incidents SET status=? WHERE id=?", (status,id))
    conn.commit()
    conn.close()
    return redirect("/admin_dashboard")

# -------------------- CYBER AWARENESS --------------------
@app.route("/awareness")
def awareness():
    if "user" not in session:
        return redirect("/login")
    return render_template("awareness.html")

# -------------------- LOGOUT --------------------
@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("role", None)
    return redirect("/login")
#-------------------detection of phishng-----------
def detect_phishing(message):
    phishing_keywords = [
        "urgent",
        "verify your account",
        "bank",
        "password",
        "otp",
        "click here",
        "login now",
        "limited time",
        "suspended",
        "update your account"
    ]

    score = 0
    message = message.lower()

    for word in phishing_keywords:
        if word in message:
            score += 1

    if score >= 3:
        return "⚠️ This message looks like a PHISHING attempt. Do not click links or share personal details."
    elif score == 2:
        return "⚠️ This message is suspicious. Verify the sender before taking action."
    else:
        return "✅ This message appears safe, but always stay cautious."

# -------------------- AI CHATBOT --------------------
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_msg = data.get("message", "").lower().strip()

        responses = {
            "phishing": "Phishing is a cyber attack where attackers send fake emails or messages pretending to be trusted organizations to steal passwords, bank details, or OTP.",
            
            "malware": "Malware is malicious software designed to damage computers, steal information, or spy on users. Examples include viruses, trojans, and ransomware.",
            
            "ransomware": "Ransomware is a type of malware that locks your files and demands payment to restore access.",
            
            "hacked": "If your account is hacked, immediately change your password, enable two-factor authentication, and review recent activity.",
            
            "scam": "Online scams usually involve fake calls, messages, or websites asking for money or personal information.",
            
            "otp": "Never share your OTP with anyone. Banks or official services will never ask for OTP through calls or messages.",
            
            "password": "Use strong passwords with letters, numbers, and symbols. Avoid using the same password for multiple accounts."
        }

        if user_msg in ["hi", "hello", "hey"]:
            reply = "Hello! 👋 I am your Cybersecurity Assistant. Ask me about phishing, malware, scams, or online safety."

        else:
            reply = None
            for keyword in responses:
                if keyword in user_msg:
                    reply = responses[keyword]
                    break

            if not reply:
                reply = "I can help with cybersecurity topics like phishing, malware, scams, password safety, and account protection."

        return jsonify({"reply": reply})

    except Exception as e:
        print("Chatbot error:", e)
        return jsonify({"reply": "Something went wrong"})
# -------------------- RUN APP --------------------
if __name__ == "__main__":
    init_db()
    app.run()