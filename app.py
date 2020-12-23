from flask import Flask, render_template , redirect, url_for, request
import os

app = Flask(__name__)

usuarios = [{"login":"teste","senha":"1234" }]


@app.route("/index", methods=["GET"] )
def index():
    return render_template("index.html")

@app.route("/eletronica", methods=["GET"] )
def eletronica():
    return render_template("page-ele.html")

@app.route("/rock", methods=["GET"] )
def rock():
    return render_template("page-rock.html")

@app.route("/classic", methods=["GET"] )
def classic():
    return render_template("page-cla.html")

@app.route("/pop", methods=["GET"] )
def pop():
    return render_template("page-pop.html")

@app.route("/descricao", methods=["GET"] )
def descricao():
    return render_template("descricao.html")

@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/conteudo")
def conteudo():
    return render_template("conteudo.html")


@app.route("/formlogin", methods=["PUT","POST"])
def formlogin():
    login = request.form["login"]
    senha = request.form["password"]
    for user in usuarios:
        if user['login'] == login and user['senha'] == senha:
            return render_template("index.html")
    return render_template("login.html", mensagem = "Login inválido.")

if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(debug=True, host='localhost', port=port)