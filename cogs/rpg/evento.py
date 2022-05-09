from cogs.rpg.dado import Dado
import discord

class Evento:
    def __init__(self, nome, sessao):
        self.nome = nome
        self.log = []
        self.sessao = sessao

class Combate(Evento):
    def __init__(self, nome, sessao, mestre, personagens, npcs, mapa):
        Evento.__init__(self, nome, sessao)
        self.mestre = mestre
        self.personagens = personagens
        self.ordem_de_jogada = []
        #self.npcs = npcs
        #self.mapa = mapa

    async def calcular_iniciativa(self, bot):
        iniciativas = []
        for personagem in self.personagens:
            canal = self.sessao.get_personagem_canal(personagem)
            await canal.canal.send(self.sessao.sistema.statusPersonagem[self.sessao.sistema.sigla_status_iniciativa] + " roll by " + personagem.nome)
            ini_inicial = personagem.status[self.sessao.sistema.sigla_status_iniciativa]
            iniciativa = await Dado.rolagem_pronta(bot, canal, 1,20) + ini_inicial
            await canal.canal.send(personagem.nome + "'s " + self.sessao.sistema.statusPersonagem[self.sessao.sistema.sigla_status_iniciativa] + " = " + str(iniciativa - ini_inicial) + " + " + str(ini_inicial) + " = " + str(iniciativa))
            if iniciativas == []:
                iniciativas.append(iniciativa)
                self.ordem_de_jogada.append(personagem)
            else:
                k = 0
                for i in iniciativas:
                    if iniciativa >= i:
                        k += 1
                if k > len(iniciativas):
                    iniciativas.insert(k,iniciativa)
                    self.ordem_de_jogada.insert(k, personagem)
                else:
                    iniciativas.append(iniciativa)
                    self.ordem_de_jogada.append(personagem)
        result = discord.Embed(
            title=f"""**Attack order** :crossed_swords:""",
            colour=discord.Colour.red()
        )
        i = 1
        canal_mestre = self.sessao.get_personagem_canal(self.mestre)
        for p in self.ordem_de_jogada:
            result.add_field(name="**" + str(i) + ". " + p.nome + "**", value=self.sessao.sistema.statusPersonagem[self.sessao.sistema.sigla_status_iniciativa] + " = " + str(iniciativas[i-1]), inline=False)
            i += 1
        await canal_mestre.canal.send(embed=result)

class Dia(Evento):
    def __init__(self, nome, sessao, data):
        Evento.__init__(self, nome, sessao)
        self.data = data

class Noite(Evento):
    def __init__(self, nome, sessao, data):
        Evento.__init__(self, nome, sessao)
        self.data = data

class CriacaoDeItem(Evento):
    def __init__(self, nome, sessao, personagem, chance):
        Evento.__init__(self, nome, sessao)
        self.personagem = personagem
        self.chance = chance



