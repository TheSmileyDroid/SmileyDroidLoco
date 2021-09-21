import asyncio
import gtts
from utils import get_voice_client
import discord
from discord import *
from discord.ext import commands
from discord.ext.commands.context import Context


class FalarCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def f(self, ctx: Context, *text: str):
        #if ctx.author.name != "SmileyDroid" :
        #      await ctx.author.send('Você não é o sorriso, você é {}'.format(ctx.author.name))
        #      return
        voice = await get_voice_client(ctx, None)
        txt = ''
        for t in text:
          txt += t + ' '
        tts = gtts.tts.gTTS(text=txt, lang="pt-br", slow=False)

        tts.save("cache/audio.mp3")

        voice.play(discord.FFmpegPCMAudio("cache/audio.mp3"))

        while voice.is_playing():
            await asyncio.sleep(1)
        voice.stop()
    
    @commands.command()
    async def falar(self, ctx: Context, text: str, channel: str = None, lang: str = "pt-br"):
        #if ctx.author.name != "SmileyDroid" :
        #    await ctx.author.send('Você não é o sorriso, você é {}'.format(ctx.author.name))
        #    return
        voice = await get_voice_client(ctx, channel)

        tts = gtts.tts.gTTS(text=text, lang=lang, slow=False)

        tts.save("cache/audio.mp3")

        voice.play(discord.FFmpegPCMAudio("cache/audio.mp3"))

        while voice.is_playing():
            await asyncio.sleep(10)
        voice.stop()
      
    @commands.command()
    async def n(self, ctx: Context, channel: str = None, lang: str = "pt-br"):
        voice = await get_voice_client(ctx, channel)

        tts = gtts.tts.gTTS(text="não", lang=lang, slow=False)

        tts.save("audio.mp3")

        voice.play(discord.FFmpegPCMAudio("audio.mp3"))

        while voice.is_playing():
            await asyncio.sleep(1)
        voice.stop()
    @commands.command()
    async def s(self, ctx: Context, channel: str = None, lang: str = "pt-br"):
        voice = await get_voice_client(ctx, channel)

        tts = gtts.tts.gTTS(text="sim", lang=lang, slow=False)

        tts.save("audio.mp3")

        voice.play(discord.FFmpegPCMAudio("audio.mp3"))

        while voice.is_playing():
            await asyncio.sleep(1)
        voice.stop()
    
