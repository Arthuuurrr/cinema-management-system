import pickle

ARQUIVO = "cinema.pkl"

filmes = []
salas = []
sessoes = []
ingressos = []


def salvar_dados():
    dados = {
        "filmes": filmes,
        "salas": salas,
        "sessoes": sessoes,
        "ingressos": ingressos
    }

    with open(ARQUIVO, "wb") as arquivo:
        pickle.dump(dados, arquivo)


def carregar_dados():
    try:
        with open(ARQUIVO, "rb") as arquivo:
            dados = pickle.load(arquivo)

            filmes.clear()
            filmes.extend(dados.get("filmes", []))

            salas.clear()
            salas.extend(dados.get("salas", []))

            sessoes.clear()
            sessoes.extend(dados.get("sessoes", []))

            ingressos.clear()
            ingressos.extend(dados.get("ingressos", []))

    except FileNotFoundError:
        pass
        
