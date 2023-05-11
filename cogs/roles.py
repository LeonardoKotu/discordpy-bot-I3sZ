import disnake
from main import bot
from disnake.ext import commands

class Button(disnake.ui.View):

    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(
        custom_id="games",
        label='',
        emoji="<:console:1106235121692061777>"
    )

    async def callback_1(self, button, inter):
        if button.custom_id == 'games':
            member = inter.author
            role = inter.guild.get_role(1102006225736056882)
            await member.add_roles(role)
            
        await inter.response.send_message(f":tada: Вы получили роль **Ивента.**", ephemeral=True)


    @disnake.ui.button(
        custom_id="news",
        label='',
        emoji="<:notebook:1106235118743470162>"
    )


    async def callback_2(self, button, inter):
        if button.custom_id == 'news':
            member = inter.author
            role = inter.guild.get_role(1102006228722389133)
            await member.add_roles(role)

        await inter.response.send_message(f":tada: Вы получили роль **Новости.**", ephemeral=True)

    @disnake.ui.button(
        custom_id="staff",
        label='',
        emoji="<:admin:1106235113307643955>"
    )


    async def callback_3(self, button, inter):
        if button.custom_id == 'staff':
            member = inter.author
            role = inter.guild.get_role(1102006227363450950)
            await member.add_roles(role)
        await inter.response.send_message(f":tada: Вы получили роль **Набор.**", ephemeral=True)

    @disnake.ui.button (
        custom_id="bump",
        label="",
        emoji="<:notification:1106235115425763379>"
    )

    async def callback_4(self, button, inter):
        if button.custom_id == "bump":
            member = inter.author
            role = inter.guild.get_role(1102009783306965034)
            await member.add_roles(role)
        await inter.response.send_message(f":tada: Вы получили роль **Бамп.**", ephemeral=True)

class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        bot.add_view(Button())


    @commands.Cog.listener()
    async def on_message(self, message):

        if message.content.startswith('$button'):

            image = disnake.Embed(colour=0x2f3136)

            embed = disnake.Embed(
                title = "<:colorselection:1106235110224826420> Уведомление на сервере Amnesia",
                description=
                """
                ｡︎ »︎ <:console:1106235121692061777> — игры/ивенты
                ｡︎ »︎ <:notebook:1106235118743470162> — новости и обновление 
                ｡︎ »︎ <:admin:1106235113307643955> — набор на стафф
                ｡︎ »︎ <:notification:1106235115425763379> — [бампы](https://discord.com/channels/1100858771347095755/1101908856931623042)
                """,
                colour=0x2f3136
            )

            image.set_image(url="https://avatars.mds.yandex.net/i?id=10ee4271397d119aaab9345b39c8a5d7-4872471-images-thumbs&n=13")
            embed.set_image(url="https://cdn.discordapp.com/attachments/1080131439154176010/1087096393698660503/ScreenShot_20230319223256.jpeg")
            await message.channel.send(embeds=[image, embed], view=Button())


def setup(bot):
    bot.add_cog(Info(bot))