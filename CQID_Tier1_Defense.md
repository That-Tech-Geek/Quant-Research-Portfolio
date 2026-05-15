# CQID Tier 1 Defense: Adversarial Question Bank

This document contains 60 adversarial questions (20 per paper) designed to simulate a high-pressure technical interview at IMC Trading for the Tier 1 research papers.

---

## 📈 P13: Market Microstructure (Hawkes + OFI)
*Focus: Market Making, Order Book Dynamics, Self-Excitation*

1. **Kyle's Lambda**: "How do you distinguish between temporary price impact (liquidity provision) and permanent price impact (informed trading) in your $\lambda$ estimate?"
2. **Hawkes Overfitting**: "With an exponential kernel $\alpha e^{-\beta t}$, how do you ensure $\beta$ isn't just capturing the periodicity of your data source rather than true self-excitation?"
3. **Inventory Skew**: "In your Avellaneda-Stoikov implementation, how do you determine the risk aversion parameter $\gamma$? Is it static or regime-dependent?"
4. **Adverse Selection**: "If your Hawkes intensity spikes, how does your model prevent 'getting picked off' by informed traders who are causing the excitement?"
5. **Tick Test Accuracy**: "The Lee-Ready tick test is notoriously inaccurate in high-frequency environments. Have you benchmarked it against actual trade-side data?"
6. **Latent Liquidity**: "Your OFI ignores the 'hidden' depth at levels beyond the best bid/ask. How does this impact your market depth $\lambda$?"
7. **Branching Ratio**: "If $n \to 1$, your system predicts a crash. How do you handle the high rate of false positives in this critical state?"
8. **Transaction Costs**: "You claim alpha after costs. Are you using a flat fee or a multi-tiered exchange fee model (Maker/Taker rebate)?"
9. **Kernel Selection**: "Why use an exponential kernel? Would a power-law kernel (Fat-tailed) better capture long-range volatility clustering?"
10. **Mid-Price Drift**: "In your mid-price adjustment $r(s, t)$, how do you handle cases where the equilibrium price drifts significantly beyond your inventory limit?"
11. **Feature Leakage**: "Is there any look-ahead bias in your rolling Z-score for OFI?"
12. **Cross-Asset Impact**: "Does the Hawkes intensity of a correlated asset (e.g., NIFTY Futures) inform your equity market making quotes?"
13. **Model Latency**: "What is the computational overhead of solving the Hawkes log-likelihood in real-time?"
14. **Spread Capture**: "What percentage of your PnL comes from the spread vs. directional OFI prediction?"
15. **Inventory Decay**: "Does your model aggressively dump inventory at the end of the day, or do you carry risk overnight?"
16. **Regime Switching**: "How do you define the transition threshold between 'Trending' and 'Mean-Reverting' intensity?"
17. **Order Size**: "Does your OFI weight large institutional 'blocks' differently than small retail trades?"
18. **VIX Interaction**: "How does the global VIX level scale your background arrival rate $\mu$?"
19. **Numerical Stability**: "How do you prevent the intensity $\lambda(t)$ from exploding during a flash crash scenario?"
20. **Practicality**: "If IMC's hardware latency is 5$\mu$s, can your Hawkes model run fast enough to be useful?"

---

## 🌪️ P12: Tail-Risk-Bates (Heston + Merton Jumps)
*Focus: Volatility Modeling, Jump Diffusion, Numerical Methods*

21. **FFT Complexity**: "Why use the Carr-Madan FFT approach instead of a simpler Monte Carlo simulation for pricing?"
22. **Jump Intensity**: "How do you calibrate the Poisson intensity $\lambda$ during period of low volume where jumps are rare but high-impact?"
23. **Feller Condition**: "Does your Heston parameter set satisfy $2\kappa\theta > \sigma^2$? If not, how do you handle the variance reaching zero?"
24. **Volatility Smile**: "Can your Bates model reproduce the steep 'smirk' observed in NIFTY OTM puts better than a standard SABR model?"
25. **Correlation ($\rho$)**: "Your Brownian motions are correlated. How does the leverage effect ($\rho < 0$) impact your jump size distribution?"
26. **Damping Factor**: "In your FFT pricing formula, how did you choose the damping factor $\alpha$? Is your result sensitive to this choice?"
27. **Model Calibration**: "How often do you re-calibrate the Bates parameters? Does the model 'break' during sudden regime shifts?"
28. **Jump Size ($k$)**: "You assume log-normal jump sizes. Is this consistent with the empirical 'fat tails' of the Indian market?"
29. **Mean Reversion ($\kappa$)**: "Is the speed of mean reversion $\kappa$ constant across different volatility regimes?"
30. **Hedge Ratios**: "How do the 'Greeks' in a Bates model differ from Black-Scholes? How does the jump component affect your Delta hedge?"
31. **Numerical Stability**: "Does your FFT integral converge for deep OTM options?"
32. **Path Dependency**: "The Bates model is a point-in-time pricer. How do you use it to manage path-dependent risks like barrier breaches?"
33. **Volatility Clustering**: "Does the Heston component capture the persistence of volatility seen in your Hawkes microstructure research?"
34. **Parameter Identification**: "How do you distinguish between a high $\sigma$ (vol of vol) and a high $\lambda$ (jump frequency) during calibration?"
35. **Alternative Models**: "Why not use a Rough Volatility model (e.g., rBergomi) which better captures the fractal nature of volatility?"
36. **Risk-Neutral vs Real-World**: "How do you transition from the risk-neutral measure used for pricing to the physical measure needed for backtesting?"
37. **Liquidity Premium**: "Does your model account for the wider spreads in OTM options during stress events?"
38. **Bermudan/American Features**: "Can your FFT approach handle the early exercise features of American-style options?"
39. **Calibration Loss**: "Are you using MSE or a weighted IV-space loss function for calibration?"
40. **Market Context**: "How did the model perform during the 2024 election-day volatility spike in India?"

---

## 🛰️ P2: Sagan-Flagship (2.43 Sharpe)
*Focus: Symbolic Regression, TCN, Hybrid Architectures*

41. **Symbolic Rationale**: "Explain 'Symbolic Residuals' as if I'm a portfolio manager, not a data scientist. Why should I trust a genetic algorithm's formula?"
42. **Overfitting**: "Genetic programming is notorious for finding spurious correlations. How do you penalize formula complexity (Occam's Razor)?"
43. **TCN vs LSTM**: "Why use a Temporal Convolutional Network? What does the dilated convolution provide that an LSTM with Attention doesn't?"
44. **Downside Convexity**: "Your exposure $\Psi_t$ scales exponentially. In a 'gap-down' open, doesn't this lead to massive slippage that your backtest ignores?"
45. **Stationarity**: "You claim the residuals are stationary. Did you perform an Augmented Dickey-Fuller (ADF) test on the symbolic output?"
46. **Feature Importance**: "Which features does the symbolic engine consistently select? Is it just picking up on the VIX-Price correlation?"
47. **Lookahead Bias**: "Is your 'rolling k-day window' for centering truly causal? Is there any information leakage from $t+1$?"
48. **Semi-Variance**: "Why use semi-variance instead of standard deviation for your risk scaling? Does it actually improve the Sortino ratio?"
49. **Formula Stability**: "If I change the training window by one day, does the symbolic formula completely change? How stable is the 'Discovery'?"
50. **Harmonic Terms**: "Your formulas use Sine/Cosine. Are you claiming the market has fixed-frequency cycles? Isn't that a dangerous assumption?"
51. **TCN Receptive Field**: "What is the effective lookback of your TCN? Is it long enough to capture macro cycles?"
52. **Execution Slippage**: "A 2.43 Sharpe is very high. What's the 'capacity' of this strategy before market impact eats all the alpha?"
53. **Dimensional Consistency**: "Does your symbolic engine ensure the units make sense? (e.g., adding Price to Volume?)"
54. **Model Ensemble**: "How do you combine the TCN 'Black-Box' prediction with the Symbolic 'White-Box' formula without double-counting the signal?"
55. **Market Neutrality**: "Is the strategy truly market-neutral, or is it just a very smart 'Long-Bias' momentum play?"
56. **Pathological Cases**: "When does the Sagan engine fail? (e.g., low-volatility grinding markets?)"
57. **Computation Time**: "How long does it take to 'discover' a new formula? Is this a daily or intraday process?"
58. **Transferability**: "Does a formula discovered on RELIANCE work on TCS, or is it stock-specific?"
59. **Backtest Hardening**: "Did you run a 'Randomize Returns' test to see if your result is statistically significant?"
60. **The 'Why'**: "If you had to pick one reason why this strategy beats the NIFTY50, what is the fundamental economic reason?"
