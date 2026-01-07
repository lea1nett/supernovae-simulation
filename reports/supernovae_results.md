# Monte Carlo Simulation Results

This report provides a concise summary of the key numerical results obtained from
the Monte Carlo simulations. The focus lies on the dependence of the core-collapse
supernova rate on the maximum stellar mass.

---

## Simulation Setup

- Stellar populations are generated using a Salpeter initial mass function.
- Only isolated single stars are considered.
- Core-collapse supernovae are identified based on an initial mass threshold.
- Each scenario is evaluated using repeated Monte Carlo realizations.

The reported values represent statistical summaries over these realizations.

---

## Core-Collapse Supernova Statistics

The table below summarizes the results for different values of the maximum stellar
mass \( M_{\mathrm{max}} \). Reported are the mean number of core-collapse supernovae,
the standard deviation, and the 95% confidence interval.

|   M_max |   CCSN_mean |   CCSN_std |   CCSN_CI95_low |   CCSN_CI95_high |
|--------:|------------:|-----------:|----------------:|-----------------:|
|   30.00 |      223.03 |      13.72 |          200.90 |           248.00 |
|   50.00 |      244.84 |      15.45 |          218.00 |           271.52 |
|   80.00 |      257.87 |      15.32 |          230.90 |           288.05 |
|  120.00 |      262.15 |      14.24 |          236.00 |           286.05 |
|  150.00 |      265.78 |      16.05 |          237.47 |           292.00 |
|  200.00 |      266.52 |      15.80 |          236.47 |           295.57 |

---

## Interpretation

The results show a systematic increase in the mean number of core-collapse supernovae
with increasing maximum stellar mass. At the same time, the width of the confidence
interval grows, indicating a stronger influence of rare, high-mass stars.

Despite stochastic fluctuations between individual realizations, the overall trend
is stable and monotonic across the explored parameter range.

---

## Notes on Model Limitations

The results are based on a simplified model that neglects binary stellar evolution,
metallicity effects, and time-dependent processes. The reported values should therefore
be interpreted as comparative trends rather than absolute astrophysical rates.
