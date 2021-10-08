from dotenv import load_dotenv
load_dotenv()

board_img = 'https://board-image.herokuapp.com/image'

import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):

        embedVar = discord.Embed(title="Snakes And Ladders", color=0x00ff00)
        embedVar.add_field(name="\u200b", value="**Player 1** rolled a 5.")
        embedVar.set_image(url=board_img);
        message = await message.channel.send(embed=embedVar)

        message2 = await message.channel.send('**Player 2** to roll')
        await message2.add_reaction('🎲')

        return;


client.run(os.environ.get('bot_token'));
