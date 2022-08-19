import nextcord
from nextcord.ext import commands
from nextcord import Intents, Member

class StaffCog(commands.Cog):    
    def __init__(self, bot):
        self.bot = bot

        
    ## BAN COMMAND
    @commands.command(name="ban", description="Ban a user")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx: commands.Context, member:Member, *, reason:str=None): # Future add so it writes in log room who ban
        if reason == None:
              reason = "No Reason Provided"
      
        await member.ban(delete_message_days=1, reason=reason)
        await ctx.reply(f"**{member.name}** has been banned!")  # future make embed
  
    @ban.error    # BAN VALIDATION
    async def ban_err(self, ctx: commands.Context, error: commands.CommandError):
        print(f"{error} with type {type(error)}")
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("You do not have the permission to ban users")
            return
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.reply("I dont have permission to ban members!")
            return
        elif isinstance(error, commands.errors.MemberNotFound):
            await ctx.reply("Member not found! Are you a fucking noob??!")
            return
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("You are missing a target mention")
            return
        else:
            await ctx.reply("User has admin permissions already! No insurrections here..")
            return
  
    ## KICK COMMAND
    @commands.command(name="kick", description="Kick a user")
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self, ctx: commands.Context, member:Member, *, reason:str=None): # Future add so it writes in log room 
        print(f"ctx {ctx} ban member: {member}, with reason: {reason}.")
        if reason == None:
            reason = "No Reason Provided"
        await member.kick(reason=reason)
        await ctx.reply(f"**{member.name}** has been kicked!")  # future make embed
  
    @kick.error    # KICK VALIDATION
    async def kick_err(self, ctx: commands.Context, error: commands.CommandError):
        print(f"{error} with type {type(error)}")
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("You do not have the permission to kick users.")
            return
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.reply("I dont have permission to kick members!")
            return
        elif isinstance(error, commands.errors.MemberNotFound):
            await ctx.reply("Member not found! Are you a fucking noob??!")
            return
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("You are missing a target mention")
            return
        else:    
            await ctx.reply("User has admin permissions already! No insurrections here..")
            return
    
def setup(bot):
    bot.add_cog(StaffCog(bot))