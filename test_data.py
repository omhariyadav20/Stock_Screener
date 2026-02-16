import pandas as pd
from data import compute_technicals, compute_rsi

dates = pd.date_range(end=pd.Timestamp.today(), periods=30)
df = pd.DataFrame({'Close': range(100, 130)}, index=dates)

print('RSI length:', len(compute_rsi(df['Close'])))
print('Technicals:', compute_technicals(df))
