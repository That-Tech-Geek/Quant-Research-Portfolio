import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Setup directories
RESULTS_DIR = Path(r"D:\Quant_Research_Library\papers\P12_Tail_Risk\backtest_results")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

def simulate_bates_stress_test():
    # Parameters
    S0 = 100
    r = 0.05
    T = 1/252 # 1 day
    steps = 100
    dt = T / steps
    
    # Bates Parameters
    kappa = 2.5
    theta = 0.04
    sigma_v = 0.3
    rho = -0.7
    v0 = 0.04
    
    # Jump Parameters
    lambda_j = 0.1 # 10% chance of jump per day
    mu_j = -0.1   # -10% jump mean
    sigma_j = 0.05
    
    # Simulation
    np.random.seed(42)
    St = np.zeros(steps)
    vt = np.zeros(steps)
    St[0] = S0
    vt[0] = v0
    
    for t in range(1, steps):
        dw_s = np.random.normal(0, np.sqrt(dt))
        dw_v = rho * dw_s + np.sqrt(1 - rho**2) * np.random.normal(0, np.sqrt(dt))
        
        # Variance process (Heston)
        vt[t] = vt[t-1] + kappa * (theta - vt[t-1]) * dt + sigma_v * np.sqrt(max(0, vt[t-1])) * dw_v
        
        # Jump process (Merton)
        jump = 0
        if np.random.random() < lambda_j * dt:
            jump = np.exp(np.random.normal(mu_j, sigma_j)) - 1
            
        # Price process
        St[t] = St[t-1] * np.exp((r - 0.5 * vt[t-1]) * dt + np.sqrt(vt[t-1]) * dw_s) * (1 + jump)
        
    # Plotting
    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax1.plot(St, color='tab:blue', label="Asset Price (S_t)")
    ax1.set_ylabel('Price', color='tab:blue')
    
    ax2 = ax1.twinx()
    ax2.plot(vt, color='tab:red', linestyle='--', label="Stochastic Volatility (v_t)")
    ax2.set_ylabel('Variance', color='tab:red')
    
    plt.title("P12 Bates Model Stress Test: Price Discontinuity (Jump) and Volatility Clustering")
    fig.tight_layout()
    
    plot_path = RESULTS_DIR / "bates_stress_test.png"
    plt.savefig(plot_path)
    print(f"Saved plot to {plot_path}")

if __name__ == "__main__":
    simulate_bates_stress_test()
