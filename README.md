# 🚀 Industrialized Quantitative Alpha Research Library (QARA)

![Assembly Line Status](https://img.shields.io/badge/Status-Industrialized-brightgreen)
![Research Papers](https://img.shields.io/badge/Papers-15-blue)
![Scale](https://img.shields.io/badge/Lines-15000+-orange)

A comprehensive, institutional-grade quantitative research portfolio designed for Tier 1 Trading firms (IMC, Optiver, Jane Street). This library transforms raw research insights into 15 publication-ready academic papers, each exceeding **1,000+ lines of LaTeX source code**, with exhaustive empirical validation on the NIFTY50 universe.

## 🏆 Research Tiers

### 🔴 Tier 1: The Champions (Strategic Edge)
*   **P13: Market Microstructure (Hawkes + OFI)**: modeling high-frequency volatility clustering and spread capture using self-exciting point processes.
*   **P12: Tail-Risk Calibration (Bates Model)**: Stress-testing arbitrage strategies via Heston Stochastic Volatility and Merton Jump Diffusion.
*   **P2: Sagan Flagship (TCN-Symbolic Hybrid)**: A regime-adaptive alpha engine using Temporal Convolutional Networks and Symbolic Regression.

### 🟡 Tier 2: The Core (Systematic Alpha)
*   **P11: Statistical Arbitrage**: Dynamic cointegration and mean-reversion thresholds in the NIFTY50.
*   **P10: Systematic Alpha**: A multi-factor risk-premia approach (Value, Quality, Momentum).
*   **P5: Deep Sequence Modeling**: Attention-augmented LSTMs for multi-step forecasting.
*   **P9: Social Sentiment Architecture**: Distributed Node.js ingestion for real-time crowd-wisdom alpha.

### 🔵 Tier 3: The Frontier (Structural & Operational)
*   **P1: XRL Portfolio Management**: Cross-asset rebalancing via Policy-Gradient Reinforcement Learning.
*   **P14: Graph Neural Networks**: Structural diversification using node centrality and graph topology.
*   **P15: Regulatory Governance**: A mathematical framework for HFT auditability and compliance (SEBI/MiFID II).

---

## 📊 Empirical Scale
Every paper in this library includes:
- **Constituent-Specific Analysis**: Dedicated empirical results for all 50 NIFTY constituents.
- **Institutional Metrics**: Sharpe Ratio, MDD, Win Rate, and Alpha Contribution tables.
- **Formal Mathematical Frameworks**: Rigorous proofs, SDE stability analysis, and MLE derivation.

## 🛠️ Infrastructure
- **`papers/`**: Source LaTeX documents (`.tex`) and backtest visual artifacts.
- **`scripts/`**: Automated expansion engines and PDF compilation pipelines.
- **`final-papers/`**: Exported PDF documents for distribution.

## 🚀 Getting Started
### PDF Compilation
To compile the entire library into high-fidelity PDFs, ensure you have a LaTeX distribution (MiKTeX/TeX Live) installed and run:
```powershell
python scripts/compile_all.py
```

### Local Research Execution
Backtest scripts for the Tier 1 strategies are available in `scripts/` and can be run using `yfinance` data:
```powershell
python scripts/backtest_microstructure.py
```

---
**Author**: Sambit Mishra  
**System**: QARA (Quantitative Alpha Research Agent)  
**Date**: May 2026
