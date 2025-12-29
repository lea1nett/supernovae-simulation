# Monte Carlo Simulation of Supernova Rates

This project investigates the influence of the maximum stellar mass on supernova
rates in a stellar population using a Monte Carlo simulation approach.
Only the evolution of isolated single stars is considered.

The focus is on core-collapse supernovae. Type Ia supernovae do not occur in the model,
as binary stellar evolution is not included.

---

## Project Structure

├── src/
│ ├── init.py
│ ├── sampling.py
│ ├── stellar_physics.py
│ └── supernovae.py
│
├── notebooks/
│ └── monte_carlo.ipynb
│
├── requirements.txt
└── README.md


- `src/` contains all physical and stochastic model functions  
- `notebooks/` contains the Jupyter notebook used to run the simulation and perform the analysis  

---

## Physical Model

The simulation is based on the following assumptions:

- Stellar masses are sampled from a Salpeter initial mass function (IMF)
- A population of isolated single stars is simulated
- Core-collapse supernovae originate from stars above a fixed mass threshold
- Type Ia supernovae are not modeled, as binary systems are not included

The model is intentionally simplified in order to isolate the effect of the maximum
stellar mass on supernova rates.

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

<!-- INSERT df.to_markdown() TABLE HERE --> ## Simulation Results

The table below summarizes the results of the Monte Carlo simulation
for different values of the maximum stellar mass.

| M_max | CCSN_mean | CCSN_std | CCSN_CI68_low | CCSN_CI68_high |
|------:|----------:|---------:|--------------:|---------------:|
|  30.0 |     ...   |    ...   |       ...     |        ...     |
|  50.0 |     ...   |    ...   |       ...     |        ...     |
|  80.0 |     ...   |    ...   |       ...     |        ...     |
| 120.0 |     ...   |    ...   |       ...     |        ...     |


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