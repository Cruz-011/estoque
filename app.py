from flask import Flask, render_template, request
from controle_estoque import ControleEstoque
import os

app = Flask(__name__, static_folder='static', template_folder='templates')


controle = ControleEstoque()

@app.route('/')
def index():
    return render_template('index.html', estoque=controle.estoque, total=controle.total_estoque())

@app.route('/adicionar', methods=['POST'])
def adicionar():
    sabor = request.form['sabor']
    quantidade = int(request.form['quantidade'])
    controle.adicionar_estoque(sabor, quantidade)
    return index()

@app.route('/remover', methods=['POST'])
def remover():
    sabor = request.form['sabor']
    quantidade = int(request.form['quantidade'])
    controle.remover_estoque(sabor, quantidade)
    return index()

if __name__ == '__main__':
    app.run(debug=True)
