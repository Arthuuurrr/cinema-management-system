import pickle
from datetime import datetime

ARQUIVO_VENDAS = "vendas.pkl"


def carregar_vendas():
    try:
        with open(ARQUIVO_VENDAS, "rb") as arquivo:
            vendas = pickle.load(arquivo)

            if isinstance(vendas, list):
                return vendas

            return []

    except FileNotFoundError:
        return []

    except (EOFError, pickle.UnpicklingError):
        print("Não foi possível carregar o arquivo de vendas.")
        return []


def salvar_vendas(vendas):
    with open(ARQUIVO_VENDAS, "wb") as arquivo:
        pickle.dump(vendas, arquivo)


def ler_valor():
    while True:
        valor_digitado = input("Valor do ingresso: R$ ").replace(",", ".")

        try:
            valor = float(valor_digitado)

            if valor > 0:
                return valor

            print("O valor precisa ser maior que zero.")

        except ValueError:
            print("Digite um valor válido. Exemplo: 25,00")


def vender_ingresso():
    print("\n--- VENDA DE INGRESSO ---")

    nome = input("Nome do cliente: ").strip()
    cpf = input("CPF do cliente: ").strip()
    filme = input("Nome do filme: ").strip()
    sessao = input("Horário da sessão: ").strip()
    assento = input("Assento escolhido: ").strip().upper()
    valor = ler_valor()

    vendas = carregar_vendas()

    for venda in vendas:
        if (
            venda["filme"].lower() == filme.lower()
            and venda["sessao"] == sessao
            and venda["assento"].upper() == assento
        ):
            print("\nEsse assento já foi vendido para essa sessão.")
            return

    ingresso = {
        "nome": nome,
        "cpf": cpf,
        "filme": filme,
        "sessao": sessao,
        "assento": assento,
        "valor": valor,
        "data": datetime.now().strftime("%d/%m/%Y"),
        "hora_venda": datetime.now().strftime("%H:%M")
    }

    vendas.append(ingresso)
    salvar_vendas(vendas)

    print("\nIngresso vendido com sucesso!")
    print(f"Cliente: {nome}")
    print(f"Filme: {filme}")
    print(f"Sessão: {sessao}")
    print(f"Assento: {assento}")
    print(f"Valor: R$ {valor:.2f}")


def listar_vendas():
    vendas = carregar_vendas()

    print("\n--- INGRESSOS VENDIDOS ---")

    if not vendas:
        print("Nenhum ingresso foi vendido.")
        return

    for numero, venda in enumerate(vendas, start=1):
        print(f"\nIngresso {numero}")
        print(f"Cliente: {venda['nome']}")
        print(f"CPF: {venda['cpf']}")
        print(f"Filme: {venda['filme']}")
        print(f"Sessão: {venda['sessao']}")
        print(f"Assento: {venda['assento']}")
        print(f"Valor: R$ {venda['valor']:.2f}")
        print(f"Data da venda: {venda['data']}")
        print("-" * 30)


def menu_ingressos():
    while True:
        print("\n=== INGRESSOS ===")
        print("1 - Vender ingresso")
        print("2 - Listar ingressos vendidos")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            vender_ingresso()

        elif opcao == "2":
            listar_vendas()

        elif opcao == "0":
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu_ingressos()
