import discord
from discord.ext import commands
from discord.utils import get

import asyncio
import itertools
import sys
import traceback
import youtube_dl
from async_timeout import timeout
from functools import partial

from cogs.rpg.dado import Dado

class Sessao:
    def __init__(self, ctx, personagens, mestre, sistema):
        self.sistema = sistema
        self.personagens = personagens
        self.mestre = mestre
        self.ctx = ctx
        self.bot = ctx.bot
        self._guild = ctx.guild
        self._cog = ctx.cog
        self.canais = []

    async def iniciar_sessao(self):
        await self._guild.create_category('RPG')
        category = discord.utils.get(self._guild.categories, name='RPG')
        mestre_nome = "master-" + self.mestre.nome.replace(" ", "-").lower()
        await self._guild.create_text_channel(mestre_nome, category=category)
        canal = discord.utils.get(self.bot.get_all_channels(), guild__name=self._guild.name, name=mestre_nome)
        c = Canal(canal, self.mestre)
        self.canais.append(c)
        for personagem in self.personagens:
            nome = personagem.nome.replace(" ", "-").lower()
            await self._guild.create_text_channel(nome, category=category)
            canal = discord.utils.get(self.bot.get_all_channels(), guild__name=self._guild.name, name=nome)
            c = Canal(canal, personagem)
            self.canais.append(c)

    async def terminar_sessao(self):
        categorias = self._guild.by_category()
        for categoria, canais in categorias:
            if str(categoria) == "RPG":
                for canal in canais:
                    await canal.delete()
                await categoria.delete()

    def get_personagem_canal(self, personagem):
        for canal in self.canais:
            if personagem == canal.personagem:
                return canal
        return False

    async def enviar_rolagem(self, ctx, dados, lados, personagem):
        if ctx.author == self.mestre.dono:
            canal = self.get_personagem_canal(personagem)
            resultado = await Dado.rolagem_pronta(self.bot, canal, dados, lados)
            return resultado
        return False

    async def seleciona_personagens(self, canal):
        participantes = []
        emoji = [":one:", ":two:", ":three:", ":four:", ":five:", ":six:", ":seven:", ":eight:", ":nine:", ":keycap_ten:"]
        emoji_raw = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
        paginas = len(self.personagens) // 10
        if paginas == 0:
            paginas = 1
        select = discord.Embed(
            title=f"""Choose the characters that will participate in the combat""",
            description="Select the character number and confirm or cancel the fight.",
            colour=discord.Colour.red()
        )
        tamanho = len(self.personagens)
        p = 1
        p_total = tamanho // 10
        n = ((p - 1) * 10)
        pagina_tamanho = 0
        concluido = False
        while not concluido:
            e = 0
            for k in range(10):
                if n < tamanho:
                    select.add_field(name=emoji[e], value=self.personagens[(10 * (p - 1)) + k].nome, inline=False)
                    n += 1
                    pagina_tamanho += 1
                    e += 1
            emb_msg = await canal.send(embed=select)
            for j in range(pagina_tamanho):
                await emb_msg.add_reaction(emoji=emoji_raw[j])
            await emb_msg.add_reaction(emoji="🇽")
            await emb_msg.add_reaction(emoji="✅")
            if p < p_total and p > 1:
                await emb_msg.add_reaction(emoji="⏮️️️")
                await emb_msg.add_reaction(emoji="⏭️️️")
            elif p == 1 and p < p_total:
                await emb_msg.add_reaction(emoji="⏭️️️️")
            elif p == p_total and p > 1:
                await emb_msg.add_reaction(emoji="⏮️")
            entra = 1
            while entra == 1:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=None)
                if str(user) == self.mestre.dono:
                    if str(reaction.emoji) == emoji_raw[0]:
                        participantes.append(self.personagens[(p * 10) - 10])
                    elif str(reaction.emoji) == emoji_raw[1]:
                        participantes.append(self.personagens[(p * 10) - 9])
                    elif str(reaction.emoji) == emoji_raw[2]:
                        participantes.append(self.personagens[(p * 10) - 8])
                    elif str(reaction.emoji) == emoji_raw[3]:
                        participantes.append(self.personagens[(p * 10) - 7])
                    elif str(reaction.emoji) == emoji_raw[4]:
                        participantes.append(self.personagens[(p * 10) - 6])
                    elif str(reaction.emoji) == emoji_raw[5]:
                        participantes.append(self.personagens[(p * 10) - 5])
                    elif str(reaction.emoji) == emoji_raw[6]:
                        participantes.append(self.personagens[(p * 10) - 4])
                    elif str(reaction.emoji) == emoji_raw[7]:
                        participantes.append(self.personagens[(p * 10) - 3])
                    elif str(reaction.emoji) == emoji_raw[8]:
                        participantes.append(self.personagens[(p * 10) - 2])
                    elif str(reaction.emoji) == emoji_raw[9]:
                        participantes.append(self.personagens[(p * 10) - 1])
                    elif str(reaction.emoji) == "⏮️":
                        entra = 0
                        await emb_msg.delete()
                        p -= 1
                    elif str(reaction.emoji) == "⏭️":
                        entra = 0
                        await emb_msg.delete()
                        p += 1
                    elif str(reaction.emoji) == "🇽":
                        participantes = []
                        await emb_msg.delete()
                        entra = 0
                        concluido = True
                    elif str(reaction.emoji) == "✅":
                        await emb_msg.delete()
                        concluido = True
                        entra = 0
                        if participantes != []:
                            texto = "**Selected characters:** "
                            for p in participantes:
                                texto += p.nome + " - "
                            texto = texto[:len(texto)-2]
                            await canal.send(texto)
        return participantes

class Canal:
    def __init__(self, canal, personagem):
        self.canal = canal
        self.personagem = personagem

    def getCanal(self):
        return self.canal

    def pode_escrever(self, ctx):
        if ctx.author == self.personagem.getDono():
            return True
        return False







