# Importação dos pacotes Flask e SQLAlchemy para criação da aplicação web com banco de dados relacional
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# Inicialização da aplicação Flask
app = Flask(__name__)

# Definição da base declarativa para o SQLAlchemy
class Base(DeclarativeBase):
    pass

# Criação do objeto de banco de dados SQLAlchemy, associando-o ao modelo Base
db = SQLAlchemy(model_class=Base)

# Configuração do banco de dados SQLite (arquivo local)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# Inicialização do SQLAlchemy com a aplicação Flask
db.init_app(app)

# Definição da tabela 'Book' usando ORM (Object-Relational Mapping)
class Book(db.Model):
    # Campo de ID (chave primária, inteiro, autoincrementado)
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Título do livro (único e obrigatório, até 250 caracteres)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    # Nome do autor (obrigatório)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    # Nota de avaliação do livro (float, obrigatório)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

# Rota principal: exibe a lista de livros cadastrados ordenados por título
@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template("index.html", all_books=all_books)

@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # Cria um novo objeto Book com os dados submetidos via formulário
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"])
        # Adiciona o novo livro na sessão e grava no banco
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")

@app.route("/edit", methods=["GET","POST"])
def edit():
    if request.method == "POST":
        # Recupera o livro a ser atualizado pelo ID passado no formulário
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Book, book_id)
        # Atualiza o rating com o novo valor
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("home"))
    # Se for GET, recupera o ID passado pela URL (query string)
    book_id = request.args.get("id")
    book_selected = db.get_or_404(Book, book_id)
    return render_template("edit_rating.html", book=book_selected)

@app.route("/delete")
def delete():
    # Recupera o livro a ser deletado pelo ID passado na query string
    book_id = request.args.get("id")
    book_to_delete =  db.get_or_404(Book, book_id)
    # Remove o registro do banco e confirma a transação
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    # Cria as tabelas no banco de dados (se ainda não existirem)
    with app.app_context():
        db.create_all()
    app.run(debug=True)

