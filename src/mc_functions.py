
import numpy as np
from src.sampling import sample_salpeter, sample_metallicity
from src.stellar_physics import ms_lifetime_years, stellar_endpoint
from src.supernovae import core_collapse_SN_type, is_type_ia


def run_single_mc(N, m_max, m_min=0.1, alpha=2.35):
    """
    Run one Monte Carlo realization for a given maximum stellar mass.

    Parameters:
    N (int):
        Number of stars to simulate.
    m_max (float):
        Maximum stellar mass in solar masses.
    m_min (float, optional):
        Minimum stellar mass in solar masses (default: 0.1).
    alpha (float, optional):
        Power law index for the Salpeter IMF (default: 2.35).

    Returns:
    dict:
        Dictionary with counts of 'core_collapse', 'type_ia', and 'total' supernovae.
    """

    masses = sample_salpeter(N, m_min=m_min, m_max=m_max, alpha=alpha)
    metallicities = sample_metallicity(N)

    endpoints = np.array([
        stellar_endpoint(m) for m in masses
    ])

    # Supernova bookkeeping, count types
    n_core_collapse = 0
    n_type_ia = 0

    for m, ep in zip(masses, endpoints):
        if core_collapse_SN_type(m) is not None:
            n_core_collapse += 1
        elif is_type_ia(ep):
            n_type_ia += 1

    return {
        "core_collapse": n_core_collapse,
        "type_ia": n_type_ia,
        "total": n_core_collapse + n_type_ia
    }



def mc_statistics(N, m_max, n_realizations=100):
    """
    Run multiple MC realizations and compute statistics.

    Parameters:
    N (int):
        Number of stars to simulate in each realization.
    m_max (float):
        Maximum stellar mass in solar masses.
    n_realizations (int, optional):
        Number of Monte Carlo realizations to run (default: 100).

    Returns:
    dict:
        Dictionary with statistics (mean, std, confidence intervals) for
        'core_collapse', 'type_ia', and 'total' supernovae.
    """

    results = {
        "core_collapse": [],
        "type_ia": [],
        "total": []
    }

    for _ in range(n_realizations):
        out = run_single_mc(N, m_max)
        for key in results:
            results[key].append(out[key])

    stats = {}
    for key, values in results.items():
        arr = np.array(values)
        stats[key] = {
            "mean": np.mean(arr),
            "std": np.std(arr, ddof=1),
            "ci_68": (
                np.percentile(arr, 16),
                np.percentile(arr, 84)
            ),
            "ci_95": (
                np.percentile(arr, 2.5),
                np.percentile(arr, 97.5)
            )
        }

    return stats
