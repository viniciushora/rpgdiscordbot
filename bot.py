import discord
import random
import pickle
import io
import youtube_dl
import os
from discord.utils import get
import logging
import asyncio

from cogs.rpg.char import *
from cogs.rpg.sessao import *
from cogs.rpg.server import *
#from cogs.database import *

from discord.ext import commands

bot = commands.Bot(command_prefix='!')
bot.remove_command("help")

code_race = code_class = code_status = code_proefs = code_items = code_religions = code_proefs2 = code_skills = code_spells = code_users = code_chars = code_systems = 0

global systems, servers, users, chars, character, classes, races, status, proefs, proefs2, items, religions, skills, spells, players

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

servers = []

@bot.event
async def on_member_join(member):
    print("Member Join")

@bot.event
async def on_guild_join(guild):
    print("Guild Join")


@bot.event
async def on_ready():
    global masters, races, classes, status, proefs, proefs2, items, religions, skills, spells, users, chars, systems, code_class, code_race, code_status, code_items, code_religions, code_proefs2, code_skills, code_spells, code_users, code_chars, code_systems
    print('Estou funcionando como {0.user}'.format(bot))
    print("Tudo Ok")


@bot.command()
async def criarpersonagem(ctx,*,arg):
    if not str(ctx.author) in users.values():
        code_users += 1
        users[code_users] = ctx.author
        print("Usuário criado com sucesso!")

@bot.command()
async def criarraca(ctx,*,arg):
    global code_race
    if str(ctx.author) in masters:
        raca = arg
        await ctx.send(f"""Desejar colocar uma foto da classe? <deixe o link da imagem para **sim** ou digite qualquer coisa para **não**> """)
        msg = await bot.wait_for('message')
        foto = None
        if msg.content.startswith('http'):
            foto = msg.content
        await ctx.send(f"""Escreva a descrição da raça:""")
        msg = await bot.wait_for('message')
        desc = msg.content
        await ctx.send(f"""Escreva sobre a idade da raça:""")
        msg = await bot.wait_for('message')
        idade = msg.content
        await ctx.send(f"""Escreva sobre as tendências da raça:""")
        msg = await bot.wait_for('message')
        tend = msg.content
        await ctx.send(f"""Escreva sobre o tamanho da raça:""")
        msg = await bot.wait_for('message')
        tam = msg.content
        await ctx.send(f"""Escreva sobre as motivações da raça:""")
        msg =  await bot.wait_for('message')
        motiv = msg.content
        await ctx.send(f"""Escreva sobre as vantagens da raça:""")
        msg =  await bot.wait_for('message')
        vant = msg.content
        habil = None
        code_race += 1
        races[code_race] = [raca,foto,desc,idade,tend,tam,motiv,vant,habil]
        print(f"""Raça: {raca} criada com sucesso! """)
        await ctx.send(f"""Raça: {raca} criada com sucesso! """)
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def deletarraca(ctx,*,arg):
    global code_race
    if str(ctx.author) in masters:
        raca = arg
        race_key = -1
        for key in races:
            if races[key] == raca:
                race_key = key
        if race_key != -1:
            del races[race_key]
            print(f"""Raça: {raca} criada com sucesso! """)
            await ctx.send(f"""Raça: {raca} deletada com sucesso! """)
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def listarracas(ctx):
    if str(ctx.author) in masters:
        embed = discord.Embed(
            title="Raças cadastradas :boy:  ",
            description=f"""Estas são as raças cadastradas em **My Rpg Bot**:""",
            colour=discord.Colour.blue()
        )
        racas = ""
        cont = 1
        for key in races:
            racas += f"""**{cont}.** {races[key][0]}\n"""
            cont += 1
        embed.add_field(name="**Raças:**", value=racas, inline=True)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def criarclasse(ctx,*,arg):
    global code_class
    if str(ctx.author) in masters:
        classe = arg
        await ctx.send(f"""Desejar colocar uma foto da classe? <deixe o link da imagem para **sim** ou digite qualquer coisa para **não**> """)
        msg = await bot.wait_for('message')
        foto = None
        if msg.content.startswith("http"):
            foto = msg.content
        await ctx.send(f"""Informe o dado de vida da classe (somente números):""")
        msg = await bot.wait_for('message')
        try:
            dado_vida = int(msg.content)
        except:
            dado_vida = None
            await ctx.send(f"""Dado de vida não foi especificado :(""")
        await ctx.send(f"""Escreva o tipo da classe:""")
        msg =  await bot.wait_for('message')
        tipo = msg.content
        await ctx.send(f"""Escreva a descrição da classe:""")
        msg =  await bot.wait_for('message')
        desc = msg.content
        await ctx.send(f"""Escreva sobre a fonte de poter da classe (atributos e tals):""")
        msg = await bot.wait_for('message')
        ft_poder = msg.content
        await ctx.send(f"""Escreva sobre as vantagens da classe:""")
        msg = await bot.wait_for('message')
        vant = msg.content
        habil = None
        code_class += 1
        classes[code_class] = [classe, foto, dado_vida, tipo, desc, ft_poder, vant, habil]
        print(f"""Classe: {classe} criada com sucesso! """)
        await ctx.send(f"""Classe: {classe} criada com sucesso! """)
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def deletarclasse(ctx,*,arg):
    global code_class
    if str(ctx.author) in masters:
        classe = arg
        class_key = -1
        for key in classes:
            if classes[key] == classe:
                class_key = key
        if class_key != -1:
            del classes[class_key]
            print(f"""Classe: {classe} deletada com sucesso! """)
            await ctx.channel.send(f"""Classe: {classe} deletada com sucesso! """)
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def listarclasses(ctx):
    if str(ctx.author) in masters:
        embed = discord.Embed(
            title="Classes cadastradas :crossed_swords: ",
            description=f"""Estas são as classes cadastradas em **My Rpg Bot**:""",
            colour=discord.Colour.red()
        )
        cont = 1
        classes1 = ""
        for key in classes:
            classes1 += f"""**{cont}.** {classes[key][0]}\n"""
            cont += 1
        embed.add_field(name="**Classes:**", value=classes1, inline=True)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def criarstatus(ctx,*,arg):
    if str(ctx.author) in masters:
        status1 = {}
        await ctx.send("Para adicionar um status digite '!status nomestatus'. Para sair digite '!sair'.")
        msg1 = await bot.wait_for('message')
        mensagem = msg1.content
        while mensagem != '!sair':
            if msg1.content.startswith('!status '):
                stat = ""
                for i in range(8, (len(msg1.content))):
                    stat += msg1.content[i]
                await ctx.send(f"""Status: {stat}. Para definir a sigla do status digite '!sigla nomesigla'.""")
                msg2 = await bot.wait_for('message')
                if msg2.content.startswith('!sigla '):
                    stat_sigla = ""
                    for i in range(7, (len(msg2.content))):
                        stat_sigla += msg2.content[i]
                    status1[stat_sigla] = stat
                    await ctx.send(f"""Status: {stat} criado com sucesso.""")
            await ctx.send("Para adicionar um status digite '!status nomestatus'. Para sair digite '!sair'.")
            msg1 = await bot.wait_for('message')
            mensagem = msg1.content
        if status1 != {}:
            code_status += 1
            status[code_status] = status1
            await ctx.send("Seus status foram armazenados")
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def deletarstatus(ctx,*,arg):
    if str(ctx.author) in masters:
        aux = arg
        status_key = -1
        for key in status:
            if key == aux:
                status_key = key
        if status_key > -1:
            del status[status_key]
            await ctx.send(f"""Grupo de Status: {status_key} deletado com sucesso! """)
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def listarstatus(ctx):
    if str(ctx.author) in masters:
        embed = discord.Embed(
            title="Grupos de Status cadastrados",
            description=f"""Estes são os grupos de Status em **My Rpg Bot**:""",
            colour=discord.Colour.green()
        )
        cont = 1
        for status_key in status:
            stat1 = ""
            for stat_key,stat in status[status_key].items():
                stat1 += f"""{stat}({stat_key})\n"""
            embed.add_field(name=f"""**{cont}.**""", value=stat1, inline=True)
            cont+=1
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def criarpericia(ctx,*,arg):
    code_proefs = 0
    if str(ctx.author) in masters:
        proef = arg
        code_proefs += 1
        proefs[code_proefs] = proef
        print(f"""Perícia: {proef} criada com sucesso!""")
        await ctx.send(f"""Perícia: {proef} criada com sucesso! """)
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def deletarpericia(ctx,*,arg):
    if str(ctx.author) in masters:
        proef = arg
        proef_key = -1
        for key in proefs:
            if proefs[key] == proef:
                proef_key = key
        if proef_key != -1:
            del proefs[proef_key]
            print(f"""Perícia: {proef} deletada com sucesso! """)
            await ctx.send(f"""Perícia: {proef} deletada com sucesso! """)
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def listarpericias(ctx):
    if str(ctx.author) in masters:
        embed = discord.Embed(
            title="Perícias cadastradas",
            description=f"""Estas são as perícias cadastradas em **My Rpg Bot**:""",
            colour=discord.Colour.purple()
        )
        cont = 1
        pericias = ""
        for key in proefs:
            pericias += f"""**{cont}.** {proefs[key]}\n"""
            cont += 1
        embed.add_field(name="**Perícias:**", value=pericias, inline=True)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def criaritem(ctx,*,arg):
    if str(ctx.author) in masters:
        item = arg
        code_items += 1
        items[code_items] = item
        print(f"""Item: {item} criado com sucesso!""")
        await ctx.send(f"""Item: {item} criado com sucesso! """)
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def deletaritem(ctx,*,arg):
    if str(ctx.author) in masters:
        item = arg
        item_key = -1
        for key in items:
            if items[key] == item:
                item_key = key
        if item_key != -1:
            del items[item_key]
            print(f"""Item: {item} deletado com sucesso! """)
            await ctx.send(f"""Item: {item} deletado com sucesso! """)
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def listaritems(ctx):
    if str(ctx.author) in masters:
        embed = discord.Embed(
            title="Items cadastrados",
            description=f"""Estes são os Items cadastrados em **My Rpg Bot**:""",
            colour=discord.Colour.dark_grey()
        )
        cont = 1
        items1 = ""
        for key in items:
            items1 += f"""**{cont}.** {items[key]}\n"""
            cont += 1
        embed.add_field(name="**Items:**", value=items1, inline=True)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def criarreligiao(ctx,*,arg):
    if str(ctx.author) in masters:
        religion = arg
        code_religions += 1
        religions[code_religions] = religion
        print(f"""Religião: {religion} criada com sucesso!""")
        await ctx.send(f"""Religião: {religion} criada com sucesso! """)
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def deletarreligiao(ctx,*,arg):
    if ctx.author in masters:
        religion = arg
        religion_key = -1
        for key in religions:
            if religions[key] == religion:
                religion_key = key
        if religion_key != -1:
            del religions[religion_key]
            print(f"""Religião: {religion} deletada com sucesso! """)
            await ctx.send(f"""Religião: {religion} deletada com sucesso! """)
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def listarreligioes(ctx):
    if str(ctx.author) in masters:
        embed = discord.Embed(
            title="Religiões cadastrados",
            description=f"""Estas são as religiões cadastradas em **My Rpg Bot**:""",
            colour=discord.Colour.dark_gold()
        )
        cont = 1
        religioes = ""
        for key in religions:
            religioes += f"""**{cont}.** {religions[key]}\n"""
            cont += 1
        embed.add_field(name="**Religiões:**", value=religioes, inline=True)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def criarproef(ctx,*,arg):
    if str(ctx.author) in masters:
        proef = arg
        code_proefs2 += 1
        proefs2[code_proefs2] = proef
        print(f"""Proeficiência: {proef} criada com sucesso!""")
        await ctx.send(f"""Proeficiência: {proef} criada com sucesso! """)
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def deletarproef(ctx,*,arg):
    if str(ctx.author) in masters:
        proef = arg
        proef_key = -1
        for key in proefs2:
            if proefs[key] == proef:
                proef_key = key
        if proef_key != -1:
            del proefs2[proef_key]
            print(f"""Proeficiência: {proef} deletada com sucesso! """)
            await ctx.send(f"""Proeficiência: {proef} deletada com sucesso! """)
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def listarproefs(ctx):
    if str(ctx.author) in masters:
        embed = discord.Embed(
            title="Proeficiências cadastradas",
            description=f"""Estas são as proeficiências cadastradas em **My Rpg Bot**:""",
            colour=discord.Colour.blurple()
        )
        cont = 1
        proefi = ""
        for key in proefs2:
            proefi += f"""**{cont}.** {proefs2[key]}\n"""
            cont += 1
        embed.add_field(name="**Proeficiências:**", value=proefi, inline=True)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def criartalento(ctx,*,arg):
    if str(ctx.author) in masters:
        skill = arg
        code_skills += 1
        skills[code_skills] = skill
        print(f"""Talento: {skill} criado com sucesso!""")
        await ctx.send(f"""Talento: {skill} criado com sucesso! """)
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def deletartalento(ctx,*,arg):
    if ctx.author in masters:
        skill = arg
        skill_key = -1
        for key in skills:
            if skills[key] == skill:
                skill_key = key
        if skill_key != -1:
            del skills[skill_key]
            print(f"""Talento: {skill} deletado com sucesso! """)
            await ctx.send(f"""Talento: {skill} deletado com sucesso! """)
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def listartalentos(ctx):
    if str(ctx.author) in masters:
        embed = discord.Embed(
            title="Talentos cadastrados",
            description=f"""Estas são os talentos cadastrados em **My Rpg Bot**:""",
            colour=discord.Colour.dark_magenta()
        )
        cont = 1
        talentos = ""
        for key in skills:
            talentos += f"""**{cont}.** {skills[key]}\n"""
            cont += 1
        embed.add_field(name="**Talentos:**", value=talentos, inline=True)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def criarfeitico(ctx,*,arg):
    if str(ctx.author) in masters:
        spell = arg
        code_spells += 1
        spells[code_spells] = spell
        print(f"""Feitiço: {spell} criado com sucesso!""")
        await ctx.send(f"""Feitiço: {spell} criado com sucesso! """)
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def deletarfeitico(ctx,*,arg):
    if str(ctx.author) in masters:
        spell = arg
        spell_key = -1
        for key in spells:
            if spells[key] == spell:
                spell_key = key
        if spell_key != -1:
            del spells[spell_key]
            print(f"""Feitiço: {spell} deletado com sucesso! """)
            await ctx.send(f"""Feitiço: {spell} deletado com sucesso! """)
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def listarfeiticos(ctx):
    if str(ctx.author) in masters:
        embed = discord.Embed(
            title="Feitiços cadastrados",
            description=f"""Estas são os feitiços cadastrados em **My Rpg Bot**:""",
            colour=discord.Colour.magenta()
        )
        cont = 1
        feiticos = ""
        for key in spells:
            feiticos += f"""**{cont}.** {spells[key]}\n"""
            cont += 1
        embed.add_field(name="**Feitiços:**", value=feiticos, inline=True)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def ajuda(ctx):
    with open('comandos.txt', 'r') as cmd:
        linha = cmd.readline()
        while linha != "":
            exibicao = linha.strip()
            await ctx.send(exibicao)
            linha = cmd.readline()
        cmd.close()

@bot.command()
async def criarsistema(ctx,*,arg):
    if str(ctx.author) in masters:
        system_name = arg
        coef_level = ""
        rules = {}
        t_races = ""
        t_classes = ""
        t_items = ""
        system_races = []
        system_classes = []
        system_status = {}
        system_items = {}
        rcs_stats = {}
        rcs_features = {}
        e_status = discord.Embed(
            title="Grupos de Status cadastrados",
            description=f"""Estes são os grupos de Status em **My Rpg Bot**:""",
            colour=discord.Colour.green()
        )
        for status_key in status:
            stat1 = ""
            for stat_key, stat in status[status_key].items():
                stat1 += f"""{stat}({stat_key})\n"""
            e_status.add_field(name=f"""**{status_key}.**""", value=stat1, inline=True)
        await ctx.send(embed=e_status)
        await ctx.send("Quais são os status principais do sistema? (Digite !pstatus 'codigogrupostatus')")
        msg = await bot.wait_for('message')
        while not msg.content.startswith('!pstatus '):
            await ctx.send("PARÂMETROS ERRADOS!\nQuais são os status principais do sistema? (Digite !pstatus 'codigogrupostatus')")
            msg = await bot.wait_for('message')
        g_status = ""
        for i in range(9, (len(msg.content))):
            g_status += msg.content[i]
        system_status[len(system_status)+1] = ("Status principais", int(g_status))
        await ctx.send("Quais são os status dos itens do sistema? (Digite !istatus 'codigogrupostatus')")
        msg = await bot.wait_for('message')
        while not msg.content.startswith('!istatus '):
            await ctx.send("PARÂMETROS ERRADOS!\nQuais são os status dos itens do sistema? (Digite !istatus 'codigogrupostatus')")
            msg = await bot.wait_for('message')
        i_status = ""
        for i in range(9, (len(msg.content))):
            i_status += msg.content[i]
        system_status[len(system_status) + 1] = ("Status dos Itens", int(i_status))
        await ctx.send("Deseja criar mais um tipo de status? (Digite !tipostatus 'nometipostatus' ou !sair)")
        msg = await bot.wait_for('message')
        while not msg.content.startswith("!sair"):
            if msg.content.startswith('!tipostatus '):
                g_status = ""
                if msg.content.startswith('!tipostatus '):
                    for i in range(12, (len(msg.content))):
                        g_status += msg.content[i]
                await ctx.send(f"""Deseja definir qual grupo de Status como: {g_status}? (Digite !tstatus 'codigogrupostatus')""")
                msg = await bot.wait_for('message')
                while not msg.content.startswith("!tstatus "):
                    await ctx.send(f"""PARÂMETROS ERRADOS!\nDeseja definir qual grupo de Status como: {g_status}? (Digite !tstatus 'codigogrupostatus')""")
                    msg = await bot.wait_for('message')
                c_status = ""
                for i in range(9, (len(msg.content))):
                    c_status += msg.content[i]
                system_status[len(system_status)+1] = (g_status,int(c_status))
                await ctx.send("Deseja criar mais um tipo de status? (Digite !tipostatus 'nometipostatus' ou !sair)")
                msg = await bot.wait_for('message')
            else:
                await ctx.send("PARÂMETROS ERRADOS!\nDeseja criar mais um tipo de status? (Digite !tipostatus 'nometipostatus' ou !sair)")
                msg = await bot.wait_for('message')

#Raças
        await ctx.send("Deseja cadastrar quais raças em seu sistema?")
        e_races = discord.Embed(
            title="Raças cadastradas",
            description=f"""Estas são as raças cadastradas em **My Rpg Bot**:""",
            colour=discord.Colour.blue()
        )
        e_racas = ""
        for key in races:
            e_racas += f"""**{key}.** {races[key][0]}\n"""
        e_races.add_field(name="**Raças:**", value=e_racas, inline=True)
        await ctx.send(embed=e_races)
        await ctx.send("Quais raças deseja inserir? (Exemplo: !raças 1 4 5 6 7 9)")
        msg = await bot.wait_for('message')
        while not msg.content.startswith('!raças '):
            await ctx.send("PARÂMETROS ERRADOS!\nQuais raças deseja inserir? (Exemplo: !raças 1 4 5 6 7 9)")
            msg = await bot.wait_for('message')
        for num in range(7,len(msg.content)):
            t_races += msg.content[num]
        i = 0
        condition = False
        while not condition:
            t_race = ""
            while i < len(t_races) and (t_races[i] != " "):
                t_race += t_races[i]
                i += 1
            if i == len(t_races):
                condition = True
            if int(t_race) in races:
                system_races.append(int(t_race))
                e2_status = discord.Embed(
                    title="Grupos de Status cadastrados",
                    description=f"""Estes são os grupos de Status em **My Rpg Bot**:""",
                    colour=discord.Colour.green()
                )
                for status_key in status:
                    stat1 = ""
                    for stat_key, stat in status[status_key].items():
                        stat1 += f"""{stat}({stat_key})\n"""
                    e2_status.add_field(name=f"""**{status_key}.**""", value=stat1, inline=True)
                await ctx.send(embed=e2_status)
                await ctx.send(f"""Bônus e atributos base da raça {races[int(t_race)][0]}:\nDeseja adicionar algum bônus ou atributo base? (Digite 'n' para sair)""")
                msg = await bot.wait_for('message')
                while msg.content != "n":
                    await ctx.send("Informe um bônus ou atributo base: Digite <!atr 'grupostatus' 'sigla' n>")
                    msg = await bot.wait_for('message')
                    while not msg.content.startswith("!atr "):
                        await ctx.send("PARÂMETROS ERRADOS!\nInforme os bônus e atributos base da classe: <!atr 'grupostatus' 'sigla' n>")
                        msg = await bot.wait_for('message')
                    atr = ""
                    for num in range(5, len(msg.content)):
                        atr += msg.content[num]
                    atr = atr.split(" ")
                    rcs_stats[int(t_race)] = (atr[1],int(atr[2]))
                    await ctx.send("Bônus e atributos base da classe:\nDeseja adicionar algum bônus ou atributo base? (Digite 'n' para sair)")
                    msg = await bot.wait_for('message')
                await ctx.send("Habilidades da Raça:\nDeseja adicionar alguma habilidade? (Digite 'n' para sair)")
                msg = await bot.wait_for('message')
                while msg.content != "n":
                    await ctx.send("Informe o nome da habilidade: Digite <!abl 'nomehabilidade'>")
                    msg = await bot.wait_for('message')
                    while not msg.content.startswith("!abl "):
                        await ctx.send("PARÂMETROS ERRADOS!\nInforme o nome da habilidade: Digite <!abl 'nomehabilidade'>")
                        msg = await bot.wait_for('message')
                    abl = ""
                    for num in range(5, len(msg.content)):
                        abl += msg.content[num]
                    await ctx.send("Escreva a descrição da habilidade: Digite <!desc 'descrição'>")
                    msg = await bot.wait_for('message')
                    while not msg.content.startswith("!desc "):
                        await ctx.send("PARÂMETROS ERRADOS!\nEscreva a descrição da habilidade: Digite <!desc 'descrição'>")
                        msg = await bot.wait_for('message')
                    descricao = msg.content.split(" ")[1]
                    rcs_features[int(t_race)] = (abl,descricao)
                    await ctx.send("Habilidades da Raça:\nDeseja adicionar alguma habilidade? (Digite 'n' para sair)")
                    msg = await bot.wait_for('message')
                await ctx.send(f"""Raça: {races[int(t_race)][0]} adicionado(a) ao sistema.""")
            i += 1

#classes

        e_classes = discord.Embed(
            title="Classes cadastrados",
            description=f"""Estas são as classes cadastradas em **My Rpg Bot**:""",
            colour=discord.Colour.red()
        )
        e_classes1 = ""
        for key in classes:
            e_classes1 += f"""**{key}.** {classes[key][0]}\n"""
        e_classes.add_field(name="**Classes:**", value=e_classes1, inline=True)
        await ctx.send(embed=e_classes)
        await ctx.send("Quais classes deseja inserir? (Exemplo: !classes 1 4 5 6 7 9)")
        msg = await bot.wait_for('message')
        while not msg.content.startswith('!classes '):
            await ctx.send("PARÂMETROS ERRADOS!\nQual o nome do seu Sistema? (Digite !sistema nomesistema)")
            msg = await bot.wait_for('message')
        for num in range(9, len(msg.content)):
            t_classes += msg.content[num]
        i = 0
        condition = False
        while not condition:
            t_class = ""
            while i < len(t_classes) and (t_classes[i] != " "):
                t_class += t_classes[i]
                i += 1
            if i == len(t_classes):
                condition = True
            if int(t_class) in classes:
                system_classes.append(int(t_class))
                await ctx.send(f"""Classe: {classes[int(t_class)][0]} adicionado(a) ao sistema.""")
            i += 1
        code_systems += 1
        system = [system_name, system_status, system_races, rcs_stats, rcs_features, system_classes]
        systems[code_systems] = system
        await ctx.send(f"""Sistema: {system_name} criado com sucesso! """)

#items

        await ctx.send("Deseja cadastrar quais items em seu sistema?")
        e_items = discord.Embed(
            title="Items cadastrados",
            description=f"""Estes são os items cadastrados em **My Rpg Bot**:""",
            colour=discord.Colour.dark_blue()
        )
        equips = ""
        consu = ""
        colec = ""
        for key in items:
            tipo = items[key][2]
            if tipo == "Equipamento":
                equips += f"""**{key}.** {items[key][0]}\n"""
            elif tipo == "Consumível":
                consu += f"""**{key}.** {items[key][0]}\n"""
            elif tipo == "Colecionável":
                colec += f"""**{key}.** {items[key][0]}\n"""
        e_items.add_field(name="**Equipamentos:**", value=equips, inline=False)
        e_items.add_field(name="**Consumíveis:**", value=consu, inline=False)
        e_items.add_field(name="**Colecionáveis:**", value=colec, inline=False)
        await ctx.send(embed=e_items)
        await ctx.send("Quais items deseja inserir? (Exemplo: !items 1 4 5 6 7 9)")
        msg = await bot.wait_for('message')
        while not msg.content.startswith('!items '):
            await ctx.send("PARÂMETROS ERRADOS!\nQuais items deseja inserir? (Exemplo: !items 1 4 5 6 7 9)")
            msg = await bot.wait_for('message')
        for num in range(8, len(msg.content)):
            t_items += msg.content[num]
        i = 0
        condition = False
        while not condition:
            t_item = ""
            while i < len(t_items) and (t_items[i] != " "):
                t_item += t_items[i]
                i += 1
            if i == len(t_items):
                condition = True
            if int(t_item) in items:
                system_races.append(int(t_race))
                e3_status = discord.Embed(
                    title="Status de Itens",
                    description=f"""Possíveis Status para os items em **{system_name}**:""",
                    colour=discord.Colour.green()
                )
                for status_key in status:
                    stat1 = ""
                    for stat_key, stat in status[status_key].items():
                        stat1 += f"""{stat}({stat_key})\n"""
                    e3_status.add_field(name=f"""**{status_key}.**""", value=stat1, inline=True)
                await ctx.send(embed=e3_status)
                await ctx.send(f"""Bônus e atributos base da raça {races[int(t_race)][0]}:\nDeseja adicionar algum bônus ou atributo base? (Digite 'n' para sair)""")
                msg = await bot.wait_for('message')
                while msg.content != "n":
                    await ctx.send("Informe um bônus ou atributo base: Digite <!atr 'grupostatus' 'sigla' n>")
                    msg = await bot.wait_for('message')
                    while not msg.content.startswith("!atr "):
                        await ctx.send(
                            "PARÂMETROS ERRADOS!\nInforme os bônus e atributos base da classe: <!atr 'grupostatus' 'sigla' n>")
                        msg = await bot.wait_for('message')
                    atr = ""
                    for num in range(5, len(msg.content)):
                        atr += msg.content[num]
                    atr = atr.split(" ")
                    rcs_stats[int(t_race)] = (atr[1], int(atr[2]))
                    await ctx.send(
                        "Bônus e atributos base da classe:\nDeseja adicionar algum bônus ou atributo base? (Digite 'n' para sair)")
                    msg = await bot.wait_for('message')
                await ctx.send("Habilidades da Raça:\nDeseja adicionar alguma habilidade? (Digite 'n' para sair)")
                msg = await bot.wait_for('message')
                while msg.content != "n":
                    await ctx.send("Informe o nome da habilidade: Digite <!abl 'nomehabilidade'>")
                    msg = await bot.wait_for('message')
                    while not msg.content.startswith("!abl "):
                        await ctx.send(
                            "PARÂMETROS ERRADOS!\nInforme o nome da habilidade: Digite <!abl 'nomehabilidade'>")
                        msg = await bot.wait_for('message')
                    abl = ""
                    for num in range(5, len(msg.content)):
                        abl += msg.content[num]
                    await ctx.send("Escreva a descrição da habilidade: Digite <!desc 'descrição'>")
                    msg = await bot.wait_for('message')
                    while not msg.content.startswith("!desc "):
                        await ctx.send(
                            "PARÂMETROS ERRADOS!\nEscreva a descrição da habilidade: Digite <!desc 'descrição'>")
                        msg = await bot.wait_for('message')
                    descricao = msg.content.split(" ")[1]
                    rcs_features[int(t_race)] = (abl, descricao)
                    await ctx.send("Habilidades da Raça:\nDeseja adicionar alguma habilidade? (Digite 'n' para sair)")
                    msg = await bot.wait_for('message')
                await ctx.send(f"""Raça: {races[int(t_race)][0]} adicionado(a) ao sistema.""")
            i += 1

    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def listarsistemas(ctx):
    if str(ctx.author) in masters:
        cont = 1
        for key in systems:
            embed = discord.Embed(
                title=f"""**{systems[key][0]}**""",
                description="Informações gerais sobre o sistema:",
                colour=discord.Colour.green()
            )
            embed2 = discord.Embed(
                title="Raças cadastradas",
                description=f"""Estas são as raças cadastradas no sistema **{systems[key][0]}**:""",
                colour=discord.Colour.blue()
            )
            embed3 = discord.Embed(
                title="Classes cadastrados",
                description=f"""Estas são as classes cadastradas no sistema **{systems[key][0]}**:""",
                colour=discord.Colour.red()
            )
            racas = ""
            classes1 = ""
            for status_type, cd_gstatus in systems[key][1].values():
                status1 = ""
                for sig, stat in status[cd_gstatus].items():
                    status1 += f"""{stat}(**{sig}**)\n"""
                embed.add_field(name=f"""**{status_type}:**""", value=status1, inline=True)
            cont2 = 1
            for cd_race in systems[key][2]:
                racas += f"""**{cont2}.** {races[cd_race]}\n"""
                cont2 += 1
            embed2.add_field(name="**Raças:**", value=racas, inline=True)
            cont3=1
            for cd_class in systems[key][3]:
                classes1 += f"""**{cont3}.** {classes[cd_class]}\n"""
                cont3 +=1
            embed3.add_field(name="**Classes:**", value=classes1, inline=True)
            await ctx.send(embed=embed)
            await ctx.send(embed=embed2)
            await ctx.send(embed=embed3)
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def deletarsistema(ctx,*,arg):
    if str(ctx.author) in masters:
        system = arg
        sys_key = -1
        for key,sys in systems.items():
            if system == sys[0]:
                sys_key = key
        if sys_key > -1:
            del systems[sys_key]
            await ctx.send(f"""Sistema: {system} deletado com sucesso!""")
    else:
        await ctx.send(f"""Usuário: {ctx.author} não autorizado a usar esse comando. Somente os mestres têm acesso!""")

@bot.command()
async def teste(ctx):
    await ctx.send('Olá mestre!')

@bot.command()
async def descricao(ctx,tipo,*,objeto):
    if tipo == "raça":
        for raca,foto,desc,idade,tend,tam,motiv,vant,habil in races.values():
            if objeto == raca:
                e_race = discord.Embed(
                    title=f"""**{objeto}**""",
                    description=f"""Ficha da raça {objeto}""",
                    colour=discord.Colour.red()
                )
                e_race.set_image(url=foto)
                e_race.add_field(name="**Descrição**", value=desc, inline=False)
                e_race.add_field(name="**Idade**", value=idade, inline=False)
                e_race.add_field(name="**Tendências**", value=tend, inline=False)
                e_race.add_field(name="**Tamanho**", value=tam, inline=False)
                e_race.add_field(name="**Motivação**", value=motiv, inline=False)
                e_race.add_field(name="**Vantagens**", value=vant, inline=False)
                e_race.add_field(name="**Habilidades**", value=habil, inline=False)
                await ctx.send(embed=e_race)
                return 3
            else:
                await ctx.send(f"""Raça: {objeto} não encontrado.""")
    elif tipo == "classe":
        for classe, foto, dado_vida, tipo, desc, ft_poder, vant, habil in classes.values():
            if objeto == classe:
                e_class = discord.Embed(
                    title=f"""**{objeto}**""",
                    description=f"""Ficha da raça {objeto}""",
                    colour=discord.Colour.blue()
                )
                e_class.set_image(url=foto)
                e_class.add_field(name="**Dado de vida**", value=f"""1D{dado_vida}""", inline=False)
                e_class.add_field(name="**Tipo de classe**", value=tipo, inline=False)
                e_class.add_field(name="**Descrição**", value=desc, inline=False)
                e_class.add_field(name="**Fonte de Poder**", value=ft_poder, inline=False)
                e_class.add_field(name="**Vantagens**", value=vant, inline=False)
                e_class.add_field(name="**Habilidades**", value=habil, inline=False)
                await ctx.send(embed=e_class)
                return 3
            else:
                await ctx.send(f"""Classe: {objeto} não encontrado.""")

bot.load_extension("cogs.music")
bot.load_extension("cogs.assist")
bot.load_extension("cogs.rpg.jogo")
bot.load_extension("cogs.rpg.dado")
#bot.load_extension("cogs.rpg.cadastro")
bot.run('NzIyMjQ2NjIzNjk4MjIzMTk1.XugSlQ.pv0d9wvXHSEwDPEggM8cxJFvlVs')