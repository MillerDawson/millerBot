import nextcord
from nextcord.ext import commands
from nextcord import Intents, Member

class FunCog(commands.Cog):    
    def __init__(self, bot):
        self.bot = bot

    # ASIMULATOR LICK COMMAND
    @commands.command()
    @commands.guild_only()
    async def lick(self, ctx:commands.Context, member:Member, *, reason:str=None):
        await ctx.send(f"I have licked {member.mention}! Yummy!!") 

    @lick.error    # LICK VALIDATION
    async def lick_err(self, ctx, error: commands.CommandError):
        print(f"{error} with type {type(error)}")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("You must mention someone to target them")
            return

    @commands.command()
    @commands.guild_only()
    @commands.has_role("Fella")
    async def ping(self, ctx:commands.Context, member:Member, *, reason:str=None):    # PING COMMAND
        await ctx.send(f"{member.mention} Heres 5 pings!")
        await ctx.send(f"{member.mention} Heres 5 pings!")
        await ctx.send(f"{member.mention} Heres 5 pings!")
        await ctx.send(f"{member.mention} Heres 5 pings!")
        await ctx.send(f"{member.mention} Heres 5 pings!")
        return

    @ping.error    # PING VALIDATION
    async def ping_err(self, ctx, error: commands.CommandError):
        if isinstance(error, commands.MissingRole):
            await ctx.reply("You are missing the role to ping people!")
            return
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Please mention a player to target!")
            return

def setup(bot):
    bot.add_cog(FunCog(bot))