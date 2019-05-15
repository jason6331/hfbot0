from discord.ext import commands
import discord

bot = commands.Bot(command_prefix = ".")
bot.remove_command("help")

###  ###
# Help #
###  ###

@bot.command()
async def help(ctx, *command):
    c = ''
    for i in command: c = c + ' ' + i
    guild = ctx.guild
    #mod1 = discord.utils.get(guild.roles, name="Moderator")
    #mod2 = discord.utils.get(guild.roles, name="Expert Moderator")
    mod3 = discord.utils.get(guild.roles, name="Leaders")
    jason = discord.utils.get(guild.members, id=368359878651019265)
    if mod3 in ctx.author.roles or ctx.author == jason:
        if c == '':
            embed=discord.Embed(title="Commands of HF Bot", description="`help dm`", color=0x1bb6f1)
            embed.add_field(name="Do `.help help` or `.help dm` for more info about each command.", value="Command from: " + str(ctx.message.channel), inline=True)
            embed.set_footer(text="Bot made by jason6331")
            await ctx.author.send(embed=embed)
        elif c == ' help':
            embed=discord.Embed(title="Commands of HF Bot", description="`.help [commands...]`", color=0x1bb6f1)
            embed.add_field(name="Function:", value="Shows this message.", inline=False)
            embed.set_footer(text="Bot made by jason6331")
            await ctx.author.send(embed=embed)
        elif c == ' dm':
            embed=discord.Embed(title="Commands of HF Bot", description="`.dm <message> [Role Name] [True/False]`", color=0x1bb6f1)
            embed.add_field(name="Function:", value="Sends a dm message to everyone in the server.", inline=False)
            embed.add_field(name="Syntax:", value="`.dm <message> [Role Name] [True/False]`", inline=False)
            embed.add_field(name="**<message>**:", value="The message that will be dm'ed to the users. **If it's more than one word you should use quotation marks (" ").**", inline=False)
            embed.add_field(name="**[Role Name]**:", value="Say the role that should be pinged. **If it's more than one word you should use quotation marks (" ").** Defaults on `everyone`.", inline=False)
            embed.add_field(name="**[True/False]**:", value="Say whether only online users should be pinged or everyone with the role. Defaults on `True` (only online).", inline=False)
            embed.add_field(name="Examples:", value="1) `.dm \"Hello There!\"` or `.dm \"Hello There!\" everyone True` Dm's everyone online. Default values.\n2) `.dm \"Hello There!\" Event` Dm's every online user with the Event role.\n3) `.dm \"Hello There!\" everyone False` Dm's everyone online and offline.\n4) `.dm \"Hello There!\" Event False` Dm's every online and offline user with the Event role.", inline=False)
            embed.add_field(name="Notes:", value="If you use the 3rd parameter, **you must use the 2nd parameter as well!** If you want to use only the 3rd parameter do:\n`.dm \"Hello There!\" everyone [True/False]`", inline=False)
            embed.add_field(name="Pro Tip:", value="You can skip the 2nd and the 3rd parameters and it will just message all the online users (shown in Example 1).", inline=False)
            embed.set_footer(text="Bot made by jason6331")
            await ctx.author.send(embed=embed)
    else:
        await ctx.send("You don't have permission for this command.")

###    ###
#Commands#
###    ###

@bot.command()
@commands.guild_only()
@commands.cooldown(1, 60, commands.BucketType.user)
async def dm(ctx, message, role="everyone", online=True):
    guild = ctx.guild
    #mod1 = discord.utils.get(guild.roles, name="Moderator")
    #mod2 = discord.utils.get(guild.roles, name="Expert Moderator")
    mod3 = discord.utils.get(guild.roles, name="Leaders")
    jason = discord.utils.get(guild.members, id=368359878651019265)
    if mod3 in ctx.author.roles or ctx.author == jason:
        if online == True:
            poor_role = discord.utils.get(guild.roles, name=role)
            if role == "everyone":
                await ctx.send("This may take a while...")
                await ctx.channel.trigger_typing()
                for i in guild.members:
                    if i.status != discord.Status.offline and i.bot == False:
                        bu = discord.utils.get(guild.members, id=575316954928381972)
                        
                        embed=discord.Embed(title=message, color=0x1bb6f1)
                        embed.set_author(name="Help Force", icon_url=bu.avatar_url)
                        await i.send(embed=embed)
                await ctx.send("Job's Done!")
            else:
                if poor_role == None:
                    await ctx.send("This role doesn't exist.")
                else:
                    await ctx.send("This may take a while...")
                    await ctx.channel.trigger_typing()
                    for i in guild.members:
                        if poor_role in i.roles:
                            if i.status != discord.Status.offline and i.bot == False:
                                bu = discord.utils.get(guild.members, id=575316954928381972)

                                embed=discord.Embed(title=message, color=0x1bb6f1)
                                embed.set_author(name="Help Force", icon_url=bu.avatar_url)
                                await i.send(embed=embed)
                    await ctx.send("Job's Done!")
                
        elif online == False:
            poor_role = discord.utils.get(guild.roles, name=role)
            if role == "everyone":
                await ctx.send("This may take a while...")
                await ctx.channel.trigger_typing()
                for i in guild.members:
                    if i.bot == False:
                        bu = discord.utils.get(guild.members, id=575316954928381972)
                        
                        embed=discord.Embed(title=message, color=0x1bb6f1)
                        embed.set_author(name="Help Force", icon_url=bu.avatar_url)
                        await i.send(embed=embed)
                await ctx.send("Job's Done!")
            else:
                if poor_role == None:
                    await ctx.send("This role doesn't exist.")
                else:
                    await ctx.send("This may take a while...")
                    await ctx.channel.trigger_typing()
                    for i in guild.members:
                        if poor_role in i.roles:
                            if i.bot == False:
                                bu = discord.utils.get(guild.members, id=575316954928381972)
                                
                                embed=discord.Embed(title=message, color=0x1bb6f1)
                                embed.set_author(name="Help Force", icon_url=bu.avatar_url)
                                await i.send(embed=embed)
                    await ctx.send("Job's Done!")
    else:
        await ctx.send("You don't have permission for this command.")

###      ###
# On Error #
###      ###

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.channel.send("This command doesn't exist.")
    elif isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.channel.send("An argument is missing.")
    elif isinstance(error, commands.errors.BadArgument):
        await ctx.channel.send("An argument is wrong.")
    elif isinstance(error, commands.NoPrivateMessage):
        await ctx.channel.send("You can only do this command in the server.")
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.channel.send("There is a cooldown for this command (1 minute).")
    else:
        raise error
        
###      ###
#On Message#
###      ###

@bot.event
async def on_message(message):
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Club Penguin Online"))
    
    if message == ".help dm":
        guild = message.guild
        mod1 = discord.utils.get(guild.roles, name="Moderator")
        mod2 = discord.utils.get(guild.roles, name="Expert Moderator")
        mod3 = discord.utils.get(guild.roles, name="Leaders")
        if mod1 in message.author.roles or mod2 in message.author.roles or mod3 in message.author.roles: await bot.process_commands(message)
        else: await message.channel.send("You don't have permission for this command.")
        
    try:
        if message.content[1] != ".": await bot.process_commands(message)
    except IndexError:
        pass

###   ###
#Run Bot#
###   ###
    
bot.run("NTc1MzE2OTU0OTI4MzgxOTcy.XNGL0w.mUXIm6MI28pkgh3cCRLBUp06oaU")
