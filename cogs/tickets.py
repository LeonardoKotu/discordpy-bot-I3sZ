import disnake
from disnake.ext import commands
from main import bot

# Наследуем модальное окно
class Menu(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.select(
        custom_id="select",
        placeholder="🔑 Выберите тип обращение",
        min_values=1,
        max_values=1,
        options = [
            disnake.SelectOption(

                label="Жалоба",
                description = "Жалоба на стафф/участник",
                emoji="<:lightbulb:1106247511863214100>"
            ),

            disnake.SelectOption(
                label="Идея & Баги",
                description="Предложение для развитие сервера/нахождение багов",
                emoji="<:businessman:1106247513998110861>"
            ),

            disnake
            .SelectOption(
                label="Снять выбор",
                emoji="<:xmark:1104181267941032049>"
            ),

        ]
        )


    # Обработка ответа, после отправки модального окна
    async def callback(self, select, inter):

        # если пользователь нажал на жалобу
        if select.values[0] == "Жалоба":

            cat = disnake.utils.get(inter.guild.categories, name="—  •  🔐 Тикеты") # категория
            global channel
            channel = await inter.guild.create_text_channel(f'🔖обращение-от-{inter.author}', category=cat) # создаем канал на этой категории

            '''отправляем эмбед'''
            embed_zaloba = disnake.Embed(
                title = "Обращение на тему `жалоба`",
                description=
                """
                > <:wait:1106247508943978546> Опишите вашу проблему, *причину* и *ник* человека которые вы захотили **пожаловаться**.
                > За ложный тикет, вы будете **замьючены.**
                """,
                colour = 0x34582
            )

            # настройка
            
            await channel.send(content=f"{inter.user.mention} / <@&1100946600886534177>", embed=embed_zaloba) # отправка сообщений, после нажатий меню
            
            await channel.set_permissions(inter.guild.default_role, read_messages=False) # это установит роле @everyone запрет на просмотр чата
            await channel.set_permissions(inter.user, read_messages=True, send_messages=True) # указываем права

            await inter.response.send_message(f"Для вас создана канал обращение - <#{channel.id}>, желаем удачи!", ephemeral=True) # сообщение о том что все успешно

            log_channel = inter.guild.get_channel(1100900722855387196)

            new_log = disnake.Embed(
            title = f"{inter.user}, создал тикет",
            description=
            f"""
            {inter.user.mention} создал тикет, на канале <#{channel.id}>
            Тип: {select.values[0]}
            """
        )
            await log_channel.send(embed=new_log)


        if select.values[0] == "Идея & Баги":

            cat = disnake.utils.get(inter.guild.categories, name="—  •  🔐 Тикеты") # категория
            channel = await inter.guild.create_text_channel(f'💡обращение-от-{inter.author}', category=cat) # создаем канал на этой категории

            '''отправляем эмбед'''
            embed_zaloba = disnake.Embed(
                title = "<:wait:1106247508943978546> Обращение на тему `Идея & Баги`",
                description=
                """
                > Расскажите **идею** для развитие сервера, или **баг** в котором вы заметили на сервере.
                > За ложный тикет, вы будете **замьючены.**
                """,
                colour = 0x39e582
            )

            # настройка
            
            await channel.send(content=f"{inter.user.mention} / <@&1100946600886534177>", embed=embed_zaloba) # отправка сообщений, после нажатий меню
            
            await channel.set_permissions(inter.guild.default_role, read_messages=False) # это установит роле @everyone запрет на просмотр чата
            await channel.set_permissions(inter.user, read_messages=True, send_messages=True) # указываем права

            await inter.response.send_message(f"Для вас создана канал обращение - <#{channel.id}>, желаем удачи!", ephemeral=True) # сообщение о том что все успешно

            log_channel = inter.guild.get_channel(1100900722855387196)

            new_log = disnake.Embed(
            title = f"{inter.user}, создал тикет",
            description=
            f"""
            {inter.user.mention} создал тикет, на канале <#{channel.id}>
            Тип: {select.values[0]}
            """
        )
            await log_channel.send(embed=new_log)


        if select.values[0] == "Снять выбор":

            await inter.response.send_message("Успешно.", ephemeral=True) # сообщение о том что все успешно



class Titckets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        bot.add_view(Menu())

    @commands.Cog.listener()    
    async def on_message(self, message):
        if message.content == "#tickets":
            image = disnake.Embed(colour=0x2f3136)
            image.set_image(url="https://i.pinimg.com/564x/28/7d/a5/287da59776dd76ec83b8ff21ef1062b9.jpg")
            
            
            embed = disnake.Embed(
                title = "<:complain:1106247517437427782> Помощь вместе с Amnesia!",
                description=
                """
                > `-` Это канал поддержки. Выберите тип *обращение*, который вы хотите **обратиться**.
                > `-` Через некоторое время, вам ответит **стафф**.
                """,
                colour = 0x2f3136

            )

            embed.set_image(url="https://cdn.discordapp.com/attachments/1100945663283437578/1104051567855927398/2023-05-05_16-26-37.png")

            await message.channel.send(embeds=[image, embed], view=Menu())

    @commands.slash_command(description="Закрыть тикет")
    async def close(self, inter):
        await channel.delete()

def setup(bot):
    bot.add_cog(Titckets(bot))