#!/usr/bin/env python
# coding: utf-8

# ## Scrapping Tesla Stock price, Technical Indicator and financial statements from AlphaVantage API

# In[201]:


# For the default integer index behavior
from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='API Key',output_format='pandas')


# In[202]:


#returns raw (as-traded) daily open/high/low/close/volume values and more covering 20 years historical data
data_daily,metadata = ts.get_daily_adjusted(symbol='TSLA',outputsize='full')


# In[203]:


#renaming raw columns

data_daily=data_daily.rename(columns={'index':'date','1. open':'open', '2. high':'high', '3. low':'low', '4. close':'close',
       '5. adjusted close':'adjusted_close', '6. volume':'volume', '7. dividend amount':'dividend',
       '8. split coefficient':'split_coefficient'})


# In[204]:


#importing technical indicator package to call for specific data related to Tesla stock price
from alpha_vantage.techindicators import TechIndicators
ti = TechIndicators(key='GFNXHWUW69O13SI7', output_format='pandas')

#returns the relative strength index (RSI) values
data_rsi, metadata= ti.get_rsi('TSLA')


# In[205]:


#returns the simple moving average (SMA) values.
data_sma, metadata= ti.get_sma('TSLA')

# returns the exponential moving average (EMA) values
data_ema, metadata=ti.get_ema('TSLA')


# In[207]:


#returns the moving average convergence / divergence (MACD) values
data_macd, metadata=ti.get_macd('TSLA')

#returns Bollinger bands (BBANDS) values
data_brands, metadata=ti.get_bbands('TSLA')


# In[208]:


# returns the commodity channel index (CCI) values
data_cci, metadata=ti.get_cci('TSLA')

#returns the stochastic oscillator (STOCH) values
data_stoch, metadata= ti.get_stoch('TSLA')


# In[215]:


#merging the technical indicators in one dataframe
data_stock=data_daily.merge(data_rsi, on='date')
data_stock=data_stock.merge(data_sma, on='date')
data_stock=data_stock.merge(data_ema, on='date')
data_stock=data_stock.merge(data_macd, on='date')
data_stock=data_stock.merge(data_brands, on='date')
data_stock=data_stock.merge(data_cci, on='date')
data_stock=data_stock.merge(data_stoch, on='date')


# In[216]:


#checking all columns merged according to their dates.
data_stock


# In[218]:


#additional fundamental data to study company financials.
from alpha_vantage.fundamentaldata import FundamentalData
fd = FundamentalData(key='GFNXHWUW69O13SI7', output_format='pandas',indexing_type='integer')

data_balancesheet, metadata= fd.get_balance_sheet_quarterly('TSLA')
data_incomestatement, metadata= fd.get_income_statement_quarterly('TSLA')


# In[219]:


#Exporting the files to local drive to later store in database
data_stock.to_csv(r'C:/Users/OneDrive/Desktop/data_stock.csv', index = True)
data_balancesheet.to_csv(r'C:/Users/OneDrive/Desktop/data_balancesheet.csv', index = False)
data_incomestatement.to_csv(r'C:/Users/OneDrive/Desktop/data_incomestatement.csv', index = False)


# ## Tesla Tweets from Twitter Using Twint Package

# In[221]:


#import necessary package to extract data with twint package
import twint
import nest_asyncio
nest_asyncio.apply()


# #### Only scrapping tweets most influencial profiles that can have an effect on the stock price

# In[222]:


# Scrap Elon Musk tweets mentioning about Tesla
c = twint.Config()
c.Username = "elonmusk"
c.Search = "tesla"
c.Store_csv=True
c.Output="C:/Users/fibnn/OneDrive/Desktop/elonmusk_tweet.csv"


# Run
twint.run.Search(c)


# In[223]:


# Scrap CNBC tweets mentioning about Tesla
c = twint.Config()
c.Username = "CNBC"
c.Search = "tesla"
c.Store_csv=True
c.Output="C:/Users/fibnn/OneDrive/Desktop/cnbc_tweet.csv"


# Run
twint.run.Search(c)


# In[224]:


# Scrap IBDinvestors tweets mentioning about Tesla
c = twint.Config()
c.Username = "IBDinvestors"
c.Search = "tesla"
c.Store_csv=True
c.Output="C:/Users/fibnn/OneDrive/Desktop/IBDinvestors_tweet.csv"


# Run
twint.run.Search(c)


# In[225]:



# Run
twint.run.Search(c)


# In[226]:


# Scrap marketwatch tweets mentioning about Tesla
c = twint.Config()
c.Username = "MarketWatch"
c.Search = "tesla"
c.Store_csv=True
c.Output="C:/Users/fibnn/OneDrive/Desktop/marketwatch_tweet.csv"


# Run
twint.run.Search(c)


# In[227]:


# Scrap steve Hank tweets mentioning about Tesla
c = twint.Config()
c.Username = "steve_hanke"
c.Search = "tesla"
c.Store_csv=True
c.Output="C:/Users/fibnn/OneDrive/Desktop/stevehank_tweet.csv"



# Run
twint.run.Search(c)

