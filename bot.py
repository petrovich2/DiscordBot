#===============================================================================#
#=====================         powered by pumpkin          =====================#
#===============================================================================#
#=====================                                     =====================#
#=====================     pumpkin#8186 | @pumpkin_8186    =====================#
#=====================                                     =====================#
#===============================================================================#
#===============================================================================#



import json, requests,asyncio, discord, discord.utils
from discord.ext import commands
from discord import Activity, ActivityType
from art import *
from termcolor import colored
from colorama import Back, Fore, Style, init

PREFIX = '.'

intents = discord.Intents.all()
client = commands.Bot(command_prefix = PREFIX, intents=intents)
client.remove_command('help')
logger = f'{Fore.YELLOW}[{Fore.GREEN}BOT{Fore.YELLOW}][{Fore.GREEN}i{Fore.YELLOW}] {Fore.CYAN}'

tprint('''pumpkin
        discord
                    bot''')


@client.event
async def on_ready():
    print("Бот", colored("pumpkin", 'magenta'), colored("запущен!", "green"))
    await client.change_presence(status = discord.Status.idle, activity = Activity(name = "за порядком", type = ActivityType.watching))

#Команда .about
@client.command(pass_context = True)
async def about(ctx):
    embd = discord.Embed(title="Информация о боте:", color = 0xFF00FF)
    embd.add_field(name = ".about" ,value = "Этот бот был создан *@pumpkin2#8186*\nВсе ошибки/идеи/пожелания писать мне в Telegram или VK.\nTelegram: *@pumpkin_8186*\nVK: *https://vk.com/id510788594*", inline = False)
    await ctx.send(embed = embd)
    author = ctx.message.author
    print(logger + f"Пользователь {author} использовал команду .about ")

#Команда .help
@client.command( pass_context = True )
@commands.has_permissions( view_audit_log = True)
async def help(ctx):
    emb1 = discord.Embed(title="Информация о командах:", color = 0xFF00FF)
    emb1.add_field(name = f"`{PREFIX}clear`: ", value="Очистка сообщений", inline = False)
    emb1.add_field(name = f"`{PREFIX}ban`: ", value="Блокировка участника", inline = False)
    emb1.add_field(name = f"`{PREFIX}unban`: ", value="Разблокировка участника", inline = False)
    emb1.add_field(name = f"`{PREFIX}kick`: ", value="Исключение с сервера", inline = False)
    emb1.add_field(name = f"`{PREFIX}mute`: ", value="выдать мут", inline = False)
    emb1.add_field(name = f"`{PREFIX}tempmute`: ", value="выдать временный мут", inline = False)
    emb1.add_field(name = f"`{PREFIX}unmute`: ", value="Снять мут", inline = False)
    emb1.add_field(name = f"`{PREFIX}dog`: ", value="Рандомная собачка", inline = False)
    emb1.add_field(name = f"`{PREFIX}fox`: ", value="Рандомная лисичка", inline = False)
    emb1.add_field(name = f"`{PREFIX}cat`: ", value="Рандомная кошечка", inline = False)
    emb1.add_field(name = f"`{PREFIX}about`: ", value="Информация о боте", inline = False)
    emb1.add_field(name = f"`{PREFIX}info`: ", value="Информация о пользователе", inline = False)
    emb1.add_field(name = f"`{PREFIX}addrole`: ", value="Выдать роль пользователю", inline = False)
    message = await ctx.send(embed = emb1)
    author = ctx.message.author
    print(logger + f"Пользователь {author} использовал команду .help ")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        author = ctx.message.author
        await ctx.send(f'{author.mention}, команда не найдена!\nВведите **.help** чтобы узнать что я умею!')

@client.command(pass_context = True)
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'{author.mention} привет!\n я БОТ Coddy,\n меня создал **@petrovich2#6661**')
    print(logger + f"Пользователь {author} использовал команду .hello ")

@client.command()
async def fox(ctx):
    await ctx.channel.purge(limit = 1)
    response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xFF00FF, title = 'Лисичка') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed
    author = ctx.message.author
    print(logger + f"Пользователь {author} использовал команду .fox ")

@client.command()
async def cat(ctx):
    await ctx.channel.purge(limit = 1)
    response = requests.get('https://some-random-api.ml/img/cat') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xFF00FF, title = 'Кошечка') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed    
    author = ctx.message.author
    print(logger + f"Пользователь {author} использовал команду .cat ")

@client.command()
async def dog(ctx):
    await ctx.channel.purge(limit = 1)
    response = requests.get('https://some-random-api.ml/img/dog') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    emb3 = discord.Embed(color = 0xFF00FF, title = 'Собачка') # Создание Embed'a
    emb3.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = emb3) # Отправляем Embed 
    author = ctx.message.author
    print(logger + f"Пользователь {author} использовал команду .dog ")

#Очистка сообщений
#Прописываем .clear (число) в нужный чат и удаляются последние сообщения + команда. Макс 100 сообщений
@client.command( pass_context = True )
@commands.has_permissions( view_audit_log = True)
async def clear( ctx, amount = 100):
    await ctx.channel.purge( limit = amount)
    author = ctx.message.author
    print(logger + f"Пользователь {author} использовал команду .clear ")

#Kick
@client.command( pass_context = True )
@commands.has_permissions( view_audit_log = True)
async def kick( ctx, member: discord.Member, *, reason = None ):
    await ctx.channel.purge(limit = 1)
    await member.kick( reason = reason )
    await ctx.send (f'Пользователь {member.mention} исключен с канала! ')
    author = ctx.message.author
    print(logger + f"Пользователь {author} использовал команду .kick  ")
    
#Ban
@client.command( pass_context = True )
@commands.has_permissions( view_audit_log = True)
async def ban (ctx, member: discord.Member, *, reason = None):
    await ctx.channel.purge(limit = 1)
    await member.ban(reason = reason)
    await ctx.send(f'ban user {member.mention}')
    author = ctx.send.mesage.author
    print(logger, f'Пользователь {author} использовал команду .ban')

#unban
@client.command( pass_context = True )
@commands.has_permissions( view_audit_log = True)
async def unban( ctx, *, member,):
    emb = discord.Embed(title = "Мут", color = 0xFF00FF)
    emb.add_field(name = 'Нарушитель', value = member.mention, inline = False)
    emb.set_thumbnail( url = member.avatar_url )
    emb.set_footer( text = 'Разбанен by {}'.format( ctx.author.name ), icon_url = ctx.author.avatar_url )

    banned_users = await ctx.guild.bans()

    for ban_entry in banned_users:
        user = ban_entry.user
        await ctx.guild.unban( user )
    author = ctx.send.mesage.author
    print(logger, f'Пользователь {author} использовал команду .unban')

# команда .info
@client.command()
async def info(ctx,member: discord.Member):
    await ctx.channel.purge(limit = 1)
    emb = discord.Embed(title = 'Информация о пользователе', color = 0xFF00FF)
    emb.add_field(name = 'Когда присоединился', value = member.joined_at, inline = False)
    emb.add_field(name = 'Имя пользователя', value = member.display_name, inline = False)
    emb.add_field(name = "ID", value = member.id, inline = False)
    emb.add_field(name = "Аккаунт был создан:", value = member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'), inline = False)
    emb.set_thumbnail(url = member.avatar_url)
    await ctx.send(embed = emb)

#tempmute
@client.command(pass_context = True)
@commands.has_permissions( view_audit_log = True)
async def tempmute(ctx, member: discord.Member,time:int, reason ):
        muterole = discord.utils.get(ctx.guild.roles, id = 784385223412416524 ) # ID роли
        emb = discord.Embed(title = "Мут", color = 0xFF00FF)
        emb.add_field(name = 'Администратор', value = ctx.message.author.mention, inline = False)
        emb.add_field(name = 'Нарушитель', value = member.mention, inline = False)
        emb.add_field(name = "Причина", value = reason, inline = False)
        emb.add_field(name = "Время", value = time, inline = False)
        await member.add_roles(muterole)
        await ctx.send(embed = emb)
        await asyncio.sleep(time * 60)
        await member.remove_roles(muterole)
        await ctx.send(f"{member.mention} получает право говорить!")
        author = ctx.send.mesage.author
        print(logger, f'Пользователь {author} использовал команду .tempmute')

#MUTE
@client.command(pass_context = True)
@commands.has_permissions( view_audit_log = True)
async def mute(ctx, member: discord.Member,reason ):
        muterole = discord.utils.get(ctx.guild.roles, id = 784385223412416524 ) # ID роли
        emb = discord.Embed(title = "Мут", color = 0xFF00FF)
        emb.add_field(name = 'Администратор', value = ctx.message.author.mention + " выдал перманентный мут" ,inline = False)
        emb.add_field(name = 'Нарушителю', value = member.mention, inline = False)
        emb.add_field(name = "По причине", value = reason, inline = False)
        emb.set_thumbnail( url = member.avatar_url )
        emb.set_footer( text = 'Замучен by {}'.format( ctx.author.name ), icon_url = ctx.author.avatar_url )
        await member.add_roles(muterole)
        await ctx.send(embed = emb)
        author = ctx.send.mesage.author
        print(logger, f'Пользователь {author} использовал команду .mute')

#unmute
@client.command(pass_context = True)
@commands.has_permissions( view_audit_log = True)
async def unmute(   ctx, member: discord.Member, guild: discord.Guild = None):
        guild = ctx.guild if not guild else guild
        muterole = discord.utils.get(ctx.guild.roles, id = 784385223412416524 )# ID роли
        emb = discord.Embed(title = "Размут", color = 0xFF00FF)
        emb.set_author( name = guild, icon_url = guild.icon_url )
        emb.add_field(name = 'Администратор', value = ctx.message.author.mention,inline = False)
        emb.add_field(name = 'Нарушитель', value = member.mention, inline = False)
        emb.set_thumbnail( url = member.avatar_url )
        emb.set_footer( text = 'Размучен by {}'.format( ctx.author.name ), icon_url = ctx.author.avatar_url )
        await ctx.send(embed = emb)
        await member.remove_roles(muterole)
        author = ctx.send.mesage.author
        print(logger, f'Пользователь {author} использовал команду .unmute')

#addrole
@client.command(pass_context = True)
@commands.has_permissions( manage_roles = True )
async def addrole( ctx, member: discord.Member = None, role: discord.Role = None, guild: discord.Guild = None ):
    guild = ctx.guild if not guild else guild
    emb = discord.Embed( title = 'Выдача роли', colour = discord.Color.green())   
    await member.add_roles( role )

    emb.set_author( name = guild, icon_url = guild.icon_url )
    emb.set_footer( text = 'Выдано by {}'.format( ctx.author.name ), icon_url = ctx.author.avatar_url )
    emb.set_thumbnail( url = member.avatar_url )
    emb.add_field( name = 'Роль добавлена пользователю:', value = '{}'.format( member.mention ) )
    emb.add_field( name = 'Добавлена роль', value = '{}'.format( role ) )
    await ctx.send( embed = emb )
    author = ctx.message.author
    print(logger + f"Пользователь {author} использовал команду .addrole ")
    print(member)

@client.event
async def on_member_join(member):
    channel = client.get_channel(458313739121459211)
    role = discord.utils.get(member.guild.roles, id = 781966139415986226)
    await member.add_roles( role ) 
    await channel.send( embed = discord.Embed(description = f"Пользователь ``{member}``, зашёл на сервер! \n И ему присвоена роль 'Ученик' \n {member.mention} напиши своему преподавателю и попроси роль курса!" , color = 0x0c0c0c ))
    print(logger + f" {member} Присоеденился к серверу!")


#создание приватной комнаты
# You can set default values, if u want
default_rooms_initted = False
default_room_category_id = 837348929263239208  #нужно создать категорию для создания приватных комнат и пихнуть в эту переменную её айди
default_room_creator_id = 837349020422111313  #нужно создать в онвой категории канал, и пихуть в эту переменную его айди

room_category = None
room_creator = None

async def delete_channel(guild, channel_id):
        channel = guild.get_channel(channel_id)
        await channel.delete()


async def create_voice_channel(guild, channel_name):
        channel = await guild.create_voice_channel(channel_name, category=room_category)
        return channel

def init_rooms():
    if default_room_category_id != -1:
        category_channel = client.get_channel(default_room_category_id)
        if category_channel:
            global room_category
            room_category = category_channel

    if default_room_creator_id != -1:
        create_channel = client.get_channel(default_room_creator_id)
        if create_channel:
            global room_creator
            room_creator = create_channel
  
    global default_rooms_initted
    default_rooms_initted = True

@client.command(aliases = ['temp_category_set'])
async def __temp_category_set (ctx, id):
    category_channel = client.get_channel(int(id))
    if category_channel:
        global room_category
        room_category = category_channel

@client.command(aliases = ['temp_rooms_set'])
async def __temp_rooms_set (ctx, id):
    create_channel = client.get_channel(int(id))
    if create_channel:
        global room_creator
        room_creator = create_channel

@client.event
async def on_voice_state_update(member, before, after):
    if not default_rooms_initted:
        init_rooms()

    if not room_category:
        print("Set 'Temp rooms category' id first (temp_category_set)")
        return False

    if not room_creator:
        print("Set 'Temp rooms creator' id first (temp_rooms_set)")
        return False

    if member.bot:
        return False
  
    # If user joined to the room creator channel
    if after.channel == room_creator:
        channel = await create_voice_channel(after.channel.guild, f'{member.name} room') # create new voice channel in temp rooms category
        if channel is not None: # if we successfully created our new voice room
            await member.move_to(channel) # move member to new room
            await channel.set_permissions(member, manage_channels=True) # set perm-s to the member
  
    # If user leaved temp room
    if before.channel is not None:
        if before.channel != room_creator and before.channel.category == room_category:
            if len(before.channel.members) == 0:
                await delete_channel(before.channel.guild, before.channel.id)


# RUN
token = "OTc2NTY5ODg5MTYwNTgxMTgw.GxrKPt.CBkKCXa-WOBEofZ-PO9jUZdoT7LHyQIwegtBKI"

client.run(token)
