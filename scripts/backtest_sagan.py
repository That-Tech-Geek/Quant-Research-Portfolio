import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

RESULTS_DIR = Path(r"D:\Quant_Research_Library\papers\P2_Sagan_Ensemble\backtest_results")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

def simulate_sagan_flagship(ticker="RELIANCE.NS"):
    print(f"Fetching data for {ticker} (Sagan Engine Proxy)...")
    df = yf.download(ticker, period="2y", interval="1d")
    if df.empty: return
    data = df['Close']
    
    # Sagan Strategy: 20/50 MA Crossover
    sma20 = data.rolling(window=20).mean()
    sma50 = data.rolling(window=50).mean()
    
    signal = (sma20 > sma50).astype(int)
    returns = data.pct_change()
    strategy_returns = signal.shift(1) * returns
    
    cum_strategy = (1 + strategy_returns.fillna(0)).cumprod()
    
    # Extracting scalar values for printing
    avg_ret = strategy_returns.mean()
    std_ret = strategy_returns.std()
    sharpe_val = (avg_ret / (std_ret + 1e-9)) * np.sqrt(252)
    mdd_val = (cum_strategy / (cum_strategy.cummax() + 1e-9) - 1).min()
    
    print(f"Metrics for Sagan Strategy: Sharpe={float(sharpe_val):.2f}, MDD={float(mdd_val)*100:.1f}%")
    plt.figure(figsize=(10, 5))
    plt.plot(cum_strategy)
    plt.title(f"P2 Sagan Engine: {ticker} (MA Crossover Proxy)")
    plt.savefig(RESULTS_DIR / "sagan_equity_curve.png")
    plt.close()

if __name__ == "__main__":
    simulate_sagan_flagship()
