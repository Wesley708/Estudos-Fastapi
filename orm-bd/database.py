from peewee import *

db = SqliteDatabase('freelancers.db')

class Usuario(Model):
    nome = CharField()
    email = CharField(unique=True)
    senha = CharField()
    
    class Meta:
        database = db
        
class Anuncios(Model):
    usuario = ForeignKeyField(Usuario, backref='usuario')
    titulo = CharField()
    descricao = TextField()
    valor = DecimalField()
    
    class Meta:
        database = db