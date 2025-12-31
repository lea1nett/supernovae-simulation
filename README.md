# Monte Carlo Simulation of Supernova Rates

This project investigates the influence of the maximum stellar mass on supernova
rates in a stellar population using a Monte Carlo simulation approach.
Only the evolution of isolated single stars is considered.

The focus is on core-collapse supernovae. Type Ia supernovae do not occur in the model,
as binary stellar evolution is not included.

---

## Project Structure

```text
├── configs/
│
├── figures/
│
├── notebooks/
│ └── monte_carlo.ipynb
│
├── reports/
│ └── ABOUT.txt
│
├── src/
│ ├── __init__.py
│ ├── sampling.py
│ ├── mc_functions.py
│ ├── stellar_physics.py
│ └── supernovae.py
│
├── tests/
│
├── environment.yml
└── README.md
```

- `configs/` contains seeds and parameters
- NO `data/`, we do not have any data, we simply sample based on physics.
- `figures/`contains png-plots
- `notebooks/` contains the Jupyter notebook used to run the simulation and perform the analysis
- `reports/`contains short texts 
- `src/` contains all physical and stochastic model functions  
- `tests/` contains tests

---

## Physical Model

The simulation models the final evolutionary outcomes of a population of isolated
single stars. Stellar masses are sampled from a Salpeter initial mass function (IMF),
which favors the formation of low-mass stars while allowing for rare high-mass objects.

The stellar endpoint is determined solely by the initial mass of the star:

- **Low- and intermediate-mass stars**  
  Stars with initial masses below the core-collapse threshold evolve through
  the red giant and asymptotic giant branch phases and ultimately form white dwarfs.
  These stars do not produce supernova explosions in isolation.

- **Massive stars and core-collapse supernovae**  
  Stars with sufficiently high initial masses undergo successive nuclear burning
  stages up to iron. Once nuclear fusion can no longer provide pressure support,
  the stellar core collapses under gravity, leading to a core-collapse supernova
  (Type II or related subtypes). In the model, all such events are grouped together
  as core-collapse supernovae.

- **Type Ia supernovae**  
  Type Ia supernovae originate from thermonuclear explosions of white dwarfs in
  binary systems, typically through mass accretion or mergers. Since binary stellar
  evolution is not included in this model, Type Ia supernovae do not occur in the
  simulation.

The model neglects metallicity effects, rotation, mass loss, and binary interactions.
Its purpose is not to reproduce realistic astrophysical rates, but to isolate and
analyze the statistical impact of the maximum stellar mass on supernova occurrence
within a simplified and controlled framework.

---

## Monte Carlo Method

For each scenario with a fixed maximum stellar mass \( M_{\mathrm{max}} \):

1. a population of \( N \) stars is generated,
2. stellar endpoints are determined,
3. the number of core-collapse supernovae is counted,
4. and the procedure is repeated multiple times.

From the repeated realizations, mean values, standard deviations, and confidence
intervals are computed.

A fixed random seed is set at the beginning of the simulation to ensure reproducibility.

---

## Simulation Results

The table below summarizes the main results of the Monte Carlo simulation.
It lists the mean number of core-collapse supernovae as well as the corresponding
68% confidence intervals for different values of the maximum stellar mass.

> *(The table was automatically generated from the simulation results.)*

|   M_max |   CCSN_mean |   CCSN_std |   CCSN_CI95_low |   CCSN_CI95_high |
|--------:|------------:|-----------:|----------------:|-----------------:|
|   30.00 |      226.27 |      15.98 |          196.47 |           259.20 |
|   50.00 |      246.07 |      16.64 |          211.00 |           277.00 |
|   80.00 |      259.83 |      15.71 |          231.47 |           289.00 |
|  120.00 |      261.58 |      14.18 |          235.47 |           286.57 |
|  150.00 |      264.27 |      17.90 |          227.47 |           296.52 |
|  200.00 |      267.43 |      16.27 |          236.00 |           296.52 |

---

## Reproducibility

- Python version: >= 3.9
- All external dependencies are listed in `requirements.txt`
- The simulation is fully reproducible when using the same code and random seed

---

## How to Run the Simulation

1. Create and activate a virtual environment
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. run the jupyter notebook notebooks/monte_carlo.ipynb

---

## Model Limitations

Binary stellar evolution is not included

No time evolution or delay times are modeled

The results should therefore be interpreted as comparative trends,
not as absolute astrophysical supernova rates

---

## Author / Context

This project was developed as part of a university-level project on numerical
modeling of astrophysical processes.

---
