import discord
import json

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

config = {}
print ("Getting config")
with open('config.json') as fs:
    config = json.load(fs)
print ("Config recieved")

client = MyClient()
client.run(config['tokens']['test-server'])