import discord

with open('.env','r') as env:
    TOKEN = env.read()

print(TOKEN)
client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!daphne"):
        await message.channel.send('daphne is dead')

client.run(TOKEN)