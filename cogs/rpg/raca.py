class Raca:
    def __init__(self,nome,foto,descricao,idadeMax,tendencias,tamanho,motivacoes,vantagens,habilidades,aumento_atributos):
        self.nome = nome
        self.foto = foto
        self.descricao = descricao
        self.idadeMax = idadeMax
        self.tendencias = tendencias
        self.tamanho = tamanho
        self.aumento_atributos = aumento_atributos
        self.motivacoes = motivacoes
        self.vantagens = vantagens
        self.habilidades = habilidades

    def getNome(self):
        return self.nome

    def getFoto(self):
        return self.foto

    def getDescricao(self):
        return self.descricao

    def getIdadeMax(self):
        return self.idadeMax

    def getTendencias(self):
        return self.tendencias

    def getTamanho(self):
        return self.tamanho

    def getMotivacoes(self):
        return self.motivacoes

    def getVantagens(self):
        return self.vantagens

    def getHabilidades(self):
        return self.habilidades

    def setNome(self,nome):
        self.nome = nome

    def setFoto(self,foto):
        self.foto = foto

    def setDescricao(self,descricao):
        self.descricao = descricao

    def setIdadeMax(self,idadeMax):
        self.idadeMax = idadeMax

    def setTendencias(self,tendencias):
        self.tendencias = tendencias

    def setTamanho(self,tamanho):
        self.tamanho = tamanho

    def setMotivacoes(self,motivacoes):
        self.motivacoes = motivacoes

    def setVantagens(self,vantagens):
        self.vantagens = vantagens

    def getHabilidades(self,habilidades):
        self.habilidades = habilidades
