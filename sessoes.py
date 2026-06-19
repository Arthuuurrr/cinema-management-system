from cinema import filmes, salas, sessoes, salvar_dados


def cadastrar_salas():
    while True:
        num_sala = int(input("Qual o numero da sala que deseja adicionar? (0 para sair) "))

        if num_sala == 0:
            break

        sala_existe = False

        for sala in salas:
            if sala["numero"] == num_sala:
                sala_existe = True
                break

        if sala_existe:
            print("Essa sala ja foi cadastrada!")
            continue

        capacidade = int(input("Qual a capacidade da sala? "))

        sala = {
            "numero": num_sala,
            "capacidade": capacidade
        }

        salas.append(sala)
        salvar_dados()

        print("Sala cadastrada com sucesso!")


def listar_salas():
    if not salas:
        print("Nenhuma sala foi cadastrada!")
        return

    print("\n=== SALAS CADASTRADAS ===")

    for sala in salas:
        print(f"Sala: {sala['numero']}")
        print(f"Capacidade: {sala['capacidade']}")
        print("-" * 20)


def criar_sessoes():
    if not filmes:
        print("Nenhum filme foi cadastrado!")
        return

    if not salas:
        print("Nenhuma sala foi cadastrada!")
        return

    print("\nFilmes Disponíveis:")

    for i, filme in enumerate(filmes, start=1):
        print(f"{i} - {filme['nome']}")

    opcao_filme = int(input("Escolha um filme: "))

    if opcao_filme < 1 or opcao_filme > len(filmes):
        print("Filme inválido!")
        return

    filme_escolhido = filmes[opcao_filme - 1]

    print("\nSalas Disponíveis:")

    for sala in salas:
        print(f"Sala {sala['numero']} - Capacidade: {sala['capacidade']}")

    sala_escolhida = int(input("Escolha uma sala: "))

    sala_encontrada = None

    for sala in salas:
        if sala["numero"] == sala_escolhida:
            sala_encontrada = sala
            break

    if sala_encontrada is None:
        print("Sala não encontrada!")
        return

    horario = input("Digite o horário da sessão: ")

    for sessao in sessoes:
        if sessao["sala"] == sala_escolhida and sessao["horario"] == horario:
            print("Já existe uma sessão nessa sala nesse horário!")
            return

    sessao = {
        "id": len(sessoes) + 1,
        "filme": filme_escolhido["nome"],
        "sala": sala_escolhida,
        "horario": horario,
        "capacidade": sala_encontrada["capacidade"],
        "ocupados": 0
    }

    sessoes.append(sessao)
    salvar_dados()

    print("Sessão criada com sucesso!")


def listar_sessoes():
    if not sessoes:
        print("Nenhuma sessão foi cadastrada!")
        return

    print("\n=== SESSÕES CADASTRADAS ===")

    for sessao in sessoes:
        print(f"ID: {sessao['id']}")
        print(f"Filme: {sessao['filme']}")
        print(f"Sala: {sessao['sala']}")
        print(f"Horário: {sessao['horario']}")
        print(f"Capacidade: {sessao['capacidade']}")
        print(f"Ocupados: {sessao['ocupados']}")
        print("-" * 30)


def verificar_capacidade():
    if not sessoes:
        print("Nenhuma sessão foi cadastrada!")
        return

    listar_sessoes()

    id_sessao = int(input("Digite o ID da sessão que deseja verificar: "))

    for sessao in sessoes:
        if sessao["id"] == id_sessao:
            disponiveis = sessao["capacidade"] - sessao["ocupados"]

            print("\n=== CAPACIDADE DA SESSÃO ===")
            print(f"Filme: {sessao['filme']}")
            print(f"Sala: {sessao['sala']}")
            print(f"Horário: {sessao['horario']}")
            print(f"Capacidade total: {sessao['capacidade']}")
            print(f"Ocupados: {sessao['ocupados']}")
            print(f"Disponíveis: {disponiveis}")

            return

    print("Sessão não encontrada!")
