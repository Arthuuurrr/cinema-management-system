""" Cadastrar salas
    Criar sessões
    Listar sessões
    Verificar capacidade da sala"""

def cadastrar_salas():
    sessoes=[]

    while True:

        salas=input("digite o numero da sua sala (ou sair):")

        if salas == "sair":
            break

        if salas not in sessoes:
            sessoes.append(salas)

        else:
            print("essa sala já existe!")

cadastrar_salas()

lista_sessoes=[]

while True:
    sessoess=input("digite o nome da sessão (0 pra fechar):")
    lista_sessoes.append(sessoess)
    if sessoess == "0":
       break
    elif sessoess in lista_sessoes:
        print(lista_sessoes)

""" pensei em fazer por lista e dicionario tlgd, pq uma sessao tem precisa de
uma sala, que tem uma capacidade de pessoas maxima dai no final tem que printar
as sessoes e as salas e os lugares disponiveis tlgd pq eu acho que mais pra frente
a gente vai ter que ir subtraindo o umero de lugares conforme as pessoas "chegam" pra
criar uma outra variavel com "lugares_disponiveis" mas resumindo eu acho que fica mais organizado 
com dicionarios dai, mas POR AGORA eu to vindo de cima pra maixo corrigindo esse codigo de baixo 
dai to tentando criar um dicionario chamado "lista_sessoes" e colocar
o dicionario "salas" dentro dele, ta cheio de erro tlgd e a parte de baixo do codigo é copiada do
codigo de cima pra eu arrumar dps de arrumar a parte de cima. La em baixo
vai ter que mudar tudo pq os bagulho tão 'solto' tlgd, dai tem que colocar no dicionario certo e pa
mas da linha 6 até a 14 eu tenho crtz que ta certo tlgd. Se tu quiser testar essa parte de
cima pra ver oque eu to falando vc exclui a linha 2 e 3 e toda a parte de baixo (linha 18 á 27) e 
testa pdp? 
esse é o codigo atual:


def cadastrar_salas():
    lista_sessoes={}
    lista_sessoes([salas])
    salas={}
    while True:
        nome_sala = input("digite o nome da sala (ou sair):")
        capacidade = (int(input("digite a capacidade desta sala:")))
        salas[nome_sala]= capacidade
        print("\nDicionário atualizado:")
        print(salas)
        if nome_sala == "sair":
            break
        elif nome_sala in salas:
            print("esta sala já existe!")


cadastrar_salas()

#parte de baixo
while True:

    sessoess=input("digite o nome da sessão (0 pra fechar):")
    salas[lista_sessoes]
    lista_sessoes.append(sessoess)
    if sessoess == "0":
       break
    elif sessoess in lista_sessoes:
        print(lista_sessoes)
"""

	

