<img src="configs/logo.png" alt="Logo" width="220" align="left" />  

# Monte Carlo Simulation of Supernova Rates

### This project investigates the influence of the maximum stellar mass on supernova rates in a stellar populations using a Monte Carlo simulation approach. Only the evolution of isolated single stars is considered.

---

## Project Structure

```text
├── configs/
│ └── simulation.yml
│
├── figures/
│ ├── ccsn_confidence_intervalls.png
│ ├── ccsn_vs_m_max.png
│ └── single_star_population_results.png
│
├── reports/
│ ├── ABOUT.txt
│ └── supernovae_results.md
│
├── src/
│ ├── __init__.py
│ ├── sampling.py
│ ├── mc_functions.py
│ ├── stellar_physics.py
│ └── supernovae.py
│
├── environment.yml
│
├── monte_carlo.ipynb
│
└── README.md
```

- `configs/` contains seeds and parameters, this is **not needed** to run the simulation
- `figures/`contains png-plots generated in the notebok
- `reports/`contains the results in short texts 
- `src/` contains all physical and stochastic model functions as well as the functions for
   multiple monte-carlo runs
- `monte_carlo.ipynb` is the jupyter notebook used to run the simulation and perform the analysis
- all data is generated synthetically within the Monte Carlo simulations

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
  evolution is not included in this model, Type Ia supernovae occur in the single 
  star population statistic, but not in the Monte-Carlo simulation.

The model neglects metallicity effects, rotation, mass loss, and binary interactions.
Its purpose is not to reproduce realistic astrophysical rates, but to isolate and
analyze the statistical impact of the maximum stellar mass on supernova occurrence
within a simplified and controlled framework.

---

## Single Star Population

A single-scenario star population is generated.  
Each star has a definite mass, metallicity, lifetime and endstate, these properties are sampled using astrophysical functions.  
Afterwards it is determined, which type of supernovae each star may become.

---

## Monte Carlo Method

For each scenario with a fixed maximum stellar mass `M_max`:

1. a population of `N` stars is generated,
2. stellar endpoints are determined,
3. the number of core-collapse supernovae is counted,
4. and the procedure is repeated multiple times.

From the repeated realizations, mean values, standard deviations, and confidence
intervals are computed.

---

## Simulation Results

The table below summarizes representative results of the Monte Carlo simulation.  
It lists the mean number of core-collapse supernovae as well as the corresponding
95% confidence intervals for different values of the maximum stellar mass.

*(The table was automatically generated from simulation results.)*

|   M_max |   CCSN_mean |   CCSN_std |   CCSN_CI95_low |   CCSN_CI95_high |
|--------:|------------:|-----------:|----------------:|-----------------:|
|      30 |      226.27 |    15.9835 |         196.475 |          259.2   |
|      50 |      246.07 |    16.642  |         211     |          277     |
|      80 |      259.83 |    15.714  |         231.475 |          289     |
|     120 |      261.58 |    14.1836 |         235.475 |          286.575 |
|     150 |      264.27 |    17.8958 |         227.475 |          296.525 |
|     200 |      267.43 |    16.2706 |         236     |          296.525 | 

## Additional Results

A concise summary of the numerical results, including a short interpretation and details 
on the model limitations, is provided in a separate report:
[`reports/supernova_results.md`](reports/supernovae_results.md)

---

## Reproducibility

The simulation results are reproducible in a statistical sense.

The simulation environment is fully specified using a Conda environment file
([`environment.yml`](environment.yml)).  
This ensures that the simulation can be reproduced with identical library versions across different systems.

- Python version: as specified in `environment.yml`
- All required dependencies are listed explicitly in the environment file
- A fixed random seed is used in the Monte Carlo notebook to ensure same results

When the environment is created from the provided file and the same code is used,
the simulation results are fully reproducible.

---

## How to Run the Simulation

1. Ensure that Conda (or Miniconda) is installed on your system.

2. Create the Conda environment from the provided `environment.yml` file:
   ```bash
   conda env create -f environment.yml
   ```

3. Activate the environment:
   ```bash
   conda activate myenvo
   ```

4. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

5. Open and run the Notebook:
   ```bash
   notebooks/monte_carlo.ipynb
   ```

---

## Author / Context

This project was developed as part of a university-level project on simulation tools.  
More information in [`reports/ABOUT.txt`](reports/ABOUT.txt)

---
