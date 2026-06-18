""" Cadastrar salas
    Criar sessões
    Listar sessões
    Verificar capacidade da sala"""
from cinema import filmes
from cinema import salas
from cinema import sessoes

\






"""MOSTRAR O FILME
    ESCOLHER O FILME
    RECUPERAR O FILME ESCOLHIDO
    ESCOLHER A SALA
    CRIAR HORARIOS
    CRIAR A SESSAO(DICICIONARIO)"""





def cadastrar_salas():
    while True:
        num_sala=int(input("Qual o numero da sala que deseja adicionar (0 para sair)"))

        if num_sala == 0:
            break

        sala_existe = False

        for sala in salas:
            if sala['numero'] == num_sala:
                sala_existe = True
                break

        if sala_existe:
            print("Essa sala ja foi cadastrada!")
            continue

        capacidade = int(input("Qual a capacidade da sala"))

        sala = {"numero" : num_sala,
               "capacidade" : capacidade
               }

        salas.append(sala)
        print("Sala cadastrada com sucesso!")


def listar_salas():
    if not salas:
        print("Nenhuma sala foi cadastrada!")
        return
    for sala in salas:
        print(f"Sala: {sala['numero']}")
        print(f"Capacidade: {sala['capacidade']}")
        print(f"-" * 20)



cadastrar_salas()
listar_salas()


def criar_sessoes():
    if not filmes:
        print("Nenhum filme foi cadastrado")
        return
    
    print("\nFilmes Dispoiveis:")
