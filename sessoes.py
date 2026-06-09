""" Cadastrar salas
    Criar sessões
    Listar sessões
    Verificar capacidade da sala"""

def cadastrar_salas():
    sessoes=[]

    while True:

        salas=input("digite o numero da sua sala?(ou sair)")

        if salas == "sair":
            break

        if salas not in sessoes:
            sessoes.append(salas)

        else:
            print("essa sala já existe!")

cadastrar_salas()

lista_sessoes=[]

while true
sessoes=input("digite o nome da sessão:(0 pra fechar)")
lista_sessoes.append(sessoes)
if sessoes == 0 
       break
for sessoes in sessoes
	print(sessoes)
"""eu joguei pro chat corrigir o codigo dai eu vou corrigir o meu com base no dele pra eu aprender namoral:
def cadastrar_salas():
    salas = {}
    while True:
        nome_sala = input("Digite o nome da sala (ou digite 'sair'): ").strip().lower()
        if nome_sala == 'sair':
            break
        
        if nome_sala in salas:
            print("Essa sala já existe!")
        else:
            try:
                capacidade = int(input(f"Digite a capacidade máxima da sala {nome_sala}: "))
                salas[nome_sala] = capacidade
                print(f"Sala {nome_sala} cadastrada com sucesso!\n")
            except ValueError:
                print("Por favor, digite um número válido para a capacidade.")
    return salas

def criar_sessoes(salas_disponiveis):
    sessoes = []
    while True:
        nome_sessao = input("Digite o nome da sessão (ou '0' para fechar): ").strip()
        if nome_sessao == '0':
            break
            
        if nome_sessao:
            sessoes.append(nome_sessao)
            print(f"Sessão '{nome_sessao}' adicionada.\n")
    return sessoes

def verificar_capacidade(salas):
    nome_sala = input("Verificar capacidade da sala: ").strip().lower()
    if nome_sala in salas:
        print(f"A capacidade da sala {nome_sala} é de {salas[nome_sala]} pessoas.\n")
    else:
        print("Sala não encontrada.\n")

# --- Fluxo Principal do Programa ---
print("--- Cadastro de Salas ---")
salas_cadastradas = cadastrar_salas()

if salas_cadastradas:
    print("\n--- Criação de Sessões ---")
    sessoes_criadas = criar_sessoes(salas_cadastradas)
    
    print("\n--- Listar Sessões ---")
    if sessoes_criadas:
        for s in sessoes_criadas:
            print(f"- {s}")
    else:
        print("Nenhuma sessão criada.")
    
    print("\n--- Verificar Capacidade ---")
    verificar_capacidade(salas_cadastradas)"""

	

