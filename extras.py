from cinema import filmes, salas, sessoes, ingressos
from datetime import datetime
from collections import Counter


def registrar_log(acao):
    with open("log_sistema.txt", "a", encoding="utf-8") as arquivo:
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        arquivo.write(f"{data} - {acao}\n")


def ver_log():
    try:
        with open("log_sistema.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()

            if conteudo == "":
                print("Nenhum registro no log.")
            else:
                print("\n=== LOG DO SISTEMA ===")
                print(conteudo)

    except FileNotFoundError:
        print("Nenhum log foi criado ainda.")


def dashboard():
    print("\n========== DASHBOARD ==========")

    faturamento = 0

    for ingresso in ingressos:
        faturamento += ingresso["valor"]

    print(f"Filmes cadastrados: {len(filmes)}")
    print(f"Salas cadastradas: {len(salas)}")
    print(f"Sessões cadastradas: {len(sessoes)}")
    print(f"Ingressos vendidos: {len(ingressos)}")
    print(f"Faturamento total: R$ {faturamento:.2f}")

    if ingressos:
        lista_filmes = []

        for ingresso in ingressos:
            lista_filmes.append(ingresso["filme"])

        contagem = Counter(lista_filmes)
        filme, quantidade = contagem.most_common(1)[0]

        print(f"Filme mais vendido: {filme}")
        print(f"Ingressos desse filme: {quantidade}")

    if sessoes:
        sessao_mais_ocupada = sessoes[0]

        for sessao in sessoes:
            if sessao["ocupados"] > sessao_mais_ocupada["ocupados"]:
                sessao_mais_ocupada = sessao

        print(f"Sessão mais ocupada: {sessao_mais_ocupada['filme']}")
        print(f"Ocupação: {sessao_mais_ocupada['ocupados']}/{sessao_mais_ocupada['capacidade']}")

    print("===============================")


def exportar_relatorio_txt():
    faturamento = 0

    for ingresso in ingressos:
        faturamento += ingresso["valor"]

    with open("relatorio_cinema.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("===== RELATÓRIO DO CINEMA =====\n\n")
        arquivo.write(f"Filmes cadastrados: {len(filmes)}\n")
        arquivo.write(f"Salas cadastradas: {len(salas)}\n")
        arquivo.write(f"Sessões cadastradas: {len(sessoes)}\n")
        arquivo.write(f"Ingressos vendidos: {len(ingressos)}\n")
        arquivo.write(f"Faturamento total: R$ {faturamento:.2f}\n\n")

        if ingressos:
            lista_filmes = []

            for ingresso in ingressos:
                lista_filmes.append(ingresso["filme"])

            contagem = Counter(lista_filmes)
            filme, quantidade = contagem.most_common(1)[0]

            arquivo.write(f"Filme mais vendido: {filme}\n")
            arquivo.write(f"Ingressos vendidos desse filme: {quantidade}\n")

    registrar_log("Relatório exportado em TXT")
    print("Relatório exportado com sucesso!")


def buscar_filmes():
    if not filmes:
        print("Nenhum filme cadastrado.")
        return

    print("\n=== BUSCA DE FILMES ===")
    print("1 - Nome")
    print("2 - Gênero")
    print("3 - Diretor")
    print("4 - Classificação")

    opcao = input("Escolha uma opção: ")
    busca = input("Digite o termo da busca: ").lower()

    encontrados = []

    for filme in filmes:
        if opcao == "1" and busca in filme["nome"].lower():
            encontrados.append(filme)

        elif opcao == "2" and busca in filme["genero"].lower():
            encontrados.append(filme)

        elif opcao == "3" and busca in filme["diretor"].lower():
            encontrados.append(filme)

        elif opcao == "4" and busca in filme["classificacao"].lower():
            encontrados.append(filme)

    if not encontrados:
        print("Nenhum filme encontrado.")
        return

    print("\nFilmes encontrados:")

    for filme in encontrados:
        print(f"Nome: {filme['nome']}")
        print(f"Gênero: {filme['genero']}")
        print(f"Diretor: {filme['diretor']}")
        print(f"Classificação: {filme['classificacao']}")
        print("-" * 30)

