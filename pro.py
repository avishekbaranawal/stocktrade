import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
ongc_df = yf.download('TSLA',start='2022-01-01',end='2022-05-01',progress=False)
ongc_df.head()