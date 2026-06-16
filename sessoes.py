""" Cadastrar salas
    Criar sessões
    Listar sessões
    Verificar capacidade da sala"""

def cadastrar_salas():
    sessoes=[]

    while True:

        salas=input("digite o numero da sua sala (ou sair):")

        if salas == "sair":
            break

        if salas not in sessoes:
            sessoes.append(salas)

        else:
            print("essa sala já existe!")

cadastrar_salas()

lista_sessoes=[]

while True:
    sessoess=input("digite o nome da sessão (0 pra fechar):")
    lista_sessoes.append(sessoess)
    if sessoess == "0":
       break
    elif sessoess in lista_sessoes:
        print(lista_sessoes)

