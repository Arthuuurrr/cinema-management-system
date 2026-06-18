from collections import Counter
from datetime import datetime
from ingressos import carregar_vendas


def total_ingressos():
    vendas = carregar_vendas()
    total = len(vendas)

    print("\n--- TOTAL DE INGRESSOS ---")
    print(f"Total de ingressos vendidos: {total}")


def faturamento_total():
    vendas = carregar_vendas()

    faturamento = 0

    for venda in vendas:
        faturamento += venda.get("valor", 0)

    print("\n--- FATURAMENTO TOTAL ---")
    print(f"Faturamento total: R$ {faturamento:.2f}")


def filme_mais_assistido():
    vendas = carregar_vendas()

    print("\n--- FILME MAIS ASSISTIDO ---")

    if not vendas:
        print("Nenhum ingresso foi vendido.")
        return

    filmes = []

    for venda in vendas:
        filmes.append(venda["filme"])

    quantidade_filmes = Counter(filmes)
    filme, quantidade = quantidade_filmes.most_common(1)[0]

    print(f"Filme mais assistido: {filme}")
    print(f"Ingressos vendidos: {quantidade}")


def gerar_relatorio_diario():
    vendas = carregar_vendas()
    data_hoje = datetime.now().strftime("%d/%m/%Y")

    data = input(
        f"\nDigite a data do relatório ou aperte Enter para usar {data_hoje}: "
    ).strip()

    if data == "":
        data = data_hoje

    vendas_do_dia = []

    for venda in vendas:
        if venda.get("data") == data:
            vendas_do_dia.append(venda)

    print("\n--- RELATÓRIO DIÁRIO ---")

    if not vendas_do_dia:
        print(f"Nenhuma venda encontrada em {data}.")
        return

    faturamento = 0
    filmes = []

    for venda in vendas_do_dia:
        faturamento += venda.get("valor", 0)
        filmes.append(venda["filme"])

    quantidade_filmes = Counter(filmes)
    filme, quantidade = quantidade_filmes.most_common(1)[0]

    texto_relatorio = (
        "=== RELATÓRIO DIÁRIO ===\n"
        f"Data: {data}\n"
        f"Total de ingressos vendidos: {len(vendas_do_dia)}\n"
        f"Faturamento do dia: R$ {faturamento:.2f}\n"
        f"Filme mais assistido: {filme}\n"
        f"Ingressos vendidos para esse filme: {quantidade}\n"
    )

    print(texto_relatorio)

    nome_arquivo = "relatorio_" + data.replace("/", "-") + ".txt"

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(texto_relatorio)

    print(f"Relatório salvo em: {nome_arquivo}")


def menu_relatorios():
    while True:
        print("\n=== RELATÓRIOS ===")
        print("1 - Total de ingressos vendidos")
        print("2 - Faturamento total")
        print("3 - Filme mais assistido")
        print("4 - Gerar relatório diário")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            total_ingressos()

        elif opcao == "2":
            faturamento_total()

        elif opcao == "3":
            filme_mais_assistido()

        elif opcao == "4":
            gerar_relatorio_diario()

        elif opcao == "0":
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu_relatorios()
