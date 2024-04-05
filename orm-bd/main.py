from database import db , Usuario, Anuncios


db.connect()

db.create_tables([Usuario, Anuncios])




usuario = Usuario.create(nome = input("Nome: "), email = input("Email: "), senha = input("Senha: "))

# print("Novo Usuário: ", usuario.id, usuario.nome, usuario.email)

lista_usuarios = Usuario.select()
print("Listando Usuários:")

for usuario in lista_usuarios:
    print("id : ",usuario.id)
    print("Nome : ",usuario.nome)
    print("Email : ",usuario.email)
    print("")
    
usuario = Usuario.get(int(input("Digite o Id que quer pesquisar: ")))

print("Listando o usuário de Id :", usuario.id)
print("id : ",usuario.id)
print("Nome : ",usuario.nome)
print("Email : ",usuario.email)
print("")

try:
    editusuario = Usuario.get(int(input("Digite o Id do usuário que deseja editar")))
    print("Editando o usuário de Id : ", editusuario.id)
    print("")
    print("O nome atual é : ", editusuario.nome)
    editusuario.nome = input("Qual o novo nome do usuário? : ")
    print("O email atual é : ", editusuario.email)
    editusuario.email = input("Qual o novo email do usuário? : ")
    editusuario.save()
    print("Listando o usuário Editado de Id :", editusuario.id)
    print("id : ",editusuario.id)
    print("Nome : ",editusuario.nome)
    print("Email : ",editusuario.email)
    print("")
except:
    print("usuário não existe")
    
try:
    deleteusuario = Usuario.get(int(input("Qual o id do usuário que deseja excluir : ")))
    deleteusuario.delete_instance()
    print("Usuario Id : ", deleteusuario.id , " deletado")
    deleteusuario.save()
except:
    print("Usuário não existe")
        