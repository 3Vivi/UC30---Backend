from flask import Flask, render_template

app = Flask(__name__)

@app.route('/´pizzaria/<sabor>')
def pizzaria(sabor):
    pizza= {
        "Carne":{
         "nome": "Pizza de Carne"
          "imagem":"https://stock.adobe.com/br/images/pizza-de-carne-seca-charque-dried-meat-pizza/576746962"
        },
        "margherita": {
            "nome": "Pizza de margherita",
            "imagem"":http://rossopizza.com.br/o-que-voce-sabe-sobre-a-historia-da-pizza-marguerita/"
        },
        "frango": {
            "nome": "Pizza de frango",
            "imagem": "https://www.sabornamesa.com.br/receita-pizza/pizza-de-frango-com-catupiry"
        }
    }   
    if sabor in pizzas:
        return render_template(
            "index.html",
            nome=pizzas[sabor]["nome"],
            imagem= pizzas[sabor]["imagem"]
        )

    return "<h1>Sabor não disponível</h1>"


app.run(debug=True)