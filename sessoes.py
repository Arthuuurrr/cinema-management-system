""" Cadastrar salas
    Criar sessões
    Listar sessões
    Verificar capacidade da sala"""

def cadastrar_salas():
    sessoes=[]

    while True:

        salas=input("digite o numero da sua sala?(ou sair)")

        if salas == "sair":
            break

        if salas not in sessoes:
            sessoes.append(salas)

        else:
            print("essa sala já existe!")

cadastrar_salas()

lista_sessoes=[]

while true
sessoes=input("digite o nome da sessão:(1 para adicionar mais e 0 pra fechar)")
lista_sessoes.append(sessoes)
if sessoes == 0 
break
else
