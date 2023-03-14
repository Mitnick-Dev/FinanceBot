from components.botHandler import *
from components.eventHandler import *
from telegram.ext import ApplicationBuilder, CommandHandler

def setup():
    with open("components/token.txt", "r") as f:
        TOKEN = f.read()

    appBot = ApplicationBuilder().token(TOKEN).build()

    appBot.add_handler(CommandHandler("start", start))
    appBot.add_handler(CommandHandler("options", options))
    appBot.add_handler(CommandHandler("Crypto", Crypto))
    appBot.add_handler(CommandHandler("Gainers", Gainers))
    appBot.add_handler(CommandHandler("Losers", Losers))
    appBot.add_handler(CommandHandler("MarketIndices", MarketIndices))
    appBot.add_handler(CommandHandler("MostActive", MostActive))
    appBot.add_handler(CommandHandler("AmericaMarketIndices", AmericaMarketIndices))
    appBot.add_handler(CommandHandler("AmericaMarketIndices", AsiaPacificMarketIndices))
    appBot.run_polling()