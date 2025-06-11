from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5

# Classe criada para instanciar os campos que estarão presentes no formulário de login
class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log in")

app = Flask(__name__)
app.secret_key = "forms testing"
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    # Se o botão de submit for clicado então a condicional abaixo será True
    if login_form.validate_on_submit():
        user_email = login_form.email.data
        user_password = login_form.password.data
        if user_email  == "admin@email.com" and user_password == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)

if __name__ == '__main__':
    app.run(debug=True)