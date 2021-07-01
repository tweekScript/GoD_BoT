import discord
from discord.ext import commands
import datetime

client=commands.Bot(command_prefix='#')
client.remove_command("help")

@client.command()
async def help(ctx):
    embed= discord.Embed(
        title="DBC-BOT-COMMANDS",
        description="List of all Commands" +"\n"+"Command_Prefix-- #",
        colour=discord.Colour.dark_red(),
        author="WarDog"
    )
    embed.set_thumbnail(url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/i/cf806150-5d66-4b08-bc68-8a3ea3b64896/debbdqx-0be4a429-794b-4f31-8382-53d6e2ebaa40.png/v1/fill/w_734,h_811,q_80,strp/ghost_discord_icon_by_inkwoodgfx_debbdqx-fullview.jpg")
    embed.add_field(name='help', value='displaying this list', inline="False")
    embed.add_field(name='server', value='server information', inline="False")
    embed.add_field(name='clear',value='to clear messages',inline="False")
    embed.add_field(name='kick', value='kick members',inline="False")
    embed.add_field(name='ban', value='ban members',inline="False")
    embed.add_field(name='unban', value='unban members',inline="False")

    await ctx.send(embed=embed)

@client.command()
async def server(ctx):
    name=ctx.guild.name
    description=ctx.guild.description
    region=ctx.guild.region
    icon=ctx.guild.icon_url
    member_count=ctx.guild.member_count
    owner=ctx.guild.owner

    embed=discord.Embed(
        title=name+" "+"Server Information",
        description=description,
        colour=discord.Colour.dark_red()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name='Owner: ',value=str(owner))
    embed.add_field(name='Region: ', value=region)
    embed.add_field(name='Members Count: ', value=member_count)

    await ctx.send(embed=embed)

@client.command()
@commands.has_role("alpha")
async def clear(ctx,amount,month=None,day=None,year=None):
    if amount == '-' :
        amount=None
    else:
        amount=int(amount)+1
    if month==None or day==None or year==None:
        date=None
    else:
        date=datetime.datetime(int(year),int(month),int(day))

    await ctx.channel.purge(limit=amount,before=date)

@clear.error
async def clearError(ctx,error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send("You do not have permissions ")

@client.command()
@commands.has_role("alpha")
async def kick(ctx, member: discord.Member,*,reason):
    await member.kick(reason=reason)

@kick.error
async def kick_Error(ctx,error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send("You do not have permissions ")

@client.command()
@commands.has_role("alpha")
async def ban(ctx, member: discord.Member,*,reason):
    await member.ban(reason=reason)

@ban.error
async def ban_Error(ctx,error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send("You do not have permissions ")

@client.command()
@commands.has_role("alpha")
async def unban(ctx,*,member):
    banned_members= await ctx.guild.bans()
    for person in banned_members:
        user=person.user
        if member==str(user):
            await ctx.guild.unban(user)

@unban.error
async def unban_Error(ctx,error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send("You do not have permissions ")

client.run('token')
