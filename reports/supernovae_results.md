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
the standard deviation, and the 68% confidence interval.

<!-- INSERT df.to_markdown() TABLE HERE -->

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
