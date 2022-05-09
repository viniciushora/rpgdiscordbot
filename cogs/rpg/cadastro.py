from discord.ext import commands
from cogs.rpg.exceptions import ConteudoInvalidoException
from cogs.cache import Cache
import discord

caches = {}

class Cadastro(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'new_system')
    async def cadastro_sistema_command(self,ctx):
        campos_txt = ["Name", "Level Coefficient", "Life", "Energy", "Other Energies", "Main Status", "Iniciative Status", "Moviment Status", "Character Status", "Secondary Status"]
        campos_raw = ["nome", "coeficiente_level", "vida", "energia", "outras_energias", "status_primarios",  "status_iniciativa", "status_movimento", "status_personagem", "status_secundarios"]
        guild_id = ctx.guild.id
        if guild_id not in caches:
            c = Cache()
            caches[ctx.guild.id] = c
        try:
            c = caches[guild_id]
            msg = await self.status_registro(ctx, c, campos_txt, campos_raw)
            if "nome" not in c.dados:
                m1 = await ctx.send("What's the RPG System name?")
                nome = await self.bot.wait_for('message', check=self.check(ctx.author))
                if nome.content == "" or nome.content == " ":
                    raise ConteudoInvalidoException("Invalid System's name.")
                c.adicionar_dados("nome",nome.content)
                msgs = [m1,nome]
                await self.deletar_mensagens(msgs)
                await self.status_registro(ctx, c, campos_txt, campos_raw, msg)
            if "coeficiente_level" not in c.dados:
                m1 = await ctx.send("What's the RPG System level coefficient?")
                coef = await self.bot.wait_for('message', check=self.check(ctx.author))
                if coef.content == "" or coef.content == " ":
                    raise ConteudoInvalidoException("Invalid Level Coefficient.")
                coef_level = int(coef.content)
                if coef_level <= 0:
                    raise ConteudoInvalidoException("Invalid Level Coefficient.")
                c.adicionar_dados("coeficiente_level", coef_level)
                msgs = [m1,coef]
                await self.deletar_mensagens(msgs)
                await self.status_registro(ctx, c, campos_txt, campos_raw, msg)
            if "vida" not in c.dados:
                m1 = await ctx.send("What's the name of the characters' health?")
                vida_nome = await self.bot.wait_for('message', check=self.check(ctx.author))
                if vida_nome.content == "" or vida_nome.content == " ":
                    raise ConteudoInvalidoException("Invalid System's characters' health name.")
                m2 = await ctx.send("What's the initials of the characters' health?")
                vida_sigla = await self.bot.wait_for('message', check=self.check(ctx.author))
                if vida_sigla.content == "" or vida_sigla.content == " ":
                    raise ConteudoInvalidoException("Invalid System's characters' health initials.")
                vida = (vida_nome.content, vida_sigla.content)
                c.adicionar_dados("vida", vida)
                msgs = [m1, m2, vida_nome, vida_sigla]
                await self.deletar_mensagens(msgs)
                await self.status_registro(ctx, c, campos_txt, campos_raw, msg)
            if "energia" not in c.dados:
                m1 = await ctx.send("What's the name of the main energy of the system?")
                energia_nome = await self.bot.wait_for('message', check=self.check(ctx.author))
                if energia_nome.content == "" or energia_nome.content == " ":
                    raise ConteudoInvalidoException("Invalid System's main energy name.")
                m2 = await ctx.send("What's the initials of the main energy of the system?")
                energia_sigla = await self.bot.wait_for('message', check=self.check(ctx.author))
                if energia_sigla.content == "" or energia_sigla.content == " ":
                    raise ConteudoInvalidoException("Invalid System's main energy initials.")
                energia = (energia_nome.content, energia_sigla.content)
                c.adicionar_dados("energia", energia)
                msgs = [m1, m2, energia_nome, energia_sigla]
                await self.deletar_mensagens(msgs)
                await self.status_registro(ctx, c, campos_txt, campos_raw, msg)
            if "outras_energias" not in c.dados:
                outras_energias = []
                msgs = []
                m1 = await ctx.send("Are there other types of energies in your system? <Type 'y' for yes>")
                msgs.append(m1)
                choose = await self.bot.wait_for('message', check=self.check(ctx.author))
                msgs.append(choose)
                if choose.content == "" or choose.content == " ":
                    raise ConteudoInvalidoException("Invalid choose")
                while choose.content == "Y" or choose.content == "y":
                    m = await ctx.send("What's the energy name?")
                    msgs.append(m)
                    energia_nome = await self.bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(energia_nome)
                    if energia_nome.content == "" or energia_nome.content == " ":
                        raise ConteudoInvalidoException("Invalid System's main energy name.")
                    m = await ctx.send("What's the initials of the main energy of the system?")
                    msgs.append(m)
                    energia_sigla = await self.bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(energia_sigla)
                    if energia_sigla.content == "" or energia_sigla.content == " ":
                        raise ConteudoInvalidoException("Invalid System's main energy initials.")
                    energia = (energia_nome.content, energia_sigla.content)
                    outras_energias.append(energia)
                    m = await ctx.send("Are there other types of energies in your system? <Type 'y' for yes>")
                    msgs.append(m)
                    choose = await self.bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(choose)
                    if choose.content == "" or choose.content == " ":
                        raise ConteudoInvalidoException("Invalid choose")
                c.adicionar_dados("outras_energias", outras_energias)
                await self.status_registro(ctx, c, campos_txt, campos_raw, msg)
                await self.deletar_mensagens(msgs)
            if "status_primarios" not in c.dados:
                status_primarios = {}
                msgs = []
                m = await ctx.send("Enter the name of a main status:")
                msgs.append(m)
                status_nome = await self.bot.wait_for('message', check=self.check(ctx.author))
                msgs.append(status_nome)
                if status_nome.content == "" or status_nome.content == " ":
                    raise ConteudoInvalidoException("Invalid status name.")
                m = await ctx.send("Enter the initials of a main status:")
                msgs.append(m)
                status_sigla = await self.bot.wait_for('message', check=self.check(ctx.author))
                msgs.append(status_sigla)
                if status_sigla.content == "" or status_sigla.content == " ":
                    raise ConteudoInvalidoException("Invalid System's main status initials.")
                status_primarios[status_sigla.content] = status_nome.content
                m = await ctx.send("Are there other types of main status in your system? <Type 'y' for yes>")
                msgs.append(m)
                choose = await self.bot.wait_for('message', check=self.check(ctx.author))
                msgs.append(choose)
                if choose.content == "" or choose.content == " ":
                    raise ConteudoInvalidoException("Invalid choose")
                while choose.content == "Y" or choose.content == "y":
                    m = await ctx.send("Enter the name of a main status:")
                    msgs.append(m)
                    status_nome = await self.bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(status_nome)
                    if status_nome.content == "" or status_nome.content == " ":
                        raise ConteudoInvalidoException("Invalid status name.")
                    m = await ctx.send("Enter the initials of a main status:")
                    msgs.append(m)
                    status_sigla = await self.bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(status_sigla)
                    if status_sigla.content == "" or status_sigla.content == " ":
                        raise ConteudoInvalidoException("Invalid System's main status initials.")
                    status_primarios[status_sigla.content] = status_nome.content
                    m = await ctx.send("Are there other types of main status in your system? <Type 'y' for yes>")
                    msgs.append(m)
                    choose = await self.bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(choose)
                c.adicionar_dados("status_primarios", status_primarios)
                await self.status_registro(ctx, c, campos_txt, campos_raw, msg)
                await self.deletar_mensagens(msgs)
            if "status_personagem" not in c.dados:
                status_personagem = {}
                if "status_iniciativa" not in c.dados:
                    msgs = []
                    m = await ctx.send("Enter the name of a character iniciative status:")
                    msgs.append(m)
                    status_nome = await self.bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(status_nome)
                    if status_nome.content == "" or status_nome.content == " ":
                        raise ConteudoInvalidoException("Invalid status name.")
                    m = await ctx.send("Enter the initials of a character iniciative status:")
                    msgs.append(m)
                    status_sigla = await self.bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(status_sigla)
                    if status_sigla.content == "" or status_sigla.content == " ":
                        raise ConteudoInvalidoException("Invalid System's character status initials.")
                    status_iniciativa = (status_nome.content,status_sigla.content)
                    c.adicionar_dados("status_iniciativa", status_iniciativa)
                    await self.status_registro(ctx, c, campos_txt, campos_raw, msg)
                    await self.deletar_mensagens(msgs)
                if "status_movimento" not in c.dados:
                    msgs = []
                    m = await ctx.send("Enter the name of a character moviment status:")
                    msgs.append(m)
                    status_nome = await self.bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(status_nome)
                    if status_nome.content == "" or status_nome.content == " ":
                        raise ConteudoInvalidoException("Invalid status name.")
                    m = await ctx.send("Enter the initials of a character moviment status:")
                    msgs.append(m)
                    status_sigla = await self.bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(status_sigla)
                    if status_sigla.content == "" or status_sigla.content == " ":
                        raise ConteudoInvalidoException("Invalid System's character status initials.")
                    status_iniciativa = (status_nome.content,status_sigla.content)
                    c.adicionar_dados("status_movimento", status_iniciativa)
                    await self.status_registro(ctx, c, campos_txt, campos_raw, msg)
                    await self.deletar_mensagens(msgs)
                msgs = []
                m = await ctx.send("Enter the name of a character status:")
                msgs.append(m)
                status_nome = await self.bot.wait_for('message', check=self.check(ctx.author))
                msgs.append(status_nome)
                if status_nome.content == "" or status_nome.content == " ":
                    raise ConteudoInvalidoException("Invalid status name.")
                m = await ctx.send("Enter the initials of a character status:")
                msgs.append(m)
                status_sigla = await self.bot.wait_for('message', check=self.check(ctx.author))
                msgs.append(status_sigla)
                if status_sigla.content == "" or status_sigla.content == " ":
                    raise ConteudoInvalidoException("Invalid System's character status initials.")
                status_personagem[status_sigla.content] = status_nome.content
                m = await ctx.send("Are there other types of character status in your system? <Type 'y' for yes>")
                msgs.append(m)
                choose = await self.bot.wait_for('message', check=self.check(ctx.author))
                msgs.append(choose)
                if choose.content == "" or choose.content == " ":
                    raise ConteudoInvalidoException("Invalid choose")
                while choose.content == "Y" or choose.content == "y":
                    m = await ctx.send("Enter the name of a character status:")
                    msgs.append(m)
                    status_nome = await self.bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(status_nome)
                    if status_nome.content == "" or status_nome.content == " ":
                        raise ConteudoInvalidoException("Invalid character name.")
                    m = await ctx.send("Enter the initials of a character status:")
                    msgs.append(m)
                    status_sigla = await self.bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(status_sigla)
                    if status_sigla.content == "" or status_sigla.content == " ":
                        raise ConteudoInvalidoException("Invalid System's character status initials.")
                    status_personagem[status_sigla.content] = status_nome.content
                    m = await ctx.send("Are there other types of character status in your system? <Type 'y' for yes>")
                    msgs.append(m)
                    choose = await self.bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(choose)
                c.adicionar_dados("status_personagem", status_personagem)
                await self.status_registro(ctx, c, campos_txt, campos_raw, msg)
                await self.deletar_mensagens(msgs)
                del caches[guild_id]
            if "status_secundarios" not in c.dados:
                status_secundarios = {}
                msgs = []
                m = await ctx.send("Enter the name of a secondary status:")
                msgs.append(m)
                status_nome = await self.bot.wait_for('message', check=self.check(ctx.author))
                msgs.append(status_nome)
                if status_nome.content == "" or status_nome.content == " ":
                    raise ConteudoInvalidoException("Invalid status name.")
                m = await ctx.send("Enter the initials of a secondary status:")
                msgs.append(m)
                status_sigla = await self.bot.wait_for('message', check=self.check(ctx.author))
                msgs.append(status_sigla)
                if status_sigla.content == "" or status_sigla.content == " ":
                    raise ConteudoInvalidoException("Invalid System's status initials.")
                status_secundarios[status_sigla.content] = status_nome.content
                m = await ctx.send("Are there other types of secondary status in your system? <Type 'y' for yes>")
                msgs.append(m)
                choose = await self.bot.wait_for('message', check=self.check(ctx.author))
                msgs.append(choose)
                if choose.content == "" or choose.content == " ":
                    raise ConteudoInvalidoException("Invalid choose")
                while choose.content == "Y" or choose.content == "y":
                    m = await ctx.send("Enter the name of a secondary status:")
                    msgs.append(m)
                    status_nome = await self.bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(status_nome)
                    if status_nome.content == "" or status_nome.content == " ":
                        raise ConteudoInvalidoException("Invalid status name.")
                    m = await ctx.send("Enter the initials of a secondary status:")
                    msgs.append(m)
                    status_sigla = await self.bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(status_sigla)
                    if status_sigla.content == "" or status_sigla.content == " ":
                        raise ConteudoInvalidoException("Invalid System's main status initials.")
                    status_secundarios[status_sigla.content] = status_nome.content
                    m = await ctx.send("Are there other types of secondary status in your system? <Type 'y' for yes>")
                    msgs.append(m)
                    choose = await self.bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(choose)
                c.adicionar_dados("status_secundarios", status_secundarios)
                await self.status_registro(ctx, c, campos_txt, campos_raw, msg)
                await self.deletar_mensagens(msgs)
        except ConteudoInvalidoException as e:
            await ctx.send(e)
            await ctx.send("Do you want to continue the RPG System register?")
            escolha = await self.sim_nao(ctx,self.bot)
            if escolha:
                await self.cadastro_sistema_loop(ctx, self.bot)
            else:
                del caches[guild_id]
                await ctx.send("Registration canceled.")
        except ValueError:
            await ctx.send("Integer Value bigger then 0 expected.")
            await ctx.send("Do you want to continue the RPG System register?")
            escolha = await self.sim_nao(ctx, self.bot)
            if escolha:
                await self.cadastro_sistema_loop(ctx, self.bot)
            else:
                del caches[guild_id]
                await ctx.send("Registration canceled.")

    @classmethod
    async def cadastro_sistema_loop(self,ctx,bot):
        campos_txt = ["Name", "Level Coefficient", "Life", "Energy", "Other Energies", "Main Status", "Iniciative Status", "Moviment Status", "Character Status", "Secondary Status"]
        campos_raw = ["nome", "coeficiente_level", "vida", "energia", "outras_energias", "status_primarios",  "status_iniciativa", "status_movimento", "status_personagem", "status_secundarios"]
        guild_id = ctx.guild.id
        if guild_id not in caches:
            c = Cache()
            caches[ctx.guild.id] = c
        try:
            c = caches[guild_id]
            msg = await self.status_registro(ctx, c, campos_txt, campos_raw)
            if "nome" not in c.dados:
                m1 = await ctx.send("What's the RPG System name?")
                nome = await bot.wait_for('message', check=self.check(ctx.author))
                if nome.content == "" or nome.content == " ":
                    raise ConteudoInvalidoException("Invalid System's name.")
                c.adicionar_dados("nome",nome.content)
                msgs = [m1,nome]
                await self.deletar_mensagens(msgs)
                await self.status_registro(ctx, c, campos_txt, campos_raw, msg)
            if "coeficiente_level" not in c.dados:
                m1 = await ctx.send("What's the RPG System level coefficient?")
                coef = await bot.wait_for('message', check=self.check(ctx.author))
                if coef.content == "" or coef.content == " ":
                    raise ConteudoInvalidoException("Invalid Level Coefficient.")
                coef_level = int(coef.content)
                if coef_level <= 0:
                    raise ConteudoInvalidoException("Invalid Level Coefficient.")
                c.adicionar_dados("coeficiente_level", coef_level)
                msgs = [m1,coef]
                await self.deletar_mensagens(msgs)
                await self.status_registro(ctx, c, campos_txt, campos_raw, msg)
            if "vida" not in c.dados:
                m1 = await ctx.send("What's the name of the characters' health?")
                vida_nome = await bot.wait_for('message', check=self.check(ctx.author))
                if vida_nome.content == "" or vida_nome.content == " ":
                    raise ConteudoInvalidoException("Invalid System's characters' health name.")
                m2 = await ctx.send("What's the initials of the characters' health?")
                vida_sigla = await bot.wait_for('message', check=self.check(ctx.author))
                if vida_sigla.content == "" or vida_sigla.content == " ":
                    raise ConteudoInvalidoException("Invalid System's characters' health initials.")
                vida = (vida_nome.content, vida_sigla.content)
                c.adicionar_dados("vida", vida)
                msgs = [m1, m2, vida_nome, vida_sigla]
                await self.deletar_mensagens(msgs)
                await self.status_registro(ctx, c, campos_txt, campos_raw, msg)
            if "energia" not in c.dados:
                m1 = await ctx.send("What's the name of the main energy of the system?")
                energia_nome = await bot.wait_for('message', check=self.check(ctx.author))
                if energia_nome.content == "" or energia_nome.content == " ":
                    raise ConteudoInvalidoException("Invalid System's main energy name.")
                m2 = await ctx.send("What's the initials of the main energy of the system?")
                energia_sigla = await bot.wait_for('message', check=self.check(ctx.author))
                if energia_sigla.content == "" or energia_sigla.content == " ":
                    raise ConteudoInvalidoException("Invalid System's main energy initials.")
                energia = (energia_nome.content, energia_sigla.content)
                c.adicionar_dados("energia", energia)
                msgs = [m1, m2, energia_nome, energia_sigla]
                await self.deletar_mensagens(msgs)
                await self.status_registro(ctx, c, campos_txt, campos_raw, msg)
            if "outras_energias" not in c.dados:
                outras_energias = []
                msgs = []
                m1 = await ctx.send("Are there other types of energies in your system? <Type 'y' for yes>")
                msgs.append(m1)
                choose = await bot.wait_for('message', check=self.check(ctx.author))
                msgs.append(choose)
                if choose.content == "" or choose.content == " ":
                    raise ConteudoInvalidoException("Invalid choose")
                while choose.content == "Y" or choose.content == "y":
                    m = await ctx.send("What's the energy name?")
                    msgs.append(m)
                    energia_nome = await bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(energia_nome)
                    if energia_nome.content == "" or energia_nome.content == " ":
                        raise ConteudoInvalidoException("Invalid System's main energy name.")
                    m = await ctx.send("What's the initials of the main energy of the system?")
                    msgs.append(m)
                    energia_sigla = await bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(energia_sigla)
                    if energia_sigla.content == "" or energia_sigla.content == " ":
                        raise ConteudoInvalidoException("Invalid System's main energy initials.")
                    energia = (energia_nome.content, energia_sigla.content)
                    outras_energias.append(energia)
                    m = await ctx.send("Are there other types of energies in your system? <Type 'y' for yes>")
                    msgs.append(m)
                    choose = await bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(choose)
                    if choose.content == "" or choose.content == " ":
                        raise ConteudoInvalidoException("Invalid choose")
                c.adicionar_dados("outras_energias", outras_energias)
                await self.status_registro(ctx, c, campos_txt, campos_raw, msg)
                await self.deletar_mensagens(msgs)
            if "status_primarios" not in c.dados:
                status_primarios = {}
                msgs = []
                m = await ctx.send("Enter the name of a main status:")
                msgs.append(m)
                status_nome = await bot.wait_for('message', check=self.check(ctx.author))
                msgs.append(status_nome)
                if status_nome.content == "" or status_nome.content == " ":
                    raise ConteudoInvalidoException("Invalid status name.")
                m = await ctx.send("Enter the initials of a main status:")
                msgs.append(m)
                status_sigla = await bot.wait_for('message', check=self.check(ctx.author))
                msgs.append(status_sigla)
                if status_sigla.content == "" or status_sigla.content == " ":
                    raise ConteudoInvalidoException("Invalid System's main status initials.")
                status_primarios[status_sigla.content] = status_nome.content
                m = await ctx.send("Are there other types of main status in your system? <Type 'y' for yes>")
                msgs.append(m)
                choose = await bot.wait_for('message', check=self.check(ctx.author))
                msgs.append(choose)
                if choose.content == "" or choose.content == " ":
                    raise ConteudoInvalidoException("Invalid choose")
                while choose.content == "Y" or choose.content == "y":
                    m = await ctx.send("Enter the name of a main status:")
                    msgs.append(m)
                    status_nome = await bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(status_nome)
                    if status_nome.content == "" or status_nome.content == " ":
                        raise ConteudoInvalidoException("Invalid status name.")
                    m = await ctx.send("Enter the initials of a main status:")
                    msgs.append(m)
                    status_sigla = await bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(status_sigla)
                    if status_sigla.content == "" or status_sigla.content == " ":
                        raise ConteudoInvalidoException("Invalid System's main status initials.")
                    status_primarios[status_sigla.content] = status_nome.content
                    m = await ctx.send("Are there other types of main status in your system? <Type 'y' for yes>")
                    msgs.append(m)
                    choose = await bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(choose)
                c.adicionar_dados("status_primarios", status_primarios)
                await self.status_registro(ctx, c, campos_txt, campos_raw, msg)
                await self.deletar_mensagens(msgs)
            if "status_personagem" not in c.dados:
                status_personagem = {}
                if "status_iniciativa" not in c.dados:
                    msgs = []
                    m = await ctx.send("Enter the name of a character iniciative status:")
                    msgs.append(m)
                    status_nome = await bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(status_nome)
                    if status_nome.content == "" or status_nome.content == " ":
                        raise ConteudoInvalidoException("Invalid status name.")
                    m = await ctx.send("Enter the initials of a character iniciative status:")
                    msgs.append(m)
                    status_sigla = await bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(status_sigla)
                    if status_sigla.content == "" or status_sigla.content == " ":
                        raise ConteudoInvalidoException("Invalid System's character status initials.")
                    status_iniciativa = (status_nome.content,status_sigla.content)
                    c.adicionar_dados("status_iniciativa", status_iniciativa)
                    await self.status_registro(ctx, c, campos_txt, campos_raw, msg)
                    await self.deletar_mensagens(msgs)
                if "status_movimento" not in c.dados:
                    msgs = []
                    m = await ctx.send("Enter the name of a character moviment status:")
                    msgs.append(m)
                    status_nome = await bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(status_nome)
                    if status_nome.content == "" or status_nome.content == " ":
                        raise ConteudoInvalidoException("Invalid status name.")
                    m = await ctx.send("Enter the initials of a character moviment status:")
                    msgs.append(m)
                    status_sigla = await bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(status_sigla)
                    if status_sigla.content == "" or status_sigla.content == " ":
                        raise ConteudoInvalidoException("Invalid System's character status initials.")
                    status_iniciativa = (status_nome.content,status_sigla.content)
                    c.adicionar_dados("status_movimento", status_iniciativa)
                    await self.status_registro(ctx, c, campos_txt, campos_raw, msg)
                    await self.deletar_mensagens(msgs)
                msgs = []
                m = await ctx.send("Enter the name of a character status:")
                msgs.append(m)
                status_nome = await bot.wait_for('message', check=self.check(ctx.author))
                msgs.append(status_nome)
                if status_nome.content == "" or status_nome.content == " ":
                    raise ConteudoInvalidoException("Invalid status name.")
                m = await ctx.send("Enter the initials of a character status:")
                msgs.append(m)
                status_sigla = await bot.wait_for('message', check=self.check(ctx.author))
                msgs.append(status_sigla)
                if status_sigla.content == "" or status_sigla.content == " ":
                    raise ConteudoInvalidoException("Invalid System's character status initials.")
                status_personagem[status_sigla.content] = status_nome.content
                m = await ctx.send("Are there other types of character status in your system? <Type 'y' for yes>")
                msgs.append(m)
                choose = await bot.wait_for('message', check=self.check(ctx.author))
                msgs.append(choose)
                if choose.content == "" or choose.content == " ":
                    raise ConteudoInvalidoException("Invalid choose")
                while choose.content == "Y" or choose.content == "y":
                    m = await ctx.send("Enter the name of a character status:")
                    msgs.append(m)
                    status_nome = await bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(status_nome)
                    if status_nome.content == "" or status_nome.content == " ":
                        raise ConteudoInvalidoException("Invalid character name.")
                    m = await ctx.send("Enter the initials of a character status:")
                    msgs.append(m)
                    status_sigla = await bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(status_sigla)
                    if status_sigla.content == "" or status_sigla.content == " ":
                        raise ConteudoInvalidoException("Invalid System's character status initials.")
                    status_personagem[status_sigla.content] = status_nome.content
                    m = await ctx.send("Are there other types of character status in your system? <Type 'y' for yes>")
                    msgs.append(m)
                    choose = await bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(choose)
                c.adicionar_dados("status_personagem", status_personagem)
                await self.status_registro(ctx, c, campos_txt, campos_raw, msg)
                await self.deletar_mensagens(msgs)
                del caches[guild_id]
            if "status_secundarios" not in c.dados:
                status_secundarios = {}
                msgs = []
                m = await ctx.send("Enter the name of a secondary status:")
                msgs.append(m)
                status_nome = await bot.wait_for('message', check=self.check(ctx.author))
                msgs.append(status_nome)
                if status_nome.content == "" or status_nome.content == " ":
                    raise ConteudoInvalidoException("Invalid status name.")
                m = await ctx.send("Enter the initials of a secondary status:")
                msgs.append(m)
                status_sigla = await bot.wait_for('message', check=self.check(ctx.author))
                msgs.append(status_sigla)
                if status_sigla.content == "" or status_sigla.content == " ":
                    raise ConteudoInvalidoException("Invalid System's status initials.")
                status_secundarios[status_sigla.content] = status_nome.content
                m = await ctx.send("Are there other types of secondary status in your system? <Type 'y' for yes>")
                msgs.append(m)
                choose = await bot.wait_for('message', check=self.check(ctx.author))
                msgs.append(choose)
                if choose.content == "" or choose.content == " ":
                    raise ConteudoInvalidoException("Invalid choose")
                while choose.content == "Y" or choose.content == "y":
                    m = await ctx.send("Enter the name of a secondary status:")
                    msgs.append(m)
                    status_nome = await bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(status_nome)
                    if status_nome.content == "" or status_nome.content == " ":
                        raise ConteudoInvalidoException("Invalid status name.")
                    m = await ctx.send("Enter the initials of a secondary status:")
                    msgs.append(m)
                    status_sigla = await bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(status_sigla)
                    if status_sigla.content == "" or status_sigla.content == " ":
                        raise ConteudoInvalidoException("Invalid System's main status initials.")
                    status_secundarios[status_sigla.content] = status_nome.content
                    m = await ctx.send("Are there other types of secondary status in your system? <Type 'y' for yes>")
                    msgs.append(m)
                    choose = await bot.wait_for('message', check=self.check(ctx.author))
                    msgs.append(choose)
                c.adicionar_dados("status_secundarios", status_secundarios)
                await self.status_registro(ctx, c, campos_txt, campos_raw, msg)
                await self.deletar_mensagens(msgs)
        except ConteudoInvalidoException as e:
            await ctx.send(e)
            await ctx.send("Do you want to continue the RPG System register?")
            escolha = await self.sim_nao(ctx, bot)
            if escolha:
                await self.cadastro_sistema_loop(ctx,bot)
            else:
                del caches[guild_id]
                await ctx.send("Registration canceled.")
        except ValueError:
            await ctx.send("Integer Value bigger then 0 expected.")
            await ctx.send("Do you want to continue the RPG System register?")
            escolha = await self.sim_nao(ctx, bot)
            if escolha:
                await self.cadastro_sistema_loop(ctx,bot)
            else:
                del caches[guild_id]
                await ctx.send("Registration canceled.")

    @classmethod
    def check(self, author):
        def inner_check(message):
            return message.author == author
        return inner_check

    @classmethod
    async def status_registro(self, ctx, cache, campos_txt, campos_raw, msg=None):
        mensagem = "```RPG System Register\n\n"
        for i in range(len(campos_raw)):
            if campos_raw[i] in cache.dados:
                campo = self.formatacao(cache.dados[campos_raw[i]])
                mensagem += campos_txt[i] + ": " + str(campo) + "\n"
            else:
                mensagem += campos_txt[i] + ": Waiting..."
                break
        mensagem += "```"
        if msg == None:
            nova_msg = await ctx.send(content=mensagem)
            return nova_msg
        else:
            await msg.edit(content=mensagem)

    @classmethod
    def formatacao(self,campo):
        texto = ""
        if isinstance(campo, dict):
            for chave in campo:
                texto += chave + " : " + campo[chave] + ", "
        elif isinstance(campo, tuple):
            texto += campo[0] + " : " + campo[1] + ", "
        elif isinstance(campo, list):
            if campo == []:
                texto = "None"
                return texto
            else:
                for elem in campo:
                    if isinstance(elem, tuple):
                        texto += elem[0] + " : " + elem[1] + ", "
                    else:
                        texto += elem + ", "
        if texto != "":
            texto = texto[:len(texto)-2]
            return texto
        else:
            return campo

    @classmethod
    async def deletar_mensagens(self, msgs):
        for msg in msgs:
            await msg.delete()

    @classmethod
    async def selecionar_status(self, c, status, ctx , bot):
        stat = c.dados[status]
        ordem = []
        select = discord.Embed(
            title=f"""Choose the character status""",
            description="Enter the status number.",
            colour=discord.Colour.blue()
        )
        for chave in stat:
            select.add_field(name="1. " + chave, value=stat[chave], inline=True)
            ordem.append(chave)
        emb = await ctx.send(embed=select)
        n = await bot.wait_for('message', check=self.check(ctx.author))
        try:
            num = int(n.content)
            await emb.delete()
            await n.delete()
            return ordem[num-1]
        except:
            await emb.delete()
            await n.delete()
            await self.selecionar_status(c, status, ctx, bot)

    @classmethod
    async def sim_nao(cls, ctx, bot):
        embed = discord.Embed(
            title=f"""**What's your choose?**""",
            description="React with one of the belows reactions.",
            colour=discord.Colour.dark_orange()
        )
        embed_msg = await ctx.send(embed=embed)
        await embed_msg.add_reaction(emoji='✅')
        await embed_msg.add_reaction(emoji='🇽')
        while True:
            reaction, user = await bot.wait_for('reaction_add')
            if str(reaction.emoji) == '✅' and str(user) == str(ctx.author):
                return True
            if str(reaction.emoji) == '🇽' and str(user) == str(ctx.author):
                return False

        
def setup(bot):
    bot.add_cog(Cadastro(bot))