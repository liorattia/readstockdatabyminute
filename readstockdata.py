# https://www.youtube.com/watch?v=JJO9fKj3_u4

import pandas as pd
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries

import matplotlib.pyplot as plt

api_key = '9AOUY0Z1K2ZZT93C'

ts = TimeSeries(key = api_key, output_format = 'pandas')
data_ts, meta_data_ts = ts.get_intraday(symbol = 'GOOG' , interval = '1min', outputsize = 'full' )

periods = 60 

ti = TechIndicators(key=api_key,output_format='pandas')

data_ti, meta_data_ti = ti.get_sma(symbol='GOOG',interval='1min',time_period=periods,series_type='Close')

print(data_ts)

df1 = data_ti
df2 = data_ts['4. close'].iloc[periods-1::]

df2.index = df1.index
total_df = pd.concat([df1,df2],axis = 1)

# print (total_df)

total_df.plot()
plt.show()