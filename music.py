import discord
from discord.ext import commands
from discord.ext.commands.core import command
import youtube_dl

class music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send('Vào VC đi thg ngu!')
        voice_channel = ctx.author.voice.channel
        if ctx.voice_bot is None:
            await voice_channel.connect()
        else:
            await ctx.voice_bot.move_to(voice_channel)
    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_bot.disconnect()
    @commands.command()
    async def play(self, ctx, url):
        ctx.voice_bot.stop()
        FFMPEG_OPTIONS = {'before options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format':"bestaudio"}
        vc = ctx.voice_bot

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['format'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)
    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_channel.pause()
        await ctx.send('Đã dừng phát nhạc :pause_button:.')
    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_channel.resume()
        await ctx.send('Đã phát lại nhạc :arrow_forward:.')

def setup(bot):
    bot.add_cog(music(bot)) 