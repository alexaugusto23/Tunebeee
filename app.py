from flask import Flask, render_template , redirect, url_for
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/conteudo")
def conteudo():
    return render_template("conteudo.html")

if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(debug=True, host='localhost', port=port)