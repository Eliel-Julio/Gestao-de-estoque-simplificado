import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from flask import Flask,render_template
from def_database import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', produtos=session.query(Produto).all())
@app.route('/produto/<int:id>')
def produto():
    produto = session.query(Produto).filter_by(id=id).first()
    if produto:
        return render_template('produto.html', produto=produto)
    else:
        return "Produto não encontrado", 404

app.run(debug=True)