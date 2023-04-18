# Importação do Flask para criar um webApp e o render_template para renderizar os templates HTML
from flask import Flask, render_template

# Nomear o arquivo como "app": nome padrão dado na documentação Flask

app = Flask(__name__)

produto = {
	"id":1,
	"nome":"Iphone 14 PRO ",
	"descricao":"Iphone 14, modelo PRO MAX, na cor vermelha",
	"preco":7800.00,
	"imagem":"https://upload.wikimedia.org/wikipedia/commons/3/37/Back_of_the_iPhone_14_Pro.jpg"
}

@app.route("/produto")
def exibe_produto():
    return render_template("produto.html", **produto)

app.run(debug = True)