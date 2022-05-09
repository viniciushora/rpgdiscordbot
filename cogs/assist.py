import discord
from discord.ext import commands

class Assist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='music')
    async def musica(self,ctx):
        embed = discord.Embed(
            title="**Music Commands** :musical_note: ",
            description=f"""Commands for playing music from youtube on **My Rpg Bot**:""",
            colour=discord.Colour.blue()
        )
        embed.add_field(name="**!play** <Youtube URL> or text:", value="Play/Add to queue a Youtube video audio", inline=True)
        embed.add_field(name="**!connect:**", value="Bot connects to your connected voice channel", inline=True)
        embed.add_field(name="**!pause:**", value="Pause the current music", inline=True)
        embed.add_field(name="**!resume:**", value="Resume the current paused music", inline=True)
        embed.add_field(name="**!skip:**", value="Skip the current music and plays the next in queue", inline=True)
        embed.add_field(name="**!stop:**", value="Stop current music, clear the queue and bot leaves the channel", inline=True)
        embed.add_field(name="**!queue:**", value="Show queue/playlist status",inline=True)
        embed.add_field(name="**!now_playing:**", value="Show current music info", inline=True)
        embed.add_field(name="**!volume** <Float number. Ex: 70.8>:", value="Change music volume", inline=True)
        await ctx.send(embed=embed)

    @commands.command(name='rpg')
    async def rpg(self,ctx):
        embed = discord.Embed(
            title="**RPG Commands** :crossed_swords: ",
            description=f"""Commands for RPG features of **My Rpg Bot**:""",
            color=0xf7d92f
        )
        embed.add_field(name="**!rolldice**:", value="Automatic and easier command for dice rolling", inline=True)
        embed.add_field(name="**!roll:** <XdY> X: Dice amount. Y: Dice sides amount:", value="Faster dice rolling command", inline=True)
        await ctx.send(embed=embed)

    @commands.command(name='help')
    async def help(self, ctx):
        embed = discord.Embed(
            title="**My Rpg Bot help section** :tools: ",
            description=f"""Commands for show how to use features of **My Rpg Bot**:""",
            color=0x808080
        )
        embed.add_field(name="**RPG commands :crossed_swords:**", value="!rpg", inline=True)
        embed.add_field(name="**Music commands :musical_note:**",value="!music", inline=True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Assist(bot))