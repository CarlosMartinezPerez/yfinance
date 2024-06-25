import yfinance as yf

def carregar_dados(ticker):
    df = yf.Ticker(ticker).history("1y")
    df.reset_index(inplace=True)
    df[ticker] = ticker.split(".")[0]
    return df


petrobras = carregar_dados("PETR4.SA")
bb = carregar_dados("BBAS3.SA")
vale = carregar_dados("VALE3.SA")

petrobras.tail()
vale.head()
bb.head()
