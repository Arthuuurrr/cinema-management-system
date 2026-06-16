
vendas = []

def vender_ingresso():
    print("\n--- Venda de Ingresso ---")

    nome = input("Nome do cliente: ")
    cpf = input("CPF do cliente: ")
    filme = input("Nome do filme: ")
    sessao = input("Horário da sessão: ")
    assento = input("Assento escolhido: ")

    ingresso = {
        "nome": nome,
        "cpf": cpf,
        "filme": filme,
        "sessao": sessao,
        "assento": assento
    }

    vendas.append(ingresso)

    print("\nIngresso vendido com sucesso!")
