#imports
import discord
import os
import requests
import json
import async_timeout
from keep_alive import keep_alive
from discord.ext import commands
import interact
import music

try:
    my_secret = os.environ['TOKEN']
except:
    os.system("kill 1")
#initialize bot
#my_secret = os.environ['TOKEN']
client = discord.Client()
#initialize opus
cogs = [music]
#initialize commands
client = commands.Bot(command_prefix='~')
client.remove_command('help')
#initialize music
for i in range(len(cogs)):
    cogs[i].setup(client)
#initialize interaction


#code for removing extra characters from rizz
def get_quote():
    response = requests.get("https://vinuxd.vercel.app/api/pickup")
    json_data = json.loads(response.text)
    quote = str(json_data)
    quote = quote.replace('{', '')
    quote = quote.replace('}', '')
    quote = quote.replace("'id':", '')
    quote = quote.replace("'line': ", '')
    quote = quote.replace('"', '')
    quote = quote.replace("'", "")
    quote = quote.replace(",", "", 1)
    quote = quote.replace('pickup: ', '')
    print(quote[1] + quote[2])
    if quote[1].isdigit():
        quote = quote.replace(quote[1], '')
    print(quote[1] + quote[2])
    if quote[1].isdigit():
        quote = quote.replace(quote[1], '')
    return quote


##commands ##
#rizz asks the bot for a random pickup line
@client.command()
async def rizz(ctx):
    quote = get_quote()
    await ctx.send(quote)


@client.command()
async def kiss(ctx, *, member):
    kiss = interact.get_kiss()
    embed = discord.Embed(
        description=f"{ctx.author.mention} {'kisses '} {member}",
        color=0xB4F8C8)
    embed.set_image(url=kiss)
    await ctx.send(embed=embed)


@client.command()
async def wave(ctx, *, member):
    wave = interact.get_wave()
    embed = discord.Embed(
        description=f"{ctx.author.mention} {'waves at '} {member}",
        color=0xB4F8C8)
    embed.set_image(url=wave)
    await ctx.send(embed=embed)


@client.command()
async def poke(ctx, *, member):
    poke = interact.get_poke()
    embed = discord.Embed(
        description=f"{ctx.author.mention} {'pokes '} {member}",
        color=0xB4F8C8)
    embed.set_image(url=poke)
    await ctx.send(embed=embed)


@client.command()
async def pat(ctx, *, member):
    pat = interact.get_pat()
    embed = discord.Embed(
        description=f"{ctx.author.mention} {'pats '} {member}", color=0xB4F8C8)
    embed.set_image(url=pat)
    await ctx.send(embed=embed)


@client.command()
async def wink(ctx, *, member):
    wink = interact.get_wink()
    embed = discord.Embed(
        description=f"{ctx.author.mention} {'winks at '} {member}",
        color=0xB4F8C8)
    embed.set_image(url=wink)
    await ctx.send(embed=embed)


@client.command()
async def handhold(ctx, *, member):
    handhold = interact.get_handhold()
    embed = discord.Embed(
        description=f"{ctx.author.mention} {'holds hands with '} {member}",
        color=0xB4F8C8)
    embed.set_image(url=handhold)
    await ctx.send(embed=embed)


@client.command()
async def hug(ctx, *, member):
    hug = interact.get_hug()
    embed = discord.Embed(
        description=f"{ctx.author.mention} {'hugs '} {member}", color=0xB4F8C8)
    embed.set_image(url=hug)
    await ctx.send(embed=embed)


@client.command()
async def nuzzle(ctx, *, member):
    nuzzle = interact.get_nuzzle()
    embed = discord.Embed(
        description=f"{ctx.author.mention} {'nuzzles with '} {member}",
        color=0xB4F8C8)
    embed.set_image(url=nuzzle)
    await ctx.send(embed=embed)


@client.command()
async def cuddle(ctx, *, member):
    cuddle = interact.get_cuddle()
    embed = discord.Embed(
        description=f"{ctx.author.mention} {'cuddles with '} {member}",
        color=0xB4F8C8)
    embed.set_image(url=cuddle)
    await ctx.send(embed=embed)


@client.command()
async def dance(ctx, *, member):
    dance = interact.get_dance()
    embed = discord.Embed(
        description=f"{ctx.author.mention} {'dances with '} {member}",
        color=0xB4F8C8)
    embed.set_image(url=dance)
    await ctx.send(embed=embed)


@client.command()
async def celebrate(ctx, *, member):
    celebrate = interact.get_celebrate()
    embed = discord.Embed(
        description=f"{ctx.author.mention} {'celebrates with '} {member}",
        color=0xB4F8C8)
    embed.set_image(url=celebrate)
    await ctx.send(embed=embed)


@client.command()
async def airkiss(ctx, *, member):
    airkiss = interact.get_airkiss()
    embed = discord.Embed(
        description=f"{ctx.author.mention} {'blows a kiss at '} {member}",
        color=0xB4F8C8)
    embed.set_image(url=airkiss)
    await ctx.send(embed=embed)


@client.command()
async def lick(ctx, *, member):
    lick = interact.get_lick()
    embed = discord.Embed(
        description=f"{ctx.author.mention} {'licks '} {member}",
        color=0xB4F8C8)
    embed.set_image(url=lick)
    await ctx.send(embed=embed)


@client.command()
async def slap(ctx, *, member):
    slap = interact.get_slap()
    embed = discord.Embed(
        description=f"{ctx.author.mention} {'slaps '} {member}",
        color=0xB4F8C8)
    embed.set_image(url=slap)
    await ctx.send(embed=embed)


@client.command()
async def smack(ctx, *, member):
    smack = interact.get_smack()
    embed = discord.Embed(
        description=f"{ctx.author.mention} {'smacks '} {member}",
        color=0xB4F8C8)
    embed.set_image(url=smack)
    await ctx.send(embed=embed)


@client.command()
async def punch(ctx, *, member):
    punch = interact.get_punch()
    embed = discord.Embed(
        description=f"{ctx.author.mention} {'punches '} {member}",
        color=0xB4F8C8)
    embed.set_image(url=punch)
    await ctx.send(embed=embed)


@client.command()
async def pout(ctx):
    pout = interact.get_pout()
    embed = discord.Embed(description=f"{ctx.author.mention} {'pouts'}",
                          color=0xB4F8C8)
    embed.set_image(url=pout)
    await ctx.send(embed=embed)


@client.command()
async def blush(ctx):
    blush = interact.get_blush()
    embed = discord.Embed(description=f"{ctx.author.mention} {'blushes'}",
                          color=0xB4F8C8)
    embed.set_image(url=blush)
    await ctx.send(embed=embed)


#Embeds help category for music
@client.command(name='help')
async def help(ctx):
    embed = discord.Embed(
        title=":books: Help",
        description="Use `~<category name>` to see its commands!",
        color=0xB4F8C8)
    embed.add_field(name=":musical_keyboard: Music",
                    value='List of commands for music.',
                    inline=True)
    embed.add_field(name=":scream: Reactions",
                    value='Reaction gifs and quotes to use o your friends/',
                    inline=True)
    await ctx.send(embed=embed)


#Embeds help category for music
@client.command(name='help music', aliases=['music'])
async def help_music(ctx, *music):
    embed = discord.Embed(
        title=":musical_keyboard: MattBot Music Commands",
        description="Use `~help` to return to the help categories",
        color=0xB4F8C8)
    embed.add_field(name="~banish",
                    value='banishes the bot to his home',
                    inline=True)
    embed.add_field(name="~play",
                    value='adds a song to the queue',
                    inline=True)
    embed.add_field(name='~pause',
                    value='pauses the current song',
                    inline=True)
    embed.add_field(name='~resume',
                    value='resumes the current song',
                    inline=True)
    embed.add_field(name='~queue',
                    value='shows the songs in the queue',
                    inline=True)
    embed.add_field(name='~clear',
                    value='clears the current queue',
                    inline=True)
    embed.add_field(name='~skip', value='skips the current songs', inline=True)
    await ctx.send(embed=embed)


#Embeds help category for reactions
@client.command(name='help reactions', aliases=['reactions'])
async def help_reactions(ctx, *reactions):
    embed = discord.Embed(
        title=":scream: MattBot Reaction Commands",
        description="Use `~help` to return to the help categories",
        color=0xB4F8C8)
    embed.add_field(name="~wave", value='waves at mentioned user', inline=True)
    embed.add_field(name="~poke", value='pokes mentioned user', inline=True)
    embed.add_field(name='~pat', value='pats the mentioned user', inline=True)
    embed.add_field(name='~wink',
                    value='winks at the mentioned user',
                    inline=True)
    embed.add_field(name='~handhold',
                    value='holds hand the mentioned user',
                    inline=True)
    embed.add_field(name="~hug", value='hugs mentioned user', inline=True)
    embed.add_field(name='~nuzzle',
                    value='nuzzles the mentioned user',
                    inline=True)
    embed.add_field(name='~cuddle',
                    value='cuddles the mentioned user',
                    inline=True)
    embed.add_field(name='~dance',
                    value='dances the mentioned user',
                    inline=True)
    embed.add_field(name='~celebrate',
                    value='celebrates with the mentioned user',
                    inline=True)
    embed.add_field(name='~kiss',
                    value='kisses the mentioned user',
                    inline=True)
    embed.add_field(name='~airkiss',
                    value='air kisses the mentioned user',
                    inline=True)
    embed.add_field(name='~lick',
                    value='licks the mentioned user',
                    inline=True)
    embed.add_field(name='~slap',
                    value='slaps the mentioned user',
                    inline=True)
    embed.add_field(name='~smack',
                    value='smacks the mentioned user',
                    inline=True)
    embed.add_field(name='~punch',
                    value='punches the mentioned user',
                    inline=True)

    await ctx.send(embed=embed)



#keeps app running... Do Not Touch
keep_alive()
#shows when app is ready
print('MattBotV2 is now Online!')
#run bot... Do Not Touch
client.run(my_secret)
