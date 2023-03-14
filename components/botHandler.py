from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("CihatFinance Botuna Hoşgeldiniz.\n\nseçenekleri görmek için: /options")

async def options(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    options = "Kripto: /Crypto\nKazananlar: /Gainers\nKaybedenler: /Losers\nPiyasa Endeksleri: /MarketIndices\nEn Aktif Hisseler: /MostActive"
    await update.message.reply_text(" Seçenekler\n"+"---------------------------------\n"+options)