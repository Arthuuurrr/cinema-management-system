from cinema import carregar_dados

from filmes import cadastrar_filme, listar_filmes, editar_filme, remover_filme
from sessoes import cadastrar_salas, listar_salas, criar_sessoes, listar_sessoes, verificar_capacidade
from ingressos import vender_ingresso, listar_ingressos, cancelar_ingresso, verificar_assentos
from relatorios import total_ingressos, faturamento_total, filme_mais_assistido, relatorio_diario


def menu_filmes():
    while True:
        print("\n=== MÓDULO FILMES ===")
        print("1 - Cadastrar Filme")
        print("2 - Listar Filmes")
        print("3 - Editar Filme")
        print("4 - Remover Filme")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_filme()
        elif opcao == "2":
            listar_filmes()
        elif opcao == "3":
            editar_filme()
        elif opcao == "4":
            remover_filme()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


def menu_sessoes():
    while True:
        print("\n=== MÓDULO SALAS E SESSÕES ===")
        print("1 - Cadastrar Sala")
        print("2 - Listar Salas")
        print("3 - Criar Sessão")
        print("4 - Listar Sessões")
        print("5 - Verificar Capacidade da Sala")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_salas()
        elif opcao == "2":
            listar_salas()
        elif opcao == "3":
            criar_sessoes()
        elif opcao == "4":
            listar_sessoes()
        elif opcao == "5":
            verificar_capacidade()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


def menu_ingressos():
    while True:
        print("\n=== MÓDULO INGRESSOS ===")
        print("1 - Vender Ingresso")
        print("2 - Listar Ingressos")
        print("3 - Cancelar Ingresso")
        print("4 - Verificar Assentos Disponíveis")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            vender_ingresso()
        elif opcao == "2":
            listar_ingressos()
        elif opcao == "3":
            cancelar_ingresso()
        elif opcao == "4":
            verificar_assentos()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


def menu_relatorios():
    while True:
        print("\n=== MÓDULO RELATÓRIOS ===")
        print("1 - Total de Ingressos Vendidos")
        print("2 - Faturamento Total")
        print("3 - Filme Mais Assistido")
        print("4 - Relatório Diário")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            total_ingressos()
        elif opcao == "2":
            faturamento_total()
        elif opcao == "3":
            filme_mais_assistido()
        elif opcao == "4":
            relatorio_diario()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


def menu_principal():
    carregar_dados()

    while True:
        print("\n========== SISTEMA DE CINEMA ==========")
        print("1 - Filmes")
        print("2 - Salas e Sessões")
        print("3 - Ingressos")
        print("4 - Relatórios")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_filmes()
        elif opcao == "2":
            menu_sessoes()
        elif opcao == "3":
            menu_ingressos()
        elif opcao == "4":
            menu_relatorios()
        elif opcao == "0":
            print("Sistema encerrado!")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu_principal()
