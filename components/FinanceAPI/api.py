import requests
from bs4 import BeautifulSoup

def FinanceMarketIndicesAPI(indecLocation):
    MarketIndicesResults = []
    if indecLocation == "America":
        getFinanceData = requests.get("https://www.google.com/finance/markets/indexes/americas")
    elif indecLocation == "AsiaPacific":
        getFinanceData = requests.get("https://www.google.com/finance/markets/indexes/asia-pacific")
    appFinanceSource = BeautifulSoup(getFinanceData.content,"lxml")

    indeces = appFinanceSource.find_all("ul", attrs={"class": "sbnBtf"})

    for items_indeces in indeces:
        items = items_indeces.find_all("li")
        for item_indec in items:
            indec_name = item_indec.find("div", attrs={"class": "Q8lakc W9Vc1e"}).text
            indec_value = item_indec.find("div", attrs={"class": "YMlKec"}).text
            MarketIndicesResults.append(indec_name+" = "+indec_value)
    functionResult = "\n\n".join(MarketIndicesResults)
    return functionResult

def FinanceMostActiveStockAPI():
    MostActiveStocksResults = []
    getFinancedata = requests.get("https://www.google.com/finance/markets/most-active")
    appFinanceSource = BeautifulSoup(getFinancedata.content,"lxml")

    mostActiveStocks = appFinanceSource.find_all("ul", attrs={"class": "sbnBtf"})

    for itemMostActiveStock in mostActiveStocks:
        items = itemMostActiveStock.find_all("li")
        for item_mostActiveStock in items:
            mostActiveStock_name = item_mostActiveStock.find("div", attrs={"class": "Q8lakc W9Vc1e"}).text
            mostActiveStock_value = item_mostActiveStock.find("div", attrs={"class": "YMlKec"}).text
            MostActiveStocksResults.append(mostActiveStock_name+" = "+mostActiveStock_value)
    functionResult = "\n\n".join(MostActiveStocksResults)
    return functionResult

def FinanceGainersAPI():
    GainersResults = []
    getFinancedata = requests.get("https://www.google.com/finance/markets/gainers")
    appFinanceSource = BeautifulSoup(getFinancedata.content,"lxml")

    gainers = appFinanceSource.find_all("ul", attrs={"class": "sbnBtf"})

    for itemGainers in gainers:
        items = itemGainers.find_all("li")
        for item_gainer in items:
            financegainer_name = item_gainer.find("div", attrs={"class": "Q8lakc W9Vc1e"}).text
            financeGainer_value = item_gainer.find("div", attrs={"class": "YMlKec"}).text
            GainersResults.append(financegainer_name+" = "+financeGainer_value)
    functionResult = "\n\n".join(GainersResults)
    return functionResult

def FinanceLosersAPI():
    LosersResults = []
    getFinancedata = requests.get("https://www.google.com/finance/markets/losers")
    appFinanceSource = BeautifulSoup(getFinancedata.content,"lxml")

    losers = appFinanceSource.find_all("ul", attrs={"class": "sbnBtf"})

    for itemLosers in losers:
        items = itemLosers.find_all("li")
        for item_loser in items:
            financeLoser_name = item_loser.find("div", attrs={"class": "Q8lakc W9Vc1e"}).text
            financeLoser_value = item_loser.find("div", attrs={"class": "YMlKec"}).text
            LosersResults.append(financeLoser_name+" = "+financeLoser_value)
    functionResult = "\n\n".join(LosersResults)
    return functionResult         

def FinanceCryptoAPI():
    CryptoCurrenciesResults = []
    getFinancedata = requests.get("https://www.google.com/finance/markets/cryptocurrencies")
    appFinanceSource = BeautifulSoup(getFinancedata.content,"lxml")

    cryptoCurrencies = appFinanceSource.find_all("ul", attrs={"class": "sbnBtf"})

    for itemCryptocurrencies in cryptoCurrencies:
        items = itemCryptocurrencies.find_all("li")
        for item_cryptocurrencie in items:
            financeCryptocurrencie_name = item_cryptocurrencie.find("div", attrs={"class": "Q8lakc W9Vc1e"}).text
            financeCryptocurrencie_value = item_cryptocurrencie.find("div", attrs={"class": "YMlKec"}).text
            CryptoCurrenciesResults.append(financeCryptocurrencie_name+" = "+financeCryptocurrencie_value)
    functionResult = "\n\n".join(CryptoCurrenciesResults)
    return functionResult
