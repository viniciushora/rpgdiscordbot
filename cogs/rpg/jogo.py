import discord
from discord.ext import commands
import random
from cogs.rpg.char import *
from cogs.rpg.sessao import *
from cogs.rpg.evento import *
from cogs.rpg.sistema import *

import pickle
import io
import youtube_dl
import os
from discord.utils import get
import logging
import asyncio

sessoes = {}

class Jogo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sessao(self, ctx):
        guild_id = ctx.guild.id
        if guild_id not in sessoes:
            mestre = Mestre(1, "Daciolo", "Vinicius#0112")
            sistema = SistemaGenerico("Ailian", {"ini": "Iniciativa"}, "ini")
            p1 = PersonagemGenerico("Minguado", {"ini":10}, "Vinicius#0112")
            p2 = PersonagemGenerico("Gustavo Cirstão", {"ini":12}, "Vinicius#0112")
            sistema.add_personagem(p1)
            sistema.add_personagem(p2)
            personagens = [p1, p2]
            s = Sessao(ctx, personagens, mestre, sistema)
            await s.iniciar_sessao()
            sessoes[guild_id] = s
        else:
            await ctx.send("**Session already started.**")

    @commands.command()
    async def combate(self, ctx):
        guild_id = ctx.guild.id
        if guild_id in sessoes:
            sessao = sessoes[guild_id]
            canal = sessao.get_personagem_canal(sessao.mestre)
            personagens = await sessao.seleciona_personagens(canal.canal)
            if personagens != []:
                c = Combate("Combate teste", sessao, sessao.mestre, personagens, 0 , 0)
                await c.calcular_iniciativa(self.bot)
            else:
                await ctx.send("**No characters selected.**")
        else:
            await ctx.send("**You need to start a session before.**")

    @commands.command()
    async def terminar_sessao(self,ctx):
        guild_id = ctx.guild.id
        if guild_id in sessoes:
            sessao = sessoes[guild_id]
            await sessao.terminar_sessao()
            del sessoes[guild_id]
        else:
            await ctx.send("**Session not found.**")


def setup(bot):
    bot.add_cog(Jogo(bot))
