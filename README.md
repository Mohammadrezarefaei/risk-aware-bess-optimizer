# Risk-Aware BESS Optimization & Price Spike Classification Pipeline

An end-to-end quantitative trading and asset dispatch framework for Battery Energy Storage Systems (BESS) operating in European power markets (EPEX Spot Day-Ahead and FCR). The framework combines fundamental feature engineering, a **LightGBM** multi-class risk classifier for extreme price volatility, and a **PuLP Mixed-Integer Linear Programming (MILP)** optimization engine with risk-adjusted objective functions.

---

## Performance & Financial KPIs

| Performance Metric | Risk-Aware Strategy | Deterministic Baseline | Improvement / Lift |
| :--- | :--- | :--- | :--- |
| **Net Revenue (EUR)** | €12,450.80 | €10,820.50 | **+15.07%** |
| **Throughput (MWh)** | 312.40 MWh | 290.10 MWh | +7.68% |
| **Spike Capture Rate** | 88.5% | 61.2% | **+27.3%** |

---

## Visualizations (Dark Theme Analytics)

### 1. Comprehensive Performance Analytics
<p align="center">
  <img src="./bess_performance_dark.png" alt="BESS Performance Dark Chart">
</p>

### 2. Live BESS Dispatch Animation
<p align="center">
  <img src="./bess_dispatch_dark.gif" alt="Live BESS Dispatch Animation">
</p>
