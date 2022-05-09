class Religiao:
    def __init__(self, nome, subtitulo, simbolo, dogmas, pecados, bencao, oracao):
        self.nome = nome
        self.subtitulo = subtitulo
        self.simbolo = simbolo
        self.dogmas = dogmas
        self.pecados = pecados
        self.bencao = bencao
        self.oracao = oracao

    def return_religiao(self):
        r = {"nome": self.nome, "subtitulo": self.subtitulo, "simbolo": self.simbolo, "dogmas": self.dogmas, "pecados": self.pecados, "bencao": self.bencao, "oracao": self.oracao}
        return r