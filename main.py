from flask import Flask, render_template

from frases import Estoico, Pessoa

app = Flask(__name__)

frases = Estoico.get_frases()[0]
print(frases)

adne = Pessoa(nome="adne", idade=15, sexo='masculino' )
asd = Pessoa(nome='asd', idade=155, sexo= 'feminino')
kgjl = Pessoa(nome='kgjl', idade=666, sexo= 'biscoute')


todas_pessoas = [adne, asd, kgjl]

@app.route("/hello")
def hello():
    return render_template("lista.html",
                        variavel_h1= "Eu não tenho inimigos",
                        lista_itens= todas_pessoas
                        )

if __name__ == '__main__':

    app.run()
