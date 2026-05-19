from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')          
def index():
    return render_template('index.html', usuario=None, nome=None, tittle='home')

@app.route('/contato')
def contato():
    nome = 'Gaby'
    return render_template('index.html', tittle='Página Inicial', nome=nome, usuario=None)
