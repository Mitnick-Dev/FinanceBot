from telegram import Update
from telegram.ext import ContextTypes
from components.FinanceAPI.api import FinanceCryptoAPI, FinanceGainersAPI, FinanceLosersAPI, FinanceMarketIndicesAPI, FinanceMostActiveStockAPI

async def AmericaMarketIndices(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(FinanceMarketIndicesAPI("America"))
      
async def AsiaPacificMarketIndices(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(FinanceMarketIndicesAPI("AsiaPacific"))

async def Crypto(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(FinanceCryptoAPI())

async def Gainers(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(FinanceGainersAPI())

async def Losers(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(FinanceLosersAPI())    

async def MarketIndices(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reponseTitle = "Lütfen görüntülemek istedğiniz piyasa endekslerinin lokasyonunu seçiniz.\n"
    brace = "-------------------------------------------------------------------------------\n"
    await update.message.reply_text(reponseTitle+brace+"Amerika: /AmericaMarketIndices\nAsya Pasifik: /AsiaPacificMarketIndices")

async def MostActive(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(FinanceMostActiveStockAPI())      
