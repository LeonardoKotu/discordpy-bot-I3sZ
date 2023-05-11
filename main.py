# Миграция 3.0.
# Бот является информационным(памятка правила), так же может действовать и на ролей

import disnake, os
from disnake.ext import commands

intents = disnake.Intents().all()

bot = commands.InteractionBot(intents=intents)

bot.load_extension("cogs.rules") # правила
bot.load_extension("cogs.roles") # выбор ролей
bot.load_extension("cogs.tickets") # тикеты
bot.load_extension("cogs.verify") # тикеты
#E61254

@bot.event
async def on_ready():
    print(f"{bot.user} - connected!")
    
bot.run(os.environ["DISCORD_TOKEN"])
