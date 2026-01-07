# sampling.py
# this module contains functions for sampling stellar masses and metallicities
# according to specified distributions.

import numpy as np

def sample_salpeter(n, m_min=0.1, m_max=100.0, alpha=2.35):
    """
    Sample n stellar masses from a Salpeter initial mass function (IMF).
    (star population layer function)

    The Salpeter IMF is defined as:
        dN/dM ∝ M^(-2.35)
    
    Parameters:
    n : int
        Number of stellar masses to sample.
    m_min : float, optional
        Minimum stellar mass (default: 0.1).
    m_max : float, optional
        Maximum stellar mass (default: 100.0).
    alpha : float, optional
        Power law index of the IMF (default: 2.35).

    Returns:
    np.ndarray
        Array of sampled stellar masses.
    """
    n = int(n)
    x = np.random.random(n)
    a = 1.0 - alpha
    C = (m_max**a - m_min**a)
    masses = (x * C + m_min**a)**(1.0 / a)
    return masses  


def sample_metallicity(n, Z_min=0.0001, Z_max=0.03):
    """
    Sample n metallicities uniformly between Z_min and Z_max,
    based on typical metallicity ranges in stellar populations.
    (star population layer function)
   
    Parameters:
    n : int
        Number of metallicities to sample.
    Z_min : float, optional
        Minimum metallicity (default: 0.0001).
    Z_max : float, optional
        Maximum metallicity (default: 0.03).

    Returns:
    np.ndarray
        Array of sampled metallicities.
    """
    n = int(n)
    metallicities = np.random.uniform(Z_min, Z_max, n)
    return metallicities
