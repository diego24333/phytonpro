import discord

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)
from bot_logic import gen_pass
@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("tu contraseña"+gen_pass(10))
    else:
        await message.channel.send(message.content)

client.run("MTU1NzkxMTIyNDMwODcyNzkzMQ.G8hC3B.Xy7XYTLTNnBPB_MMDK3c5ANY398JiURlJDetMU")