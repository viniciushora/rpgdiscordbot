from cogs.rpg.exceptions import EfeitosMissingException,StatusNotFoundException

class Tipo:
    def __init__(self, ID, nome):
        self.ID = ID
        self.nome = nome

    def getNome(self):
        return self.nome

    def getID(self):
        return self.ID

    def setNome(self, nome):
        self.nome = nome

class Cura(Tipo):
    def __init__(self,ID,nome):
        Tipo.__init__(self,ID,nome)

    def curar(self,personagem,valor):
        personagem.aumentarVida(valor)

class Dano(Tipo):
    def __init__(self, ID, nome):
        Tipo.__init__(self, ID, nome)

    def causarDano(self, personagem, valor):
        personagem.diminuirVida(valor)

class Buff(Tipo):
    def __init__(self, ID, nome,status):
        Tipo.__init__(self, ID, nome)
        self.status = status

    def buffar(self, personagem, valor):
        try:
            for stat in self.status:
                personagem.aumentarStatus(valor, stat)
        except StatusNotFoundException:
            print()

    def retirarBuff(self, personagem, valor):
        try:
            for stat in self.status:
                personagem.diminuirStatus(valor, stat)
        except StatusNotFoundException:
            print()

class Debuff(Tipo):
    def __init__(self, ID, nome,status):
        Tipo.__init__(self, ID, nome)
        self.status = status

    def debuffar(self, personagem, valor):
        try:
            for stat in self.status:
                personagem.debuffarStatus(valor,stat)
        except StatusNotFoundException:
            print()

    def retirarDebuff(self, personagem,valor):
        try:
            for stat in self.status:
                personagem.diminuirStatus(valor, stat)
        except StatusNotFoundException:
            print()

class CC(Tipo):
    def __init__(self, ID, nome,efeitos):
        Tipo.__init__(self, ID, nome)
        self.efeitos = efeitos

    def aplicarEfeito(self, personagem):
        try:
            for efeito in self.efeitos:
                personagem.adicionarEfeito(efeito)
        except EfeitosMissingException:
            print()

    def fimEfeito(self, personagem):
        try:
            for efeito in self.efeitos:
                personagem.removerEfeito(efeito)
        except EfeitosMissingException:
            print()