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




Photos = os.path.join('static', 'Photos')
print(Photos)
app.config['UPLOAD_FOLDER'] = Photos




@app.route("/blogs")
def blog():
    Photo1 = os.path.join(app.config['UPLOAD_FOLDER'], 'mario.png')
    return render_template("blog.html", user_image=Photo1)










if __name__ == "__main__":
    app.run(debug=True)
