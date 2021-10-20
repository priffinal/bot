import discord, random, asyncio
from discord import member
from discord.ext import commands, tasks
from itertools import cycle
import youtube_dl

bot = commands.Bot(command_prefix = '.')

status = cycle(['Never', 'Gonna', 'Give', 'You', 'Up'])
# Ready
@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Game('sus'), status = discord.Status.do_not_disturb, )
    change_status.start()
    print('Bot is ready.')

bot.load_extension('dismusic')
# Member join
@bot.event
async def on_member_join(member):
    print(f'{member} đã vào server')
# Member leave
@bot.event
async def on_member_remove(member):
    print(f'{member} đã rời server')
# 8ball
@bot.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ['Sao hỏi tui?', 'Dễ thế mà cx ko bt!', 'Chắc có', 'IDK', 'Nếu đúng chết liền', 'Pablo']
    await ctx.send(f':8ball: {random.choice(responses)}')
# Clear
@bot.command()
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount+1)
# Kick
@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Đã kick {member.mention}')
# Ban
@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Đã ban {member.mention}')
# Unban
@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discrim = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name,user.discriminator) == (member_name,member_discrim):
             await ctx.guild.unban(user)
             await ctx.send(f'Đã unban {user.mention}')
             return
#Status
@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))
# Error
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Biết dùng bàn phím ko?')
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Biết dùng bot ko?')

@bot.command()
async def tkb(ctx, *, x):
    await ctx.send(f'{ctx.message.author.mention} \n```T2: CC, GDCD, CN, Sinh, Toán \nT3: Anh, Toán, Địa, Hóa \nT4: TD, Văn, Văn, Toán \nT5: Anh, Lý, Lý, Sử \nT6: Anh, Văn, Văn, TD \nT7: Tin, Địa, Hóa, Lý, SH```')
bot.run('ODU3OTY0MTQ3NDIwNTYxNDI5.YNXPYA.Gezqr_2GF4SU60LIaOsSl_2NpP4')
