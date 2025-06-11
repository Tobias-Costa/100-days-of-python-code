from flask import Flask, render_template, request
from dotenv import load_dotenv
import requests
import smtplib
import os

load_dotenv()

ADDR_EMAIL = os.environ["ADDR_EMAIL"]
EMAIL_PASSWORD = os.environ["EMAIL_PASSWORD"]

posts = requests.get("https://api.npoint.io/fd8aaa19feac34e202b6").json()

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        msg = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        send_email(msg, email)

        return render_template("contact.html", info="Successfully sent your message")
    else:
        return render_template("contact.html")

def send_email(msg, email):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(ADDR_EMAIL, EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=ADDR_EMAIL, to_addrs=email, msg=f"Subject: Contact Blog Confirmation\n\n{msg}".encode("utf-8")
        )

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
