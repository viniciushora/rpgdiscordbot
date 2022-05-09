class Sistema:
    def __init__(self, nome, vida, energiaPrincipal, outras_energias, status_primarios, status_personagem, status_iniciativa, status_movimento, status_secundarios, coeficienteLevel, classes, personagens, racas, itens, mapas, spells, skills, dinheiro_inicial, religioes, pericias, proeficiencias, linguas, alinhamentos):
        self.nome = nome
        self.vida = vida
        self.energiaPrincipal = energiaPrincipal
        self.outras_energias = outras_energias
        self.status_iniciativa = status_iniciativa
        self.status_movimento = status_movimento
        self.status_primarios = status_primarios
        self.status_personagem = status_personagem
        self.status_secundarios = status_secundarios
        self.coeficienteLevel = coeficienteLevel
        self.classes = classes
        self.personagens = personagens
        self.racas = racas
        self.itens = itens
        self.mapas = mapas
        self.spells = spells
        self.skills = skills
        self.dinheiro_inicial = dinheiro_inicial
        self.religioes = religioes
        self.pericias = pericias
        self.proeficiencias = proeficiencias
        self.nomes_moeda = []
        self.dinheiro_inicial = dinheiro_inicial
        self.linguas = linguas
        self.alinhamentos = alinhamentos
        self.personagens = []

    def add_personagem(self, personagem):
        self.personagens.append(personagem)

class SistemaGenerico:
    def __init__(self, nome, statusPersonagem, sigla_status_iniciativa):
        self.nome = nome
        self.statusPersonagem = statusPersonagem
        self.sigla_status_iniciativa = sigla_status_iniciativa
        self.personagens = []

    def add_personagem(self, personagem):
        self.personagens.append(personagem)
