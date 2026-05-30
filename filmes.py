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
cadastrar_filme()



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

listar_filme()




def editar_filme():
    nome=input("Qual filme voce desseja editar")
    
    for filme in filmes:
        if filme["nome"] == nome:
            print("1 - Nome")
            print("2 - Gênero")
            print("3 - Duração")
            print("4 - Classificação")
            print("5 - Ano")
            print("6 - Direito")

            opcao = input("O que deseja editar? ")
            
            if opcao == "1":
                filme["nome"] = input("Novo nome: ")
            if opcao == "2":
                filme["genero"] = input("Novo genero: ")
            if opcao == "3":
                filme["duracao"] = input("Nova duração: ")
            if opcao == "4":
                filme["classificacao"] = input("Nova classificacao: ")
            if opcao == "5":
                filme["ano"] = input("Novo ano: ")
            if opcao == "6":
                filme["diretor"] = input("Novo diretor: ")

            print("Filme editado com sucesso")
            return

    print("Filme não encontrado. ")
