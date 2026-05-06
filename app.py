from flask import Flask, render_template

app = Flask(name_)

@app.route('/')
def index():
    return 'Essa é minha primeira aplicação em Flask!'

# Crie uma rota /login no seu projeto flask que carregue uma página HTML (login. html, por exemplo) contendo um formulário com 2 campos de texto: um para o nome do usuário e outro para senha.

@app.route('/login')
def login():
    return render_template('login.html')
# Crie uma rota/alunos que renderize uma página HTML (alunos. html, por exemplo) com o nome e a matrícula de alguns alunos em uma tabela.

@app. route('/alunos')
def alunos():
    lista_alunos = [
        {'nome': 'Alice', 'matricula': '12345678'}
        {'nome': 'Bruno', 'matricula': '98765432'},
        {'nome': 'Clara', 'matricula': '45678912'},
        {'nome': 'Marcos','matricula': '74125896'},
        {'nome': 'Valéria', 'matricula': '85236974'}
   ]

    return render_template(' alunos. html', alunos-lista_alunos)

#Crie uma rota /arearestrita que recebe um parâmetro (ex: / arearestrita/



@app.route("/arearestrita/<int:id>")
def arearestrita(id):
    if id == 1:
        return 'cadeado Fechado'
    elif id == 2:
          return 'cadeado Aberto'
    else:
        return "Acesso inválido"
    return render_template(' restrita html', imagem=imagem)

# Crie uma rota /operacao que recebe 3 parâmetros (ex: /operacao/<tipo>/<op1>/<op2>.

def operacao (tipo, op1, op2):
             return "Erro: divisâo por zero"
        resultado = op1 / op2
    else:
        return "Tipo de operação inválido"

    return f"Resultado: {resultado}"


@app.route('/somar', defaults={"1": "0", "n2": "0"})
@app. route('/somar/<int:n2>')
def somar (n1, n2):

        resultado = n1 + n2
        return str (resultado)

@app.route('/soma', defaults={"n1": "0", "n2": "0"})
@app. route('/soma/<int:n1>/<int:n2>')
def soma(n1, n2):
  resultado = n1 + n2
  return render_template('somar. html', n1=n1, n2=n2,
  resultado=resultado)
if _name_ == '_main_':
    app. run(debug=True)
