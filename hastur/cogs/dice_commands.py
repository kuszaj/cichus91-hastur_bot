import datetime
from typing import Optional, Union, Any
import discord
from enum import Enum
from discord import Colour
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument
from hastur.dice_utils.RollController import RollController


# class DiceButton(discord.ui.Button):
#
#     def setup(self, data):
#         self.label = data['label']
#         self.custom_id = data['custom_id']
#         self.style = data['style']
#
#     async def callback(self, interaction: discord.Interaction):
#         await self.view.roll_dice(interaction)


class RpgCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.game = "Standard"
        self.roll_controller = RollController()


    @commands.command(name="roll")
    async def standard_roll(self, ctx, dice_amount=1, dice_type=6):
        roll_result_message = self.roll_controller.get_roll_message(dice_amount=dice_amount,
                                                              dice_type=dice_type,
                                                              author=ctx.author.display_name,
                                                              game=self.game)
        for result_embed in roll_result_message:
            await ctx.send(embed=result_embed)


    @commands.command(name="set_game")
    async def dice_settings(self, ctx, game_name):
        response = self.roll_controller.set_game(game_name)
        self.game = response.get("game")
        await ctx.send(response.get("message"))

    @commands.command(name="check")
    async def check_settings(self, ctx):
        await ctx.send(f"{self.game}")


async def setup(bot):
    await bot.add_cog(RpgCommands(bot))

