from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from models import db, Cliente

#------------rotas--------------

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# ── Cria tabelas automaticamente ao iniciar ──
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/produto')
def produto():
    return render_template('produto.html')

@app.route('/demo')
def demo():
    return render_template('demo.html')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        novo_cliente = Cliente(
            nome     = request.form['nome'],
            email    = request.form['email'],
            empresa  = request.form['empresa'],
            plano    = request.form['plano'],
            mensagem = request.form['mensagem']
        )
        db.session.add(novo_cliente)
        db.session.commit()
        flash('Mensagem enviada com sucesso!')
        return redirect(url_for('contato'))
    return render_template('contato.html')

#-------------inicializaçao-----------

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug = False)
