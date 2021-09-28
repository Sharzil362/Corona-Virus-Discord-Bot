import discord
import datetime
from bs4 import BeautifulSoup
import requests
#WEB_SCRAPE
url='https://www.worldometers.info/coronavirus/country/bangladesh/'
result=requests.get(url)
everything = BeautifulSoup(result.text, 'html.parser')
final=everything.find_all(['div'], class_="maincounter-number")
deaths=str(final[1].find('span').get_text())
client = discord.Client()
#TIME
date=datetime.date.today()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('corona'):
        await message.channel.send('Till this date, '+str(date)+','+'  '+'the amount of people that have died due to COVID-19 in Bangladesh is '+str(deaths))

client.run('ODkwNzA2NTgyMjc3NjAzMzM4.YUztJQ.JAABOnjuiP1LCgQnnrwGkD_a04g')