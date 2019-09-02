import pandas as pd
import numpy as np
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame

# 01 Gen 2010
start = datetime.datetime(2010, 1, 1)
# 02 Sep 2019
end = datetime.datetime(2019, 9, 2)

df = web.DataReader("BTC-USD", 'yahoo', start, end)
df.head()

close_px = df['Adj Close']
mavg = close_px.rolling(window=100).mean()

# %matplotlib inline
import matplotlib.pyplot as plt
from matplotlib import style

# Adjusting the size of matplotlib
import matplotlib as mpl
mpl.rc('figure', figsize=(8, 7))
mpl.__version__

# Adjusting the style of matplotlib
style.use('ggplot')

# close_px.plot(label='BTC-USD')
# mavg.plot(label='mavg')
# plt.legend()

rets = close_px / close_px.shift(1) - 1
rets.plot(label='return')

