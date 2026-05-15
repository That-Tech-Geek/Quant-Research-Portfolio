import numpy as np
import pandas as pd
import logging
from typing import Dict, Any, List, Optional
from dataclasses import dataclass

@dataclass
class BacktestConfig:
    initial_capital: float = 1_000_000.0
    commission_bps: float = 15.0
    slippage_bps: float = 2.0
    risk_free_rate: float = 0.065
    annualization_factor: int = 252

class BacktestEngine:
    """
    QARA Core Vectorized Backtesting Engine.
    Enforces point-in-time signal alignment and realistic cost modeling.
    """
    def __init__(self, config: BacktestConfig = BacktestConfig()):
        self.config = config
        self.logger = logging.getLogger("QARA.BacktestEngine")
        
    def run(self, returns: pd.Series, signals: pd.Series) -> Dict[str, Any]:
        """
        Runs a vectorized backtest.
        signals: Position weights (sum can exceed 1 for leverage, or -1 for short).
        returns: Daily asset returns (log returns preferred).
        """
        # Ensure point-in-time safety: signals must be shifted by 1 day
        # so that trade on day t is based on information from day t-1.
        safe_signals = signals.shift(1).fillna(0)
        
        # Calculate gross returns
        portfolio_returns = safe_signals * returns
        
        # Calculate turnover and transaction costs
        turnover = safe_signals.diff().abs().fillna(0)
        total_costs = (self.config.commission_bps / 10000.0) * turnover
        
        # Net returns
        net_returns = portfolio_returns - total_costs
        
        # Cumulative returns
        cum_returns = (1 + net_returns).cumprod()
        
        return self._calculate_metrics(net_returns, cum_returns)

    def _calculate_metrics(self, net_returns: pd.Series, cum_returns: pd.Series) -> Dict[str, Any]:
        """
        PhD-level performance metrics calculation.
        """
        avg_ret = net_returns.mean() * self.config.annualization_factor
        vol = net_returns.std() * np.sqrt(self.config.annualization_factor)
        
        sharpe = (avg_ret - self.config.risk_free_rate) / (vol + 1e-9)
        
        # Drawdown analysis
        running_max = cum_returns.cummax()
        drawdown = (cum_returns / running_max) - 1
        max_dd = drawdown.min()
        
        # Sortino Ratio
        downside_returns = net_returns[net_returns < 0]
        downside_vol = downside_returns.std() * np.sqrt(self.config.annualization_factor)
        sortino = (avg_ret - self.config.risk_free_rate) / (downside_vol + 1e-9)
        
        # Calmar Ratio
        calmar = avg_ret / (abs(max_dd) + 1e-9)
        
        return {
            "total_return": float(cum_returns.iloc[-1] - 1),
            "annualized_return": float(avg_ret),
            "annualized_vol": float(vol),
            "sharpe_ratio": float(sharpe),
            "sortino_ratio": float(sortino),
            "calmar_ratio": float(calmar),
            "max_drawdown": float(max_dd),
            "equity_curve": cum_returns.to_dict(),
            "drawdown_curve": drawdown.to_dict()
        }
