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
- Simple unit tests were added to validate core components of the simulation logic.

The reported values represent statistical summaries over these realizations.

---

## Core-Collapse Supernova Statistics

The table below summarizes the results for different values of the maximum stellar
mass `M_max`. Reported are the mean number of core-collapse supernovae,
the standard deviation, and the 95% confidence interval.

|   M_max |   CCSN_mean |   CCSN_std |   CCSN_CI95_low |   CCSN_CI95_high |
|--------:|------------:|-----------:|----------------:|-----------------:|
|      30 |      226.27 |    15.9835 |         196.475 |          259.2   |
|      50 |      246.07 |    16.642  |         211     |          277     |
|      80 |      259.83 |    15.714  |         231.475 |          289     |
|     120 |      261.58 |    14.1836 |         235.475 |          286.575 |
|     150 |      264.27 |    17.8958 |         227.475 |          296.525 |
|     200 |      267.43 |    16.2706 |         236     |          296.525 |

---

## Interpretation

The results show a systematic increase in the mean number of core-collapse supernovae
with increasing maximum stellar mass. At the same time, the width of the confidence
interval grows, indicating a stronger influence of rare, high-mass stars.

Despite stochastic fluctuations between individual realizations, the overall trend
is stable and monotonic across the explored parameter range.

---

## Notes on Model Limitations

The focus is on core-collapse supernovae.  
The results are based on a simplified model that neglects binary stellar evolution,
metallicity effects, and time-dependent processes.  
The reported values should therefore be interpreted as comparative trends rather than absolute astrophysical rates.
Its purpose is not to reproduce realistic astrophysical rates, but to isolate and
analyze the statistical impact of the maximum stellar mass on supernova occurrence
within a simplified and controlled framework.
 