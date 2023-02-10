import pandas as pd
import html5lib
import numpy as np

# Scrape the entire S&P500 List from wikipedia into Pandas dataframe
ticker_list = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
df = ticker_list[0]

ticker = df['Symbol'].to_list()
# Drop a few unwanted columns of database
# df.drop(columns = ['SEC filings', 'Date first added', 'Founded'], inplace = True)

# Fill out CIK codes by converting to string then adding 0s up to 10 digits
# df.CIK = df.CIK.astype(str)
# df['CIK'] = df['CIK'].str.zfill(10)
ticker_df = pd.DataFrame(ticker)
#ticker_df = df.drop(df.columns[0], axis = 1)
#print(ticker_df)
ticker_df.to_csv('spy500_tickers.csv')
