from flask import Flask,redirect,url_for,render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "WHATTHEFKISASECRETKEY?"
app.permanent_session_lifetime = timedelta(days=5)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["fn"]
        lname = request.form["ln"]
        age = request.form["age"]
        job = request.form["job"]
        session["user"] = user
        session["lname"] = lname
        session["age"] = age
        session["job"] = job
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        
        return render_template("login.html")
    

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        lname = session["lname"]
        age = session["age"]
        job = session["job"]
        return f"<h1>Greetings! {user} {lname}, You are logged in! your age is {age}, your job is {job}</h1>"
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))



if __name__ == "__main__":
    app.run(debug=True)