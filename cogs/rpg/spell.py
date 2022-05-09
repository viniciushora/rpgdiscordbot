from cogs.rpg.tipo import Tipo,Cura,Buff,Debuff,Dano,CC
import discord

class Spell:
    def __init__(self, ID, nome, descricao, tipos, numTurnos, dado, quantDados, custo, eventos):
        self.ID = ID
        self.nome = nome
        self.descricao = descricao
        self.numTurnos = numTurnos
        self.tipos = tipos
        self.dado = dado
        self.quantDados = quantDados
        self.custo = custo
        self.eventos = eventos

    def setNome(self,nome):
        self.nome = nome

    def setDescricao(self,descricao):
        self.descricao = descricao

    def setDado(self,dado):
        self.dado = dado

    def setQuantDados(self,quantDados):
        self.quantDados = quantDados

    def addTipo(self,tipo):
        self.tipos.append(tipo)

    def delTipo(self,tipo):
        for i in range(len(self.tipos)):
            if self.tipos[i].getID() == tipo:
                del(self.tipos[i])

    def nomesTipos(self):
        tipos = ""
        for tipo in self.tipos:
            tipos += tipo.getNome() + ", "
        tipos = tipos[:len(tipos)-2]
        return tipos

    def nomesEfeitos(self):
        efeitos = ""
        for t in self.tipos:
            if isinstance(t, CC):
                for efeito in t.efeitos:
                    efeito += efeito.getNome() + ", "
        efeitos = efeitos[:len(efeitos) - 2]
        return efeitos

    def ligarSpell(self,alvo,valor):
        for tipo in self.tipos:
            if isinstance(tipo,Cura):
                tipo.curar(alvo,valor)
            elif isinstance(tipo,Dano):
                tipo.causarDano(alvo,valor)
            elif isinstance(tipo,Buff):
                tipo.buffar(alvo,valor)
            elif isinstance(tipo,Debuff):
                tipo.debuffar(alvo,valor)
            elif isinstance(tipo,CC):
                tipo.aplicarEfeito(alvo,valor)

    def desligarSpell(self,alvo,valor):
        for tipo in self.tipos:
            if isinstance(tipo,Buff):
                tipo.retirarBuff(alvo,valor)
            elif isinstance(tipo,Debuff):
                tipo.retirarDebuff(alvo,valor)
            elif isinstance(tipo,CC):
                tipo.fimEfeito(alvo,valor)

    async def descricaoSpell(self,ctx):
        embed = discord.Embed(
            title=self.nome,
            description=self.descricao,
            colour=discord.Colour.blue()
        )
        embed.add_field(name="**ID**", value=self.ID, inline=False)
        embed.add_field(name="**Tipos**", value=self.nomesTipos(), inline=False)
        embed.add_field(name="**Efeitos**", value=self.nomesEfeitos(), inline=False)
        embed.add_field(name="**Dado**", value="D"+str(self.dado), inline=False)
        embed.add_field(name="**Quantidade de dados**", value=str(self.quantDados), inline=False)
        await ctx.send(embed=embed)