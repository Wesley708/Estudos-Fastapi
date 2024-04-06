from peewee import *

db = SqliteDatabase('possofaltar.db')

class Usuario(Model):
    nome = CharField()
    email = CharField(unique=True)
    senha = CharField()
    
    class Meta:
        database = db
        
class Materias(Model):
    usuario = ForeignKeyField(Usuario, backref='usuario')
    materia = CharField()
    
    class Meta:
        database = db
        
db.connect()
db.create_tables([Usuario, Materias], safe=True)