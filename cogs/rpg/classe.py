class Classe:
    def __init__(self,nome,foto,dadoVida,tipoClasse,descricao,fonteDePoder,vantagens,habilidades,):
        self.nome = nome
        self.foto = foto
        self.dadoVida = dadoVida
        self.tipoClasse = tipoClasse
        self.descricao = descricao
        self.fonteDePoder = fonteDePoder
        self.vantagens = vantagens
        self.habilidades = habilidades

    def getNome(self):
        return self.nome

    def getFoto(self):
        return self.foto

    def getDadoVida(self):
        return self.dadoVida

    def getTipoClasse(self):
        return self.tipoClasse

    def getDescricao(self):
        return self.descricao

    def getFonteDePoder(self):
        return self.fonteDePoder

    def getVantagens(self):
        return self.vantagens

    def getHabilidades(self):
        return self.habilidades

    def setNome(self,nome):
        self.nome = nome

    def setFoto(self,foto):
        self.foto = foto

    def setDadoVida(self,dadoVida):
        self.dadoVida = dadoVida

    def setTipoClasse(self,tipoClasse):
        self.tipoClasse = tipoClasse

    def setDescricao(self,descricao):
        self.descricao = descricao

    def setFonteDePoder(self):
        return self.fonteDePoder

    def setVantagens(self,vantagens):
        self.vantagens = vantagens

    def setHabilidades(self,habilidades):
        self.habilidades = habilidades