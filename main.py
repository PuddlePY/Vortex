from flask import Flask, render_template
import os
#imports



#flask app
app = Flask(__name__)




#app routes
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/aboutus")
def about():
    return render_template("about.html")



@app.route("/form")
def form():
    return render_template("form.html")









@app.route("/blogs")
def blog():
    return render_template("blog.html")



@app.route("/tc")
def tc():
    return render_template("tc.html")




    










if __name__ == "__main__":
    app.run(debug=True)
