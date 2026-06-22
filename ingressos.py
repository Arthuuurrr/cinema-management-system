from cinema import ingressos, sessoes, salvar_dados
from datetime import datetime
import tkinter as tk


def escolher_assento_tkinter(capacidade, assentos_ocupados):
    assento_escolhido = {"valor": None}

    janela = tk.Tk()
    janela.title("Escolha de Assento")

    colunas = 5
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    quantidade_fileiras = (capacidade + colunas - 1) // colunas

    contador = 0

    def selecionar_assento(assento):
        assento_escolhido["valor"] = assento
        janela.destroy()

    titulo = tk.Label(janela, text="Escolha seu assento", font=("Arial", 16, "bold"))
    titulo.grid(row=0, column=0, columnspan=colunas, pady=10)

    legenda = tk.Label(janela, text="[X] = Ocupado | Clique em um assento livre")
    legenda.grid(row=1, column=0, columnspan=colunas, pady=5)

    for i in range(quantidade_fileiras):
        for numero in range(1, colunas + 1):
            contador += 1

            if contador > capacidade:
                break

            assento = f"{letras[i]}{numero}"

            botao = tk.Button(
                janela,
                text=assento,
                width=6,
                height=2,
                command=lambda a=assento: selecionar_assento(a)
            )

            if assento in assentos_ocupados:
                botao.config(state="disabled", text="X")

            botao.grid(row=i + 2, column=numero - 1, padx=5, pady=5)

    janela.mainloop()

    return assento_escolhido["valor"]


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

    assento = escolher_assento_tkinter(
        sessao_escolhida["capacidade"],
        assentos_ocupados
    )

    if assento is None:
        print("Nenhum assento escolhido!")
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
        disponiveis = sessao["capacidade"] - sessao["ocupados"]

        print(
            f"Filme: {sessao['filme']} | "
            f"Horário: {sessao['horario']} | "
            f"Disponíveis: {disponiveis}"
        )
