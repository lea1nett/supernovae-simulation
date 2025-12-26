
import numpy as np
from sampling import sample_salpeter, sample_metallicity
from stellar_physics import ms_lifetime_years, stellar_endpoint
from supernovae import core_collapse_SN_type, is_type_ia


def run_single_mc(N, m_max, m_min=0.1, alpha=2.35):
    """
    Run one Monte Carlo realization for a given maximum stellar mass.
    Returns SN counts.
    """

    masses = sample_salpeter(N, m_min=m_min, m_max=m_max, alpha=alpha)
    metallicities = sample_metallicity(N)

    endpoints = np.array([
        stellar_endpoint(m) for m in masses
    ])

    # Supernova bookkeeping
    n_core_collapse = 0
    n_typeIa = 0

    for m, ep in zip(masses, endpoints):
        if core_collapse_SN_type(m) is not None:
            n_core_collapse += 1
        elif is_typeIa_SN(ep):
            n_typeIa += 1

    return {
        "core_collapse": n_core_collapse,
        "typeIa": n_typeIa,
        "total": n_core_collapse + n_typeIa
    }



def mc_statistics(N, m_max, n_realizations=100):
    """
    Run multiple MC realizations and compute statistics.
    """

    results = {
        "core_collapse": [],
        "typeIa": [],
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
