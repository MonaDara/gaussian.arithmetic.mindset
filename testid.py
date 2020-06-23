import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import tushare as ts
import pandas_datareader.data as web
from scipy import stats
import numpy as np
import matplotlib
import statsmodels.api as sm
from datetime import datetime
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas_datareader.data as web
from lmfit.models import LinearModel, StepModel
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
from statsmodels.tsa.stattools import adfuller as ADF
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from pandas import Series
from statsmodels.tsa.stattools import adfuller
from pandas import Series 
import openpyxl
 
# 0's in binary representation of a number 

df = pd.read_csv('C:/Users/Monica/Documents/Monica Files/report/workspace/Python/ID/ID00.csv', parse_dates= True)
style.use('ggplot')
df.head()
print(df.describe)
print(df[['A']])

series =pd.Series(df['A'])

result = series.nonzero()

print("result:",result)

values = series.iloc[result]

idx = 0
print(values.to_frame)
arr1 = result[1:3]
print (arr1)
list2 = [0,1,2,3]

wb = openpyxl.Workbook()
sheet = wb.active

##new_col = values[:,0]
##new_col
##vlaues.insert(loc=idx, column='count', value=new_col)
