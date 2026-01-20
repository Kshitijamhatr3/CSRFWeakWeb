from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "insecure-secret-key"

# LAB CONFIG (INTENTIONALLY INSECURE)
app.config.update(
    SESSION_COOKIE_SAMESITE=None,
    SESSION_COOKIE_SECURE=False
)

# Database helper
def get_db():
    return sqlite3.connect(
        "users.db",
        timeout=10,
        check_same_thread=False
    )

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    error = None
    if request.method == "POST":
        try:
            conn = get_db()
            c = conn.cursor()
            c.execute(
                "INSERT INTO users VALUES (?, ?, ?)",
                (
                    request.form["username"],
                    request.form["password"],
                    request.form["email"]
                )
            )
            conn.commit()
            conn.close()
            return redirect("/login")
        except sqlite3.IntegrityError:
            error = "Username already exists"

    return render_template("signup.html", error=error)

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        conn = get_db()
        c = conn.cursor()
        c.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (request.form["username"], request.form["password"])
        )
        user = c.fetchone()
        conn.close()

        if user:
            session["username"] = user[0]
            return redirect("/profile")
        else:
            error = "Invalid credentials"

    return render_template("login.html", error=error)

@app.route("/profile")
def profile():
    if "username" not in session:
        return redirect("/login")

    conn = get_db()
    c = conn.cursor()
    c.execute(
        "SELECT email FROM users WHERE username=?",
        (session["username"],)
    )
    email = c.fetchone()[0]
    conn.close()

    return render_template(
        "profile.html", 
        username=session["username"],
        email=email)

# 🚨 CSRF VULNERABLE ENDPOINT
@app.route("/change-email", methods=["GET", "POST"])
def change_email():
    if "username" not in session:
        return redirect("/login")

    # GET → CSRF attack path
    if request.method == "GET":
        email = request.args.get("email")

    # POST → Legit user action
    else:
        email = request.form.get("email")

    if not email:
        return "Email parameter missing", 400

    conn = get_db()
    c = conn.cursor()
    c.execute(
        "UPDATE users SET email=? WHERE username=?",
        (email, session["username"])
    )
    conn.commit()
    conn.close()

    return redirect("/profile")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
