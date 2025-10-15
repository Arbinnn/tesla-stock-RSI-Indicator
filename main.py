import pandas as pd
import pandas_datareader as web
import datetime as dt
import matplotlib.pyplot as plt
import yfinance as yf

ticker = 'TSLA'
start = dt.datetime(2025, 1, 1)
end = dt.datetime.now()

data = yf.download(ticker, start=start, end=end)

delta = data['Close'].diff(1)
delta.dropna(inplace=True)

pos=delta.copy()
neg=delta.copy()

pos[pos<0]=0
neg[neg>0]=0

days=14

avg_gain = pos.rolling(window=days).mean()
avg_loss= abs(neg.rolling(window=days).mean())

relative_strength = avg_gain / avg_loss
RSI = 100.0 - (100.0 / (1.0 + relative_strength))

combined = pd.DataFrame()
combined['RSI'] = RSI
combined['Close'] = data['Close']

plt.figure(figsize = (12,8))
axl= plt.subplot(211)
axl.plot(combined.index, combined['Close'], color='lightblue')
axl.set_title("Adjusted Close price", color='white')

axl.grid(True, color='#555555')
axl.set_axisbelow(True)
axl.set_facecolor('black')
axl.figure.set_facecolor('black')
axl.tick_params(axis='x', colors='white')
axl.tick_params(axis='y', colors='white')

ax2=plt.subplot(212, sharex=axl)
ax2.plot(combined.index, combined['RSI'], color='lightblue')
ax2.axhline(0, linestyle='--', color='#ff0000', alpha=0.5)
ax2.axhline(10, linestyle='--', color='#ffaa00', alpha=0.5)
ax2.axhline(20, linestyle='--', color='#00ff00', alpha=0.5)
ax2.axhline(30, linestyle='--', color='#cccccc', alpha=0.5)
ax2.axhline(70, linestyle='--', color='#cccccc', alpha=0.5)
ax2.axhline(80, linestyle='--', color='#00ff00', alpha=0.5)
ax2.axhline(90, linestyle='--', color='#ffaa00', alpha=0.5)
ax2.axhline(100, linestyle='--', color='#ff0000', alpha=0.5)

ax2.set_title("RSI value", color='white')
ax2.grid(False)
ax2.set_axisbelow(True)
ax2.set_facecolor('black')
ax2.figure.set_facecolor('black')
ax2.tick_params(axis='x', colors='white')
ax2.tick_params(axis='y', colors='white')



plt.show()

