import discord
import random
from discord.ext import commands

class Dado(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='rolldice')
    async def rolldice(self, ctx):
        quant_dados = 0
        lados = 0
        await ctx.send("How many dices?")
        msg = await self.bot.wait_for('message')
        mensagem = msg.content
        try:
            quant_dados = int(mensagem)
        except:
            await ctx.send("Incorrect parameter.")
        if quant_dados > 0 and quant_dados < 25:
            await ctx.send("Enter the amount of sides:")
            msg = await self.bot.wait_for('message')
            mensagem = msg.content
            try:
                lados = int(mensagem)
            except:
                await ctx.send("Incorrect parameter.")
        if lados > 0:
            dado = discord.Embed(
                title=f"""{quant_dados} D{lados} roll by {str(ctx.author)} :game_die: """,
                colour=discord.Colour.greyple()
            )
            total = 0
            soma = ""
            for i in range(quant_dados):
                num = random.randint(1, lados)
                dado.add_field(name=f"""Dice #{i + 1}""", value=num, inline=True)
                total += num
                soma += str(num) + " + "
            soma = soma[:len(soma) - 2]
            dado.description = f"""SUM: {soma} = **{total}**"""
            await ctx.send(embed=dado)
        else:
            await ctx.send(f"""You failed to roll the dice. Try Again.""")

    @commands.command(name='roll', aliases=['r'])
    async def fast_rolldice(self, ctx, dado):
        quant_dados = 0
        lados = 0
        try:
            for i in range(len(dado)):
                if dado[i].upper() == "D":
                    posicao_x = i
                    quant_dados = int(dado[:posicao_x])
                    if quant_dados > 0 and quant_dados < 25:
                        lados = int(dado[posicao_x + 1:len(dado)])
                    break
            if lados > 0:
                dado = discord.Embed(
                    title=f"""{quant_dados} D{lados} roll by {str(ctx.author)} :game_die: """,
                    colour=discord.Colour.greyple()
                )
                total = 0
                soma = ""
                for i in range(quant_dados):
                    num = random.randint(1, lados)
                    dado.add_field(name=f"""Dice #{i + 1}""", value=num, inline=True)
                    total += num
                    soma += str(num) + " + "
                soma = soma[:len(soma) - 2]
                dado.description = f"""SUM: {soma} = **{total}**"""
                await ctx.send(embed=dado)
        except:
            await ctx.send(f"""Incorrect parameters. Dices amount must be enter 1 and 25 / Dice sides must be integer and greater than 0.""")

    @classmethod
    async def rolagem_pronta(self, bot, canal, dados, lados):
        if (dados > 0 and dados < 25) and (lados > 0):
            dado = discord.Embed(
                title=f"""{dados} D{lados} roll by {canal.personagem.nome} :game_die: """,
                description="Click on the dice below to roll the dice.",
                colour=discord.Colour.greyple()
            )
            embed_dado = await canal.canal.send(embed=dado)
            await embed_dado.add_reaction(emoji='🎲')
            rolagem = 0
            while rolagem == 0:
                reaction, user = await bot.wait_for('reaction_add')
                if str(reaction.emoji) == '🎲' and str(user) == canal.personagem.dono:
                    rolagem = 1
                    await embed_dado.delete()
                    total = 0
                    soma = ""
                    dado1 = discord.Embed(
                        title=f"""{dados} D{lados} roll by {canal.personagem.nome} :game_die: """,
                        colour=discord.Colour.greyple()
                    )
                    for i in range(dados):
                        num = random.randint(1, lados)
                        dado1.add_field(name=f"""Dice #{i + 1}""", value=num, inline=True)
                        total += num
                        soma += str(num) + " + "
                    soma = soma[:len(soma) - 2]
                    dado1.description = f"""SUM: {soma} = **{total}**"""
                    await canal.canal.send(embed=dado1)
                    return total
        else:
            await canal.canal.send(f"""Incorrect parameters.""")

def setup(bot):
    bot.add_cog(Dado(bot))