from cinema import ingressos, sessoes, salvar_dados
from datetime import datetime


def mostrar_assentos(capacidade, assentos_ocupados):

    print("\n=== MAPA DE ASSENTOS ===")

    colunas = 5
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    quantidade_fileiras = (capacidade + colunas - 1) // colunas

    print("     ", end="")
    for numero in range(1, colunas + 1):
        print(f"{numero:^5}", end="")
    print()

    assento_atual = 0

    for i in range(quantidade_fileiras):

        print(f"{letras[i]} ", end=" ")

        for numero in range(1, colunas + 1):

            assento_atual += 1

            if assento_atual > capacidade:
                break

            assento = f"{letras[i]}{numero}"

            if assento in assentos_ocupados:
                print("[X]  ", end="")
            else:
                print("[ ]  ", end="")

        print()

    print("\n[X] = Ocupado")
    print("[ ] = Livre\n")

def vender_ingresso():

   if not sessoes:
      print("Nenhuma sessão cadastrada!")
      return

   print("\n=== SESSÕES DISPONÍVEIS ===")

   for sessao in sessoes:
      print(
         f"ID: {sessao['id']} | "
         f"Filme: {sessao['filme']} | "
         f"Horário: {sessao['horario']}"
      )

   id_sessao = int(input("Escolha a sessão: "))

   sessao_escolhida = None

   for sessao in sessoes:
      if sessao["id"] == id_sessao:
         sessao_escolhida = sessao
         break

   if sessao_escolhida is None:
      print("Sessão não encontrada!")
      return

   if sessao_escolhida["ocupados"] >= sessao_escolhida["capacidade"]:
      print("Sessão lotada!")
      return

   nome = input("Nome do cliente: ")
   cpf = input("CPF: ")
   
   assentos_ocupados = []

   for ingresso in ingressos:
      if ingresso["sessao"] == id_sessao:
         assentos_ocupados.append(ingresso["assento"])

   mostrar_assentos(sessao_escolhida["capacidade"], assentos_ocupados)

   assento = input("Escolha um assento: ").upper()

   assentos_validos = []

   colunas = 5
   letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

   quantidade_fileiras = (sessao_escolhida["capacidade"] + colunas - 1) // colunas

   contador = 0

   for i in range(quantidade_fileiras):
      for numero in range(1, colunas + 1):
         contador += 1

         if contador > sessao_escolhida["capacidade"]:
            break

         assentos_validos.append(f"{letras[i]}{numero}")

   if assento not in assentos_validos:
      print("Assento inválido!")
      return
   if assento in assentos_ocupados:
      print("Assento já vendido!")
      return


   valor = float(input("Valor do ingresso: "))

   ingresso = {
      "nome": nome,
      "cpf": cpf,
      "filme": sessao_escolhida["filme"],
      "sessao": id_sessao,
      "assento": assento,
      "valor": valor,
      "data": datetime.now().strftime("%d/%m/%Y")
   }

   ingressos.append(ingresso)

   sessao_escolhida["ocupados"] += 1

   salvar_dados()

   print("Ingresso vendido com sucesso!")


def listar_ingressos():

    if not ingressos:
        print("Nenhum ingresso vendido!")
        return

    print("\n=== INGRESSOS ===")

    for numero, ingresso in enumerate(ingressos, start=1):

        print(f"\nIngresso {numero}")
        print(f"Cliente: {ingresso['nome']}")
        print(f"CPF: {ingresso['cpf']}")
        print(f"Filme: {ingresso['filme']}")
        print(f"Sessão: {ingresso['sessao']}")
        print(f"Assento: {ingresso['assento']}")
        print(f"Valor: R$ {ingresso['valor']:.2f}")
        print(f"Data: {ingresso['data']}")


def cancelar_ingresso():

    cpf = input("CPF do cliente: ")

    for ingresso in ingressos:

        if ingresso["cpf"] == cpf:

            for sessao in sessoes:

                if sessao["id"] == ingresso["sessao"]:
                    sessao["ocupados"] -= 1
                    break

            ingressos.remove(ingresso)

            salvar_dados()

            print("Ingresso cancelado com sucesso!")
            return

    print("Ingresso não encontrado!")



def verificar_assentos():

    if not sessoes:
        print("Nenhuma sessão cadastrada!")
        return

    for sessao in sessoes:

        disponiveis = (
            sessao["capacidade"]
            - sessao["ocupados"]
        )

        print(
            f"Filme: {sessao['filme']} | "
            f"Horário: {sessao['horario']} | "
            f"Disponíveis: {disponiveis}"
        )
