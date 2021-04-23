from flask import Flask, render_template, url_for
import os
import time
#imports






#flask app
app = Flask(__name__)




#app routes

#





@app.route("/", methods=['GET', 'POST'])
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
