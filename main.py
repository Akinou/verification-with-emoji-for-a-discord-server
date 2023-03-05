import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_reaction_add(reaction, user):
    if str(reaction.emoji) == '👍' and reaction.message.channel.name == 'verification':
        role = discord.utils.get(user.server.roles, name='Unverified')
        await client.remove_roles(user, role)

client.run('YOUR_DISCORD_BOT_TOKEN')
