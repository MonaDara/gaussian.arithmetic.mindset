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
 

df = pd.read_csv('C:/Users/Monica/Documents/Monica Files/report/workspace/Python/ID/ID00.csv', index_col=0)
style.use('ggplot')
df.head()
#print(df.describe)


import csv

with open("ID00.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lines in csv_reader:
      print("list:",lines)
      print("count:",lines.count('0'))
import collections
print(collections.Counter(lines))


