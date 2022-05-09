from cogs.rpg.efeito import EfeitoDPS

class Char:
    def __init__(self, ID, nome, dono):
        self.ID = ID
        self.nome = nome
        self.dono = dono

    def getID(self):
        return self.ID

    def getNome(self):
        return self.nome

    def getDono(self):
        return self.dono

    def setID(self,ID):
        self.ID = ID

    def setNome(self,nome):
        self.nome = nome

class Mestre(Char):
    def __init__(self, ID, nome, dono):
        Char.__init__(self, ID, nome, dono)

class Personagem(Char):
    def __init__(self, sistema, ID, nome,dono,raca,classes,vida,energia, tamanho,religiao,spells,atributos, status, char_status, def_status, pericias, foto, proeficiencias, linguas):
        Char.__init__(self, ID, nome,dono)
        self.foto = foto
        self.sistema = sistema
        self.raca = raca
        self.classes = classes
        self.atributos = atributos
        self.status = status
        self.char_status = char_status
        self.def_status = def_status
        self.vidaMax = vida
        self.vida = self.vidaMax
        self.energia = energia
        self.efeitos = {}
        self.buffs = {}
        self.debuffs = {}
        self.spells = spells
        self.podeAtacar = True
        self.vivo = True
        self.podeUsarSpells = True
        self.podeUsarSkills = True
        self.podeSeMover = True
        self.tamanho = tamanho
        self.religiao = religiao
        self.inventario = {1:[], 2:[], 3:[]}
        self.pericias = pericias
        self.proeficiencias = proeficiencias
        self.dinheiro = sistema.dinheiro_inicial
        self.linguas = linguas
        self.mudanca_dado = 0

    def getSpells(self):
        return self.spells

    def aumentarVida(self,valor):
        if self.vida + valor > self.vidaMax:
            self.vida = self.vidaMax
        else:
            self.vida = self.vida + valor

    def diminuirVida(self,valor):
        self.vida = self.vida - valor

    def aumentarVidaMax(self,valor):
        self.vidaMax += valor

    def diminuirVidaMax(self,valor):
        self.vidaMax -= valor

    def usarSpell(self,spell,dado,alvo):
        spell.ligarSpell(alvo,dado)

    def desativarSpell(self,spell,dado,alvo):
        spell.desligarSpell(alvo,dado)

    def aumentarStatus(self,valor,status):
        self.status[status] = self.status[status] + valor

    def diminuirStatus(self,valor,status):
        self.status[status] = self.status[status] - valor

    def adicionarEfeito(self,efeito,numTurnos):
        self.efeitos[efeito] = numTurnos
        efeito.aplicarEfeito(self)

    def removerEfeito(self,efeito):
        del self.efeitos[efeito]

    def atualizarContador(self):
        for chave in self.efeitos:
            if isinstance(chave,EfeitoDPS):
                dano = chave.danoDeTurno()
                self.diminuirVida(dano)
            self.efeitos[chave] =- 1
            if self.efeitos[chave] == 0:
                chave.desaplicarEfeito(self)
                self.removerEfeito(chave)

    def setPodeAtacar(self,pode):
        self.podeAtacar = pode;

    def setPodeSeMover(self,pode):
        self.podeSeMover = pode;

    def setPodeUsarSpells(self,pode):
        self.podeUsarSpells = pode;

    def setPodeUsarSkills(self,pode):
        self.podeUsarSkills = pode;

    def setPresenca(self,presenca):
        self.vivo = presenca;

class PersonagemGenerico:
    def __init__(self, nome, status, dono):
        self.nome = nome
        self.status = status
        self.dono = dono