from collections import Counter
from ingressos import carregar_ingressos


def total_ingressos(ingressos):
    print(f"\nTotal de ingressos vendidos: {len(ingressos)}")


def faturamento_total(ingressos):
    total = 0

    for ingresso in ingressos:
        total += ingresso["valor"]

    print(f"\nFaturamento total: R$ {total:.2f}")


def filme_mais_assistido(ingressos):
    if not ingressos:
        print("\nNenhum ingresso vendido.")
        return

    filmes = []

    for ingresso in ingressos:
        filmes.append(ingresso["filme"])

    contagem = Counter(filmes)
    filme = contagem.most_common(1)[0]

    print(f"\nFilme mais assistido: {filme[0]}")
    print(f"Ingressos vendidos: {filme[1]}")


def menu_relatorios(ingressos):
    ingressos.clear()
    ingressos.extend(carregar_ingressos())

    while True:
        print("\n=== RELATÓRIOS ===")
        print("1 - Total de ingressos vendidos")
        print("2 - Faturamento total")
        print("3 - Filme mais assistido")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            total_ingressos(ingressos)

        elif opcao == "2":
            faturamento_total(ingressos)

        elif opcao == "3":
            filme_mais_assistido(ingressos)

        elif opcao == "0":
            break

        else:
            print("Opção inválida!")
