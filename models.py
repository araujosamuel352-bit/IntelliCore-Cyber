from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Cliente(db.Model):
    __tablename__ = 'cliente'

    id            = db.Column(db.Integer, primary_key = True)
    nome          = db.Column(db.String(100), nullable = False)
    email         = db.Column(db.String(120), nullable = False)
    empresa       = db.Column(db.String(100))
    plano         = db.Column(db.String(50))
    mensagem      = db.Column(db.Text)
    data_cadastro = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Cliente {self.nome}>'

