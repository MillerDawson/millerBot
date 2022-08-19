import nextcord
import os
from nextcord.ext import commands
from nextcord import Intents


bot = commands.Bot(command_prefix=commands.when_mentioned_or("!!"), case_insensitive=True, intents=Intents.all())

def validation(authorID):
    return authorID == 167749988254744576 or authorID == 320956134343180290
    
# Upon bot running
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id}")

    for fn in os.listdir("./cogs"):
        if fn.endswith(".py"):
            bot.load_extension(f"cogs.{fn[:-3]}")
            print(f"Loaded cogs.{fn[:-3]}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.reply("Your command has not been found, type !!help")

@bot.command()  # FUTURE MAKE THESE ADMIN ONLY, FOR NOW DOESNT REALLY MATTER
async def load(ctx, extension):
    authorID = ctx.message.author.id
    if validation(authorID):
        print(f"loading {extension}")
        bot.load_extension(f"cogs.{extension}")
        print("done")
        await ctx.send(f"Loaded {extension}!")
    else:
        await ctx.reply("You dont have permission to do this!")

@load.error # LOAD VALIDATION
async def load_err(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.reply("That is already loaded!")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("You must add the name of the module you would like to load")

@bot.command()
async def reload(ctx, extension):
    authorID = ctx.message.author.id
    if validation(authorID):
        print(f"reloading {extension}")
        bot.reload_extension(f"cogs.{extension}")
        print("done")
        await ctx.send(f"Reloaded {extension}!")
    else:
        await ctx.reply("You dont have permission to do this! (Fuck off)")

@reload.error # RELOAD VALIDATION
async def reload_err(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("You must add the name of the module you would like to reload")

@bot.command()
async def unload(ctx, extension):
    authorID = ctx.message.author.id
    if validation(authorID):
        print(f"unloading {extension}")
        bot.unload_extension(f"cogs.{extension}")
        print("done")
        await ctx.send(f"Unloaded {extension}!")
    else:
        await ctx.reply("You dont have permission to do this!")

@unload.error # UNLOAD VALIDATION
async def unload_err(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.reply("That module is already unloaded!")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("You must add the name of the module you would like to unload")

bot.run(os.getenv('KEY'))