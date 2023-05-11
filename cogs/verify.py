import disnake
from disnake.ext import commands
from main import bot

class Verify(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @disnake.ui.button(label="Парень", emoji="♂️", custom_id="male")
    
    async def button_callback(self, button, interaction):
        if button.custom_id == "male":
            role = interaction.guild.get_role(1101070122128523336)
            member = interaction.user
            await member.add_roles(role)
            
            await interaction.response.send_message("> :tada: Верификация пройдена! Желаем удачи!", ephemeral=True)

    @disnake.ui.button(label="Девушка", emoji="♀️", custom_id="female")

    async def button_callback2(self, button, interaction):
        if button.custom_id == "female":
            role = interaction.guild.get_role(1102304274408546334)
            member = interaction.user
            await member.add_roles(role)

            await interaction.response.send_message("> :tada: Верификация пройдена! Желаем удачи!", ephemeral=True)

class Ddx(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
          bot.add_view(Verify())
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith('$verify'):
            embed = disnake.Embed(
                title="<:WHITE_Weed:1101889257641083012>  Добро пожаловать в Amnesia!", 
                description=
                """Благодарим за ваш вход! Чтобы продолжить, укажите ваш **пол**.
                ||`P.s`|| если вдруг верификация не сработало, просим обратиться к <@742344719572533249>/<@602070785632501765>""",
                colour=0x2f3236
                )
            embed.set_footer(text="Хорошего времяпровождение!")
            embed.set_image(url="https://images-ext-1.discordapp.net/external/cN1w1zlioFrh_tLW8MCSjrddMOgFz0z7YsC3Wdaxud8/https/i.pinimg.com/564x/c8/73/a1/c873a1497b5c6f41d01d06a5391c3f2c.jpg?width=702&height=268")

            await message.channel.send(embed=embed, view=Verify())

def setup(bot):
    bot.add_cog(Ddx(bot))
  