import pickle
from datetime import datetime

ARQUIVO = "ingressos.pkl"


def carregar_ingressos():
    try:
        with open(ARQUIVO, "rb") as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        return []


def salvar_ingressos(ingressos):
    with open(ARQUIVO, "wb") as arquivo:
        pickle.dump(ingressos, arquivo)


def vender_ingresso(ingressos):
    print("\n--- VENDA DE INGRESSO ---")

    nome = input("Nome do cliente: ")
    cpf = input("CPF do cliente: ")
    filme = input("Nome do filme: ")
    sessao = input("Horário da sessão: ")
    assento = input("Assento escolhido: ")

    try:
        valor = float(input("Valor do ingresso: R$ ").replace(",", "."))
    except ValueError:
        print("Valor inválido!")
        return

    for ingresso in ingressos:
        if (
            ingresso["filme"].lower() == filme.lower()
            and ingresso["sessao"] == sessao
            and ingresso["assento"].lower() == assento.lower()
        ):
            print("Esse assento já foi vendido para essa sessão!")
            return

    ingresso = {
        "nome": nome,
        "cpf": cpf,
        "filme": filme,
        "sessao": sessao,
        "assento": assento,
        "valor": valor,
        "data": datetime.now().strftime("%d/%m/%Y")
    }

    ingressos.append(ingresso)
    salvar_ingressos(ingressos)

    print("\nIngresso vendido com sucesso!")


def listar_ingressos(ingressos):
    print("\n--- INGRESSOS VENDIDOS ---")

    if not ingressos:
        print("Nenhum ingresso vendido.")
        return

    for numero, ingresso in enumerate(ingressos, start=1):
        print(f"\nIngresso {numero}")
        print(f"Cliente: {ingresso['nome']}")
        print(f"CPF: {ingresso['cpf']}")
        print(f"Filme: {ingresso['filme']}")
        print(f"Sessão: {ingresso['sessao']}")
        print(f"Assento: {ingresso['assento']}")
        print(f"Valor: R$ {ingresso['valor']:.2f}")
        print(f"Data: {ingresso['data']}")


def menu_ingressos(ingressos):
    ingressos.clear()
    ingressos.extend(carregar_ingressos())

    while True:
        print("\n=== INGRESSOS ===")
        print("1 - Vender ingresso")
        print("2 - Listar ingressos")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            vender_ingresso(ingressos)

        elif opcao == "2":
            listar_ingressos(ingressos)

        elif opcao == "0":
            break

        else:
            print("Opção inválida!")
