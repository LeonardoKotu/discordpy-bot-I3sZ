import disnake
from main import bot
from disnake.ext import commands



class Btn(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(
        label="Купить",
        disabled=True
    )
    
    async def btn(self, btn, inter):
        pass

class Menu1(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    
    @disnake.ui.select(
        placeholder="☘️ Выберите желамое",
        custom_id="menu_shop",
        options=[
            disnake.SelectOption(
                label="Любовные комнаты",
                emoji="💕"
            ),
            disnake.SelectOption(
                label="Кланы",
                emoji="🏫"
            ),
            disnake.SelectOption(
                label="Личные роли",
                emoji="🌌"
            ),
            disnake.SelectOption(
                label="Роль: спасибо!",
                emoji="🧃"
            ),
            disnake.SelectOption(
                label="Снять выбор",
                emoji="❌"
            )
        ]
    )
    
    async def select_callback(self, select, interaction):
        if select.values[0] == "Любовные комнаты":
            love = disnake.Embed(
                
                title="💕 Любовные комнаты, на двоих",
                description="""
                Вы можете создать, для себя лав рум. Для своей **парочке**
                """,
                colour=0xE61254
            
            )
            
            love.add_field(
                name="> Цена - ",
                value="""
                ```2 BOOST / 89.000 Coins```
                """,
                inline=False

            )
            
            love.add_field(
                name="> Условии - ",
                value="""
                `>` Любовная комната, доступна только парнем и девушкой.
                `>` Комната будет доступна только **30 дней**
                """,
                inline=False
            )
            
            love.set_thumbnail(url="https://media.discordapp.net/attachments/1100945663283437578/1107001329483784272/toast.png?width=80&height=80")

            await interaction.response.send_message(embed=love, ephemeral=True)

      
        if select.values[0] == "Кланы":
            clan = disnake.Embed(
                
                title="🏫 Кланы: сообщество людей",
                description="""
                Вы можете создать для себя клан, которые будут **несколько людей.**
                """,
                colour=0xE61254

            
            )
            
            clan.add_field(
                name="> Цена - ",
                value="""
                ```2 BOOST / 100.000 Coins```
                """,
                inline=False
            )
            
            clan.add_field(
                name="> Условии - ",
                value="""
                `>` За существование клана, нужно платить владельцу 5.000 коинов, каждую неделю.
                `>` Комната будет доступна только **2 месяца**
                `>` Название указываете только вы Сами.
                `>` Лимит людей: 10.
                """,
                inline=False
            )
            
            
            clan.set_thumbnail(url="https://media.discordapp.net/attachments/1100945663283437578/1107001329194389544/clan.png?width=80&height=80")
            
            await interaction.response.send_message(embed=clan, ephemeral=True)

        
        if select.values[0] == "Личные роли":
            direct_role = disnake.Embed(
                
                title="🌌 Личные роли",
                description="""
                Создайте для себя **личную роль**.
                """,
                colour=0xE61254

            
            )
            
            direct_role.add_field(
                name="> Цена - ",
                value="""
                ```1 BOOST / 25.000 Coins```
                """,
                inline=False
            )
            
            direct_role.add_field(
                name="> Условии - ",
                value="""
                `>` Название, цвет и иконку указываете только Вы.
                `>` Роль будет действовать только **месяц**.
                """,
                inline=False
            )
            
            
            direct_role.set_thumbnail(url="https://media.discordapp.net/attachments/1100945663283437578/1107001328850436197/user-profile.png?width=80&height=80")
            
            await interaction.response.send_message(embed=direct_role, ephemeral=True)

            
        if select.values[0] == "Роль: спасибо!":
            thanks = disnake.Embed(
                
                title="🧃 Роль за поддержку",
                description="""
                Вы можете получить роль <@&1102307023955165194>, который позволяет отправлять
                фото, видео в **общий чат**.
                """,
                colour=0xE61254

            
            )
            
            thanks.add_field(
                name="> Цена - ",
                value="""
                ```FREE```
                """,
                inline=False
            )
            
            thanks.add_field(
                name="> Условии - ",
                value="""
                `>` Нужно поставить нашу ссылку сервера, в Ваш **био.**
                `>` Ссылка должна быть кликабельной. Если вы уберете обратно, роль удаляется.
                """,
                inline=False
            )
            
            thanks.set_thumbnail(url="https://media.discordapp.net/attachments/1100945663283437578/1107001328586203238/thanks.png?width=80&height=80")
            
            await interaction.response.send_message(embed=thanks, ephemeral=True)
            
        if select.values[0] == "Снять выбор":
            await interaction.response.send_message("Успешно.", ephemeral=True)



class Shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        bot.add_view(Menu1())
        bot.add_view(Menu1())
    
    @commands.Cog.listener()
    async def on_message(self, message):
        image = disnake.Embed(colour=0x2f3136)
        image.set_image(url="https://kartinkin.net/uploads/posts/2021-07/1625607580_45-kartinkin-com-p-kvartal-krasnikh-fonarei-anime-anime-krasi-52.jpg")
        if message.content == "##shop":
            
            embed = disnake.Embed(
                
                title="<:reaction_role_6:1102043551262576710> Магазин ролей Amnesia",
                description="""
                > На нашем сервере, доступные разные **плюшки**, которые вам помогут.
                > Выберите предмет, которые вам нужно. Для получение обращайтесь к <@742344719572533249>/<@602070785632501765>
                """,
                colour=0x2f3236
            )
            
            embed.set_image(url="https://cdn.discordapp.com/attachments/1100945663283437578/1104051567855927398/2023-05-05_16-26-37.png")

           
            await message.channel.send(embeds=[image,embed], view=Menu1())

def setup(bot):
    bot.add_cog(Shop(bot))
