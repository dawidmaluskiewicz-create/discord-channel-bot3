import os
from discord.ext import commands
from dotenv import load_dotenv

# Załaduj token z pliku .env
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Ustawienia bota
intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Lista dozwolonych kanałów (możesz dodać więcej ID)
ALLOWED_CHANNELS = [1408714685770895402]  # <- wstaw ID kanałów

# Event po włączeniu bota
@bot.event
async def on_ready():
    print(f"Bot zalogowany jako {bot.user}")

# Komenda szukania kanałów
@bot.command()
async def szukaj(ctx, *, fraza: str):
    if ctx.channel.id not in ALLOWED_CHANNELS:
        await ctx.send("❌ Ta komenda działa tylko w określonych kanałach!")
        return

    guild = ctx.guild
    znalezione = []

    for channel in guild.channels:
        if fraza.lower() in channel.name.lower():
            znalezione.append(channel)

    if znalezione:
        odpowiedz = "🔎 Znalazłem kanały:\n"
        odpowiedz += "\n".join([f"#{c.name} (ID: {c.id})" for c in znalezione])
    else:
        odpowiedz = "❌ Nie znalazłem kanałów."

    await ctx.send(odpowiedz)

# Uruchomienie bota
bot.run(TOKEN)