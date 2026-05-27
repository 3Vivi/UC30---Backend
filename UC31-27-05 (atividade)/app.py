from flask import Flask, render_template

app = Flask(__name__)

# Página inicial
@app.route('/')
def inicio():
    return render_template('index.html')

# Página de cursos
@app.route('/cursos')
def cursos():
    return render_template('cursos.html')

# Página de professores
@app.route('/professores')
def professores():
    return render_template('professores.html')

# Página de contato
@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)