import discord
from discord.ext import commands

print("[+] Logado na conta Discord")

bot = commands.Bot(command_prefix="?", self_bot=True)
bot.remove_command("help")


@bot.event
async def on_ready():
    print("\n\n[=] Estou pronto. Apenas digite ?purge")
    print(f"[=] Nome: {bot.user.name}")
    print(f"[=] ID: {bot.user.id}\n\n")


@bot.command()
async def purge(ctx, limit: int = None):
    passed = 0
    failed = 0
    async for msg in ctx.message.channel.history(limit=limit):
        if msg.author.id == bot.user.id:
            try:
                await msg.delete()
                passed += 1
            except:
                failed += 1
    print(f"[+] Foram limpas {passed} mensagens com {failed} falhas")


bot.run("token aqui!",
        bot=False)
