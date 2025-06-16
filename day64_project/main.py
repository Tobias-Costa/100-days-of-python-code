from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
import requests
import os

load_dotenv()

# Autenticação para API TMDB
HEADERS = {
        "accept": "application/json",
        "Authorization": os.environ["TOKEN"]
    } 

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]
Bootstrap5(app)

# ORM base
class Base(DeclarativeBase):
    pass

# DB config
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Formulário de avaliação
class RateMovieForm(FlaskForm):
    rating = StringField(label="Your rating out 10. E.g. 8.5", validators=[DataRequired()])
    review = StringField(label="Your review", validators=[DataRequired()])
    submit = SubmitField(label="Done")

# Formulário de adição
class AddMovie(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")

# Criação da tabela Movie(model)
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

# Home: leitura e ordenação por rating
@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()

    for index in range(len(all_movies)):
        all_movies[index].ranking = len(all_movies) - index
    db.session.commit()

    return render_template("index.html", movies=all_movies)

# Edição de avaliação
@app.route("/edit", methods=["GET","POST"])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get("id") #Get id from the movie selected to edit
    movie_selected = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        new_rating = form.rating.data
        new_review = form.review.data
        movie_selected.rating = float(new_rating)
        movie_selected.review = new_review
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie_selected, form=form)

# Exclusão de registros
@app.route("/delete")
def delete():
    movie_id = request.args.get("id") #Get id from the movie selected to delete
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

# Inserção a partir da API
@app.route("/add")
def add():
    movie_id = request.args.get("movie_id")
    movie_details = get_movie_details_api(movie_id)
    new_movie = Movie(
        title=movie_details["title"],
        year=movie_details["release_date"].split("-")[0],
        description=movie_details["overview"],
        img_url=f"https://image.tmdb.org/t/p/original/{movie_details['poster_path']}",
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("edit", id=new_movie.id))

# Busca na API
@app.route("/find", methods=["GET","POST"])
def find_movie():
    form = AddMovie()
    if form.validate_on_submit():
        movie_title = form.title.data
        list_of_movies = get_movies_by_title_api(movie_title)
        return render_template("select.html", movies=list_of_movies)        
    return render_template("add.html", form=form)

# Integração com TMDB - busca por título
def get_movies_by_title_api(movie_title):
    url = "https://api.themoviedb.org/3/search/movie"

    params = {
        "query": movie_title
    }

    response = requests.get(url, headers=HEADERS, params=params).json()
    return response["results"]

# Integração com TMDB - detalhes
def get_movie_details_api(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    response = requests.get(url, headers=HEADERS).json()
    return response

# Bootstrap + ORM setup
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True)