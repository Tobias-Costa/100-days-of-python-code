from flask import Flask, render_template
import requests

POSTS_URL = "https://api.npoint.io/c790b4d5cab58020d391"
posts = requests.get(POSTS_URL).json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route('/read/<int:id>')
def read_more(id):
    return render_template("post.html", id=id, posts=posts)

if __name__ == "__main__":
    app.run()
