class Cache:
    def __init__(self):
        self.dados = {}

    def adicionar_dados(self, nome, conteudo):
        self.dados[nome] = conteudo