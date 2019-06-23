from discord.ext import commands
import discord
from random import randint
import os

bot = commands.Bot(command_prefix = ".")
bot.remove_command("help")

###        ###
#Help Command#
###        ###

@bot.command()
async def help(ctx, *command):
    c = ''
    for i in command: c = c + ' ' + i
    if c == '':
        embed=discord.Embed(title="Commands of RiotCraft", description="`.help .ip .store .announce`", color=randint(0,16777215))
        embed.add_field(name="Do `.help <command>` for more info about it.", value="Command from: " + str(ctx.message.channel), inline=True)
        embed.set_footer(text="Bot made by me...")
        await ctx.author.send(embed=embed)
    elif c == ' help':
        embed=discord.Embed(title="Commands of RiotCraft", description="`.help [commands...]`", color=randint(0,16777215))
        embed.add_field(name="Function:", value="Shows this message.", inline=False)
        embed.set_footer(text="Bot made by me...")
        await ctx.author.send(embed=embed)
    elif c == ' ip':
        embed=discord.Embed(title="Commands of RiotCraft", description="`.ip`", color=randint(0,16777215))
        embed.add_field(name="Function:", value="Shows the ip of RiotCraft.", inline=False)
        embed.set_footer(text="Bot made by me...")
        await ctx.author.send(embed=embed)
    elif c == ' store':
        embed=discord.Embed(title="Commands of RiotCraft", description="`.store`", color=randint(0,16777215))
        embed.add_field(name="Function:", value="Shows the server's store link.", inline=False)
        embed.set_footer(text="Bot made by me...")
        await ctx.author.send(embed=embed)
    elif c == ' announce':
        embed=discord.Embed(title="Commands of RiotCraft", description="`.announce <channel> <message>`", color=randint(0,16777215))
        embed.add_field(name="Function:", value="Announces a message to a channel.", inline=False)
        embed.add_field(name="Example:", value="`.announce #general You are dumb!!`", inline=False)
        embed.set_footer(text="Bot made by me...")
        await ctx.author.send(embed=embed)

###            ###
#General commands#
###            ###

@bot.command()
@commands.guild_only()
async def announce(ctx, ch, *message):
    guild = ctx.guild
    owner = discord.utils.get(guild.roles, id=591643694789034006)
    if owner in ctx.author.roles:
        c = ''
        for i in message: c = c + ' ' + i
        channel = discord.utils.get(guild.text_channels, mention=ch)
        await channel.send(c)
        await ctx.send("Message Announced!")
    else:
        await ctx.send("You do not have permission to use this command.")

@bot.command()
async def ip(ctx):
    await ctx.send("**IP**: riotcraft.club")

@bot.command()
async def store(ctx):
    await ctx.send("**STORE**: store.riotcraft.club")

###          ###
#Command Errors#
###          ###

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass #await ctx.channel.send("This command doesn't exist.")
    elif isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.channel.send("An argument is missing.")
    elif isinstance(error, commands.errors.BadArgument):
        await ctx.channel.send("An argument is wrong.")
    elif isinstance(error, commands.NoPrivateMessage):
        await ctx.channel.send("You can only do this command in the server.")
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.channel.send("There is a cooldown for this command.")
    else:
        raise error
###   ###
#On Join#
###   ###

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, id=591647376905863168)
    await channel.send("<:riot_emoji:591655597317816330> | Hello " + member.mention + " welcome to the official Discord Server of **RiotCraft**\n\nRiotCraft is a Skyblock Minecraft server where you have to develop your island to become the number one island in the server, If you are strong and have the best island in the server you are obviously going to win some cool and crazy rewards.\n\nAdditional Information:\n**Store**: https://store.riotcraft.com/\n**Discord**: https://discord.gg/Wv3TGYD")

###   ###
#Run Bot#
###   ###

bot.run(os.environ.get("token"))
