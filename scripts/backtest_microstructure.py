import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from pathlib import Path

RESULTS_DIR = Path(r"D:\Quant_Research_Library\papers\P13_Market_Microstructure\backtest_results")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

def simulate_microstructure_alpha(ticker="RELIANCE.NS"):
    print(f"Fetching data for {ticker}...")
    data = yf.download(ticker, period="1mo", interval="5m")
    if data.empty: return None
    data['OFI'] = (data['Close'] - data['Open']) * data['Volume']
    data['OFI_Signal'] = data['OFI'].rolling(window=5).mean()
    data['Hawkes_Intensity'] = data['OFI'].rolling(window=10).std()
    data['Returns'] = data['Close'].pct_change()
    data['Signal'] = -np.sign(data['OFI_Signal']) * (data['Hawkes_Intensity'] / (data['Hawkes_Intensity'].mean() + 1e-9))
    data['Strategy_Returns'] = data['Signal'].shift(1) * data['Returns']
    sharpe = (data['Strategy_Returns'].mean() / (data['Strategy_Returns'].std() + 1e-9)) * np.sqrt(252 * 78)
    print(f"Metrics for {ticker}: Sharpe={sharpe:.2f}")
    plt.figure(figsize=(10, 5))
    plt.plot((1 + data['Strategy_Returns'].fillna(0)).cumprod())
    plt.title(f"P13: {ticker}")
    plt.savefig(RESULTS_DIR / f"{ticker}_equity_curve.png")
    plt.close()
    return sharpe

if __name__ == "__main__":
    simulate_microstructure_alpha("RELIANCE.NS")
    simulate_microstructure_alpha("HDFCBANK.NS")
