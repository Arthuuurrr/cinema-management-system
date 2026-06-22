"""MODULO DE FILMES
1. Módulo de Filmes
 Cadastrar filmes
 Listar filmes
 Editar informações
 Remover filme"""


from cinema import filmes, salvar_dados


def cadastrar_filme():
    while True:
        nome = input("Qual o filme? (digite sair para parar) ")

        if nome.lower() == "sair":
            break

        filme_existe = False

        for filme in filmes:
            if filme["nome"].lower() == nome.lower():
                filme_existe = True
                break

        if filme_existe:
            print("Filme já foi cadastrado!")
            continue

        genero = input("Qual o genero? ")

        try:
            duracao = int(input("Qual a duracao? "))
            ano = int(input("Qual o ano de lançamento? "))
        except ValueError:
            print("Digite apenas números!")
            continue

        classificacao = input("Qual a classificacao? ")
        diretor = input("Qual o diretor? ")

        filme = {
            "nome": nome,
            "genero": genero,
            "duracao": duracao,
            "classificacao": classificacao,
            "ano": ano,
            "diretor": diretor
        }

        filmes.append(filme)

        salvar_dados()

        print("Filme cadastrado com sucesso!")


def listar_filmes():
    if not filmes:
        print("Nenhum filme foi cadastrado.")
        return

    print("\n=== FILMES CADASTRADOS ===")

    for filme in filmes:
        print(f"Nome: {filme['nome']}")
        print(f"Gênero: {filme['genero']}")
        print(f"Duração: {filme['duracao']} min")
        print(f"Classificação: {filme['classificacao']}")
        print(f"Ano: {filme['ano']}")
        print(f"Diretor: {filme['diretor']}")
        print("-" * 30)


def editar_filme():
    nome = input("Qual filme deseja editar? (0 para cancelar) ")

    if nome == "0":
        return

    for filme in filmes:

        if filme["nome"].lower() == nome.lower():

            print("\n1 - Nome")
            print("2 - Gênero")
            print("3 - Duração")
            print("4 - Classificação")
            print("5 - Ano")
            print("6 - Diretor")

            opcao = input("O que deseja editar? ")

            if opcao == "1":
                filme["nome"] = input("Novo nome: ")

            elif opcao == "2":
                filme["genero"] = input("Novo gênero: ")

            elif opcao == "3":
                filme["duracao"] = int(input("Nova duração: "))

            elif opcao == "4":
                filme["classificacao"] = input("Nova classificação: ")

            elif opcao == "5":
                filme["ano"] = int(input("Novo ano: "))

            elif opcao == "6":
                filme["diretor"] = input("Novo diretor: ")

            else:
                print("Opção inválida!")
                return

            salvar_dados()

            print("Filme editado com sucesso!")
            return

    print("Filme não encontrado!")


def remover_filme():
    nome = input("Qual filme deseja remover? (0 para cancelar) ")

    if nome == "0":
        return

    for filme in filmes:

        if filme["nome"].lower() == nome.lower():

            certeza = input(
                f"Tem certeza que deseja remover {nome}? (sim/nao) "
            )

            if certeza.lower() == "sim":

                filmes.remove(filme)

                salvar_dados()

                print("Filme removido com sucesso!")

            else:
                print("Operação cancelada!")

            return

    print("Filme não encontrado!")
