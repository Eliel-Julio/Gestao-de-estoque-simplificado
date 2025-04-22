import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from flask import Flask,render_template, redirect, url_for
from def_database import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', produtos=session.query(Produto).all())
@app.route('/produto/<int:id>')
def produto(id):
    produto = session.query(Produto).filter_by(id=id).first()
    if produto:
        print(produto.nome)
        return render_template('produto.html', produto=produto)
    else:
        return "Produto não encontrado", 404

@app.route('/produto/<int:id>/update/baixa/<int:quant>', methods=['POST'])
def baixa_produto(id, quant):
    produto = session.query(Produto).filter_by(id=id).first()
    produto.Baixa(quant)
    session.commit()
    return redirect(url_for('index'))

@app.route('/produto/<int:id>/update/subir/<int:quant>', methods=['POST'])
def subir_produto(id, quant):
    produto = session.query(Produto).filter_by(id=id).first()
    produto.Subir(quant)
    session.commit()
    return redirect(url_for('index'))

app.run(debug=True)