from cinema import ingressos
from collections import Counter


def total_ingressos():
    print(f"\nTotal de ingressos vendidos: {len(ingressos)}")


def faturamento_total():
    total = 0

    for ingresso in ingressos:
        total += ingresso["valor"]

    print(f"\nFaturamento total: R$ {total:.2f}")


def filme_mais_assistido():
    if not ingressos:
        print("\nNenhum ingresso vendido.")
        return

    filmes_vendidos = []

    for ingresso in ingressos:
        filmes_vendidos.append(ingresso["filme"])

    contagem = Counter(filmes_vendidos)

    filme = contagem.most_common(1)[0]

    print(f"\nFilme mais assistido: {filme[0]}")
    print(f"Ingressos vendidos: {filme[1]}")


def relatorio_diario():
    if not ingressos:
        print("\nNenhum ingresso vendido.")
        return

    data = input("Digite a data do relatório (dd/mm/aaaa): ")

    total = 0
    faturamento = 0

    for ingresso in ingressos:
        if ingresso["data"] == data:
            total += 1
            faturamento += ingresso["valor"]

    print(f"\n=== RELATÓRIO DO DIA {data} ===")
    print(f"Ingressos vendidos: {total}")
    print(f"Faturamento: R$ {faturamento:.2f}")
