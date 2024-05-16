import discord
from discord.ext import commands
import youtube_dl


FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
YDL_OPTIONS = {'format': "bestaudio"}


      
class music(commands.Cog):
  def __init__(self, client):
    self.client = client  
  #allows bot to join vc
  @commands.command()
  async def summon(self, ctx):
    if ctx.author.voice is None:
      await ctx.send("You're not in a voice channel!")
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
      await voice_channel.connect()
    else:
      await ctx.voice_client.move_to(voice_channel)  
  #removes bot from voice channel
  @commands.command()
  async def banish(self, ctx):
    await ctx.voice_client.disconnect()
  #plays music from bot
  @commands.command()
  async def play(self, ctx, url):
    if ctx.voice_client is None:
      await ctx.author.voice.channel.connect()
      FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
      YDL_OPTIONS = {'format': "bestaudio"}
      vc = ctx.voice_client
      with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
        vc.play(source)
    else:
      FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
      YDL_OPTIONS = {'format': "bestaudio"}
      vc = ctx.voice_client
      with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
        vc.play(source)
            
  #pauses the music playing
  @commands.command()
  async def pause(self, ctx):
    try:
      ctx.voice_client.pause()
      await ctx.send("Music has been paused!")
    except:
      await ctx.send(f"{ctx.author.mention} i'm not playing music at the moment!")

  #resumes the music playing
  @commands.command()
  async def resume(self, ctx):
  # Checks if music is paused and resumes it, otherwise sends the player a message that nothing is playing
    try:
      ctx.voice_client.resume()
    except:
      await ctx.send(f"{ctx.author.mention} i'm not playing music at the moment!")

		



    
  

def setup(client):
  client.add_cog(music(client))
