from flask import Flask, render_template

from frases import Estoico

app = Flask(__name__)


@app.route("/hello")
def hello():
    return render_template("lista.html",
                        variavel_h1= "Eu não tenho inimigos",
                        lista_itens= Estoico.frases()
                        )

app.run()
