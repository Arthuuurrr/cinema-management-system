""" Mostrar total de ingressos vendidos
    Calcular faturamento total
    Exibir filme mais assistido
    Gerar relatório diário  """
 
while True:
    print("\n=== RELATÓRIOS ===")
    print("1 - Total de ingressos vendidos")
    print("0 - Voltar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        total_ingressos() #ainda nao fiz o total_ingressos(), mas vai usar ela pra fazer

    elif opcao == "0":
        break

    else:
        print("Opção inválida!")
