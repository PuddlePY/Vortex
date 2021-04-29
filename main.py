from flask import Flask, render_template, url_for, request, redirect 
import os
import time
import sqlite3
#imports



current = os.path.dirname(os.path.abspath(__file__))


#flask app
app = Flask(__name__)




#app routes

#


@app.route("/login", methods=['GET', 'POST'])
def login():
    UN = request.form["username"]
    PW = request.form["password"]


    sqlconnection = sqlite3.Connection(current + "/login.db")
    cursor = sqlconnection.cursor()
    quer1 = "SELECT username, Password from User WHERE Username = {un} AND Password = {pw}".formation(un = UN, pw = PW)
    rows = cursor.execute(query1)
    rows = rows.fetchall()
    if len(rows) ==1:
        return render_template("loggedin.html")
    else:
        return redirect("/register")


@app.route("/register", methods=["GET", "POST"])
def reg():
    if request.method == "POST":
        dUN = request.form["DUsername"]
        dPW = request.form["Dpassword"]
        Uemail = request.form["Emaluser"]
        sqlconnection = sqlite3.Connection(current + "/login.db")
        cursor = sqlconnection.cursor()
        query1 = "INSERT INTO User VAULES('{u},'{p}','{a}')".format(u = dUN, p = dPW, e = Uemail )
        cursor.execute(query1)
        sqlconnect.commit()
        return redirect("/")
    return render_template("register.html")




@app.route("/", methods=['GET', 'POST'])

@app.route("/base", methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route("/aboutus")
def about():
    return render_template("about.html")



@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/podcasts")
def podcasts():
    return render_template("podcast.html")








@app.route("/blogs")
def blog():
    return render_template("blog.html")



@app.route("/tc")
def tc():
    return render_template("tc.html")

@app.route("/navi")
def navi():
    return render_template("navi.html")


@app.route("/polls")
def poll():
    return render_template("polls.html")


@app.route("/forums")
def forum():
    return render_template("forums.html")


@app.route("/profile")
def pro():
    return render_template("profile.html")














if __name__ == "__main__":
    app.run(debug=True)
