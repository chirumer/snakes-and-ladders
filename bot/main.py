from dotenv import load_dotenv
load_dotenv()

webservice_domain = 'http://board-image.herokuapp.com'

board_img_path = webservice_domain + '/image'

import discord
import os
import json
import urllib.parse

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$board'):

        size = int(message.content.split()[-1])

        embedVar = discord.Embed(title="Snakes And Ladders", color=0x00ff00)
        embedVar.add_field(name="\u200b", value="**Player 1** rolled a 5.")


        data = { 'size': size, 'positions': [('blue', 5), ('red', 2)] }
        json_encoded = json.dumps(data)
        url_encoded = urllib.parse.quote_plus(json_encoded)

        print(f'{board_img_path}?json={url_encoded}')
        embedVar.set_image(url= f'{board_img_path}?json={url_encoded}');
        message = await message.channel.send(embed=embedVar)

        message2 = await message.channel.send('**Player 2** to roll')
        await message2.add_reaction('🎲')

        return;


client.run(os.environ.get('bot_token'));
