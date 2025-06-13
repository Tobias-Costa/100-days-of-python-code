# Importação dos principais pacotes do Flask e extensões
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5  # Para integrar Bootstrap 5 ao Flask (melhora o design visual sem muito código de CSS)
from flask_wtf import FlaskForm  # Extensão para criação de formulários seguros com CSRF
from wtforms import StringField, SelectField, SubmitField  # Campos do formulário
from wtforms.validators import DataRequired, URL  # Validadores de entrada
import csv  # Para manipulação de arquivos CSV (armazenamento simples dos dados)

'''
OBSERVAÇÃO:
Se aparecerem linhas vermelhas no editor (dependência não encontrada), 
executar o seguinte comando no terminal do projeto para instalar as bibliotecas necessárias:

No Windows:
python -m pip install -r requirements.txt

No MacOS/Linux:
pip3 install -r requirements.txt
'''

# Criação da aplicação Flask
app = Flask(__name__)
# Chave secreta usada pelo Flask-WTF para proteção contra CSRF
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# Inicialização do Bootstrap para estilização automática dos templates
Bootstrap5(app)

# Definição da classe do formulário de cadastro de cafés
class CafeForm(FlaskForm):
    '''
    Classe que define os campos e validações do formulário de cadastro.
    Os dados serão posteriormente processados e salvos no arquivo CSV.
    '''
    cafe_name = StringField('Cafe name', validators=[DataRequired()])
    cafe_location = StringField('Cafe location on Google Maps (URL)', validators=[DataRequired(), URL(message="Invalid URL")])
    cafe_opening = StringField('Opening time e.g. 8AM', validators=[DataRequired()])
    cafe_closing = StringField('Closing time e.g. 5:30PM', validators=[DataRequired()])
    
    # Campos de avaliação com escolhas predefinidas (ratings visuais)
    coffee_rating = SelectField('Coffee Rating', choices=["✘","☕️","☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"], validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Strength Rating', choices=["✘","💪","💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power_rating = SelectField('Power Socket Availability', choices=["✘","🔌","🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    
    submit = SubmitField('Submit')  # Botão de envio do formulário

# Rota principal — exibe a página inicial
@app.route("/")
def home():
    return render_template("index.html")

# Rota para adição de novos cafés
@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()  # Instancia o formulário
    if form.validate_on_submit():
        # Quando o formulário for submetido corretamente, salva os dados no CSV
        with open('cafe-data.csv', "a", newline='', encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe_name.data},{form.cafe_location.data},{form.cafe_opening.data},{form.cafe_closing.data},{form.coffee_rating.data},{form.wifi_rating.data},{form.power_rating.data}")
        return redirect(url_for('cafes'))  # Redireciona para a página de listagem após salvar
    # Se for GET (ou formulário inválido), renderiza o formulário na tela
    return render_template('add.html', form=form)

# Rota que exibe a lista de cafés cadastrados
@app.route('/cafes')
def cafes():
    # Abre o arquivo CSV e carrega todos os registros para exibir na tabela
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)

# Inicialização da aplicação em modo debug (útil para desenvolvimento)
if __name__ == '__main__':
    app.run(debug=True)