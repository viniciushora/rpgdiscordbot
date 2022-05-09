from cogs.rpg.exceptions import RegrasMissingException

class Efeito:
    def __init__(self, ID, nome, descricao,regras):
        self.ID = ID
        self.nome = nome
        self.descricao = descricao
        self.regras = regras
        self.contador = 1

    def aplicarEfeito(self,personagem):
        try:
            for regra in self.regras:
                if regra == "naoPodeAtacar":
                    personagem.setPodeAtacar(False)
                elif regra == "naoPodeSeMover":
                    personagem.setPodeSeMover(False)
                elif regra == "naoPodeUsarSkills":
                    personagem.setPodeUsarSkills(False)
                elif regra == "naoPodeUsarSpells":
                    personagem.setPodeUsarSpells(False)
        except RegrasMissingException:
            print()

    def desaplicarEfeito(self,personagem):
        try:
            for regra in self.regras:
                if regra == "naoPodeAtacar":
                    personagem.setPodeAtacar(True)
                elif regra == "naoPodeSeMover":
                    personagem.setPodeSeMover(True)
                elif regra == "naoPodeUsarSkills":
                    personagem.setPodeUsarSkills(True)
                elif regra == "naoPodeUsarSpells":
                    personagem.setPodeUsarSpells(True)
        except RegrasMissingException:
            print()

class EfeitoDPS(Efeito):
    def __init__(self, ID, nome, descricao, regras, dano, coefDano):
        Efeito.__init__(self, ID, nome, descricao, regras)
        self.dano = dano
        self.coefDano = coefDano

    def danoDeTurno(self):
        dano = self.dano
        self.dano = self.dano + self.contador * self.coefDano
        self.contador += 1
        return dano
