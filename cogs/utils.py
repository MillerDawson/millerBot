import nextcord
from nextcord.ext import commands
from nextcord import Intents, Member

class UtilityCog(commands.Cog):    
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(UtilityCog(bot))