import discord


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")


@client.event
async def on_message(messgage):
    if message.content.startwith("안녕"):
        await message.channel.send("안녕하세요!")

client.run("NTc0NDkyOTM0MTQ2MDk3MTY3.XM6NiA.tL1ouEK_j1SntPVzO9kH5agiPzI")
