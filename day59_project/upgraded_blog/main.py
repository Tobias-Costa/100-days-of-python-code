import requests
from flask import Flask, render_template

url = "https://api.npoint.io/225fc4f459004ebfe0a4"
data = requests.get(url).json()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", posts=data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:id>")
def post(id):
    for post in data:
        if post["id"] == id:
            return render_template("post.html", post=post)
    
if __name__ == "__main__":
    app.run(debug=True)