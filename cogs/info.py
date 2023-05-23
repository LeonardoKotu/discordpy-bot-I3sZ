import disnake
from disnake.ext import commands
from bot import bot

class Navigator(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @disnake.ui.select(
        placeholder="Выберите тип каналов",
        custom_id="menu_navigation",
        options = 
        [
            disnake.SelectOption(
                label="Важное",
                emoji="<:information1:1110320661458604052>"
            ),
            
            disnake.SelectOption(
                label="Контент",
                emoji="<:contentwriting:1110320659403374674>"
            ),
            
            disnake.SelectOption(
                label="Общение",
                emoji="<:chat1:1110320657440444517>"
            ),
            
            disnake.SelectOption(
                label="Медиа",
                emoji="<:imagegallery:1110320654940635216>"
            ),
            
            disnake.SelectOption(
                label="Помощь",
                emoji="<:helpinghand:1110320648275886190>"
            )
            
        ]
    )
    
    async def select_callback(self, select, interaction):
        if select.values[0] == "Важное":
            embed = disnake.Embed(
                description=
                """
                <:white_dot2:1101889261432737844> <#1100869606106742926> — информация о сервере
                <:white_dot2:1101889261432737844> <#1100869520542945330> — правила сервера
                <:white_dot2:1101889261432737844> <#1105581204746543176> — партнёры нашего сервера
                <:white_dot2:1101889261432737844> <#1105580904602144848> — магазин эксклюзивных вещей

                """,
                colour=0x2f3136
            )
            
            await interaction.response.send_message(embed=embed,ephemeral=True)
        
        if select.values[0] == "Контент":
            embed = disnake.Embed(
                description=
                """
                <:white_dot2:1101889261432737844> <#1100935258154745947> — розыгрыши сервера
                <:white_dot2:1101889261432737844> <#1100935846170988606> — новости сообщества
                <:white_dot2:1101889261432737844> <#1109258218363965480> — различные ивенты
                <:white_dot2:1101889261432737844> <#1100935350534283295> — набор на стафф
                """,
                colour=0x2f3136
            )
            
            await interaction.response.send_message(embed=embed, ephemeral=True)
        
        if select.values[0] == "Общение":
            embed = disnake.Embed(
                description=
                """
                <:white_dot2:1101889261432737844> <#1100936743416516608> — основной чат
                <:white_dot2:1101889261432737844> <#1100937772858089573> — команды, флуд
                <:white_dot2:1101889261432737844> <#1100943803357069432> — Марк знает
                <:white_dot2:1101889261432737844> <#1109259175743201345> — знакомства
                """,
                colour=0x2f3136
            )
            
            await interaction.response.send_message(embed=embed, ephemeral=True)
        
        if select.values[0] == "Медиа":
            embed = disnake.Embed(
                description=
                """
                <:white_dot2:1101889261432737844> <#1102004091795804271> — медиа, скрины
                <:white_dot2:1101889261432737844> <#1102004191255343104> — селфи
                <:white_dot2:1101889261432737844> <#1102004345844801546> — фотки в реальной жизни
                """,
                colour=0x2f3136
            )
            
            await interaction.response.send_message(embed=embed, ephemeral=True)
            
        if select.values[0] == "Помощь":
            embed = disnake.Embed(
                description=
                """
                <a:aesthetic:1101997697088626829> <#1102004091795804271> — обращение, тикеты
                <a:aesthetic:1101997697088626829> <#1102004191255343104> — бампы с помощью ботов
                """,
                colour=0x2f3136
            )
            
            await interaction.response.send_message(embed=embed, ephemeral=True)

class Notification(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @disnake.ui.select(
        placeholder="Выберите роли оповещении",
        custom_id="notifi",
        options=[
            disnake.SelectOption(
                label="Новости",
                emoji="<:news:1110325508320792717>"
            ),
            disnake.SelectOption(
                label="Ивенты",
                emoji="<:game:1110325499558908117>"
            ),
            disnake.SelectOption(
                label="Бампы",
                emoji="<:bell:1110325505032470528>"
            ),
            disnake.SelectOption(
                label="Стафф",
                emoji="<:shield:1110325496807432212>"
            )
        ]
    )
    
    async def select_callback(self, select, interaction):
        if select.values[0] == "Новости":
            role = interaction.guild.get_role(1102006228722389133)
            member = interaction.user
            await member.add_roles(role)
            
            await interaction.response.send_message("> Теперь вы будете получили оповещение **новости и обновлении**", ephemeral=True)

        if select.values[0] == "Ивенты":
            role = interaction.guild.get_role(1102006225736056882)
            member = interaction.user
            await member.add_roles(role)
                
            await interaction.response.send_message("> Теперь вы будете получили оповещение **ивенты**", ephemeral=True)

        if select.values[0] == "Бампы":
            
            role = interaction.guild.get_role(1102009783306965034)
            member = interaction.user
            await member.add_roles(role)
                
            await interaction.response.send_message("> Теперь вы будете получили оповещение **бампы**", ephemeral=True)

        if select.values[0] == "Стафф":
            role = interaction.guild.get_role(1102006227363450950)
            member = interaction.user
            await member.add_roles(role)
                
            await interaction.response.send_message("> Теперь вы будете получили оповещение **стафф**", ephemeral=True)

        
class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    #2C71E6
    @commands.Cog.listener()
    async def on_ready(self):
        bot.add_view(Navigator())
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "nav!":
            image = disnake.Embed(colour=0x2f3136)
            image.set_image(url="https://i.pinimg.com/564x/ce/d8/4a/ced84adf18ce017d24cf12428d198ed5.jpg")
            
            embed = disnake.Embed(
                title="",
                description="```yaml\n🌠ㅤㅤㅤㅤㅤㅤㅤㅤㅤНавигаторㅤㅤㅤㅤㅤㅤㅤㅤㅤ```\n > · <:information1:1110320661458604052> — справка по серверу\n > · <:contentwriting:1110320659403374674> — событие сервера\n> · <:chat1:1110320657440444517> — общение & развлечение\n> · <:imagegallery:1110320654940635216> — медиа\n> · <:helpinghand:1110320648275886190> — помощь amnesia",
                colour=0x2f3136
            )
             
            embed.set_image(url="https://i.imgur.com/2GxE5Kn.gif")
            await message.channel.send(embeds=[image, embed], view=Navigator())

        if message.content == "roles!":
            
            embed = disnake.Embed(
                title = "",
                description="```yaml\n🌠ㅤㅤㅤㅤㅤㅤㅤㅤㅤОповещенииㅤㅤㅤㅤㅤㅤㅤㅤㅤ```\n > · <:news:1110325508320792717> — новости\n > · <:game:1110325499558908117> — ивенты/розыгрыши и конкурсы\n > · <:bell:1110325505032470528> — мониторинг ботов\n > · <:shield:1110325496807432212> — состав администрации",
                colour=0x2f3136
            )
            
            embed.set_image(url="https://i.imgur.com/2GxE5Kn.gif")
            await message.channel.send(embed=embed, view=Notification())

def setup(bot):
    bot.add_cog(Commands(bot))