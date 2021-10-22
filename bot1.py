import discord, random, asyncio
from discord import member
from discord.ext import commands, tasks
from itertools import cycle
import music
import keep_alive

bot = commands.Bot(command_prefix = '.')

roles = ctx.get()

status = cycle(['Never', 'Gonna', 'Give', 'You', 'Up'])
# Ready
@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Game('sus'), status = discord.Status.do_not_disturb)
    change_status.start()
    print('Bot is ready.')

# Member join
@bot.event
async def on_member_join(member):
    print(f'{member} đã vào server')
# Member leave
@bot.event
async def on_member_remove(member):
    print(f'{member} đã rời server')
# 8ball
@bot.command(name='8ball', help='Đệ tử Trần Dần.')
async def _8ball(ctx, *, question):
    responses = ['Sao hỏi tui?', 'Dễ thế mà cx ko bt!', 'Chắc có', 'IDK', 'Nếu đúng chết liền', 'Pablo']
    await ctx.send(f':8ball: {random.choice(responses)}')
# Clear
@bot.command(name='clear', help='Xóa tin nhắn.')
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount+1)
# Kick
@bot.command(name='kick', help='Đá mẹ khỏi server luôn!')
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Đã kick {member.mention}')
# Ban
@bot.command(name='ban', help='Khi tôi không muốn gặp lại bạn.')
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Đã ban {member.mention}')
# Unban
@bot.command(name='unban', help='Khi tôi lại muốn gặp lại bạn.')
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
# TKB
@bot.command(name='tkb', help='Thời khóa biểu')
async def tkb(ctx):
    await ctx.send(f'{ctx.message.author.mention} \n```T2: CC, GDCD, CN, Sinh, Toán \nT3: Anh, Toán, Địa, Hóa \nT4: TD, Văn, Văn, Toán \nT5: Anh, Lý, Lý, Sử \nT6: Anh, Văn, Văn, TD \nT7: Tin, Địa, Hóa, Lý, SH```')
# Spam
@bot.command(name='spam', help='Khi bạn gọi thằng Hoàng nhưng nó đêll thèm rep.')
async def spam(ctx, x:int, *, message):
    for i in range(x):
        await ctx.send(message)
# Ping
@bot.command(name='ping', help='Khi bạn thấy mạng lag qué.')
async def ping(ctx):
  await ctx.send(f'Pong :ping_pong:! {int(bot.latency * 1000)}ms')
# Roles test
@bot.command()
async def roles(ctx):
  await ctx.send(f'{ctx.author.roles}')

keep_alive.keep_alive()

bot.run('ODU3OTY0MTQ3NDIwNTYxNDI5.YNXPYA.Gezqr_2GF4SU60LIaOsSl_2NpP4')
