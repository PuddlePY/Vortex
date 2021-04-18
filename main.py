from flask import Flask, render_template
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







if __name__ == "__main__":
    app.run(debug=True)