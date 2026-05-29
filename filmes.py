def criar_filme():
    filmes=[]

    while True:
        filme=input("Digite o nome do filme (ou sair)")

        if filme == "sair":
            break

        if filme not in filmes:
            filmes.append(filme)
    print("\nFilmes Cadastrados:")

    for f in filmes:
        print("-", f)

criar_filme()
