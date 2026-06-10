"""MODULO DE FILMES
1. Módulo de Filmes
 Cadastrar filmes
 Listar filmes
 Editar informações
 Remover filme"""

"""Cadastrar= nome/genero/duracao/classificao indicativa"""

filmes=[]

def cadastrar_filme():
    while True:
        nome=input("Qual o filme? (digite sair para parar)")
        if nome == "sair":
            break 
        genero=input("Qual o genero?")
        duracao=int(input("Qual a duracao?"))
        classificacao=input("Qual a classificacao?")
        ano=int(input("Qual o ano de lançamento"))
        diretor=input("Qual o diretor")

        filme = {
        "nome" : nome,
        "genero" : genero,
        "duracao" : duracao,
        "classificacao" : classificacao,
        "ano" : ano,
        "diretor" : diretor
        
    }
        filmes.append(filme)
        print("Filme cadastrado com sucesso")

"""Esta parte foi responsavel pelo cadastro dos filmes no codigo,
coletando os dados, por meio de inputs que passam pra dicionarios"""


def listar_filme():
    if not filmes:
        print("Nenhum filme foi cadastrado.")
        return
    
    print("\nFilmes Cadastrados:")
    
    for filme in filmes:
        print(f"Nome: {filme['nome']}") 
        print(f"Genero: {filme['genero']}")
        print(f"Duracao: {filme['duracao']}min")
        print(f"Classificacao: {filme['classificacao']}")
        print(f"Ano: {filme['ano']}") 
        print(f"Diretor: {filme['diretor']}\n") 

"""Esta parte foi responsavel pela listagem dos filmes no codigo,
coletando os dados dos filmes ja cadastrados e printando eles"""


def editar_filme():
    nome=input("Qual filme voce desseja editar (0 para cancelar)")
    
    if nome == "0":
        return

    for filme in filmes:
        if filme["nome"].lower() == nome.lower():
            print("1 - Nome")
            print("2 - Gênero")
            print("3 - Duração")
            print("4 - Classificação")
            print("5 - Ano")
            print("6 - Diretor")

            opcao = input("O que deseja editar? ")
            
            if opcao == "1":
                filme["nome"] = input("Novo nome: ")
            if opcao == "2":
                filme["genero"] = input("Novo genero: ")
            if opcao == "3":
                filme["duracao"] = int(input("Nova duração: "))
            if opcao == "4":
                filme["classificacao"] = input("Nova classificacao: ")
            if opcao == "5":
                filme["ano"] = int(input("Novo ano: "))
            if opcao == "6":
                filme["diretor"] = input("Novo diretor: ")

            print("Filme editado com sucesso")
            return

    print("Filme não encontrado. ")


"""Esta parte foi responsavel pela edicao dos filmes no catalogo,
coletando os dados e alterando o dado escolhido para o novo valor determinado"""


def remover_filme():
    nome=input("Qual filme voce deseja remover: (0 para cancelar)")

    if nome== "0":
        return

    for filme in filmes:
        if filme["nome"].lower() == nome.lower():
            certeza=input(f"Tem certeza que deseja excluir {nome}(responda com sim ou nao)")
            if certeza.lower() == "sim":
                filmes.remove(filme)
                print(f"Filme{nome} removido com sucesso!")
            else:
                print("Operação Cancelada!")

            return
        
    print("Filme não encontrado!")
            

"""Esta parte foi responsavel pela remocao dos filmes no catalogo,
pegando os dados do filme escolhido e removendo da lista de filmes 
inclusas em listar_filmes"""


while True:
    print("\n===MODULO FILMES===")
    print("1- Cadastrar Filmes")
    print("2- Listar Filmes ")
    print("3- Editar Filmes")
    print("4- Remover Filmes")
    print("0- Sair")

    opcao=input("Escolha uma opção")

    if opcao == "1":
        cadastrar_filme()
    elif opcao == "2":
        listar_filme()
    elif opcao == "3":
        editar_filme()
    elif opcao == "4":
        remover_filme()
    elif opcao == "0":
        break
    else:
        print("Opção Inválida")

"""Esta parte do codigo cria um menu inicial, para que o usuario escolha qual funcao utilizar
separando por cada uma das funcoes criadas no codigo"""
