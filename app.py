from flask import Flask, render_template

app = Flask(__name__)

# Página inicial
@app.route("/")
def index():
    return render_template("index.html")


# Cardápio
@app.route("/cardapio")
def cardapio():
    return render_template("cardapio.html")


# Página dinâmica do lanche
@app.route("/lanche/<nome>")
def lanche(nome):

    mensagem = ""

    if nome.lower() == "pizza":
        mensagem = "Pizza deliciosa saindo do forno!"
    elif nome.lower() == "sushi":
        mensagem = "sushi fresquinho!"
    elif nome.lower() == "batata":
        mensagem = "Batata frita crocante e saborosa!"
    elif nome.lower() == "milkshake":
        mensagem = "Milkshake gelado e cremoso!"
    else:
        mensagem = "Lanche não encontrado."

    return render_template(
        "lanche.html",
        nome=nome,
        mensagem=mensagem
    )

# Página de pedidos
@app.route("/pedidos")
def pedidos():

    pedidos = [
        {"cliente": "Ana", "pedido": "Pizza", "valor": "R$ 35"},
        {"cliente": "Pedro", "pedido": "Temaki hot", "valor": "R$ 14"},
        {"cliente": "Carlos", "pedido": "Batata Frita", "valor": "R$ 20"},
        {"cliente": "Julia", "pedido": "Milkshake", "valor": "R$ 18"}
    ]

    return render_template(
        "pedidos.html",
        pedidos=pedidos
    )

# Página dinâmica do cliente
@app.route("/cliente/<nome>/<cidade>")
def cliente(nome, cidade):

    if cidade.lower() == "natal":
        status = "Entrega disponível!"
    else:
        status = "Entrega indisponível."

    return render_template(
        "cliente.html",
        nome=nome,
        cidade=cidade,
        status=status
    )

# Página contato
@app.route("/contato")
def contato():
    return render_template("contato.html")


if __name__ == "__main__":
    app.run(debug=True)