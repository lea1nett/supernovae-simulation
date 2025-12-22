## sourcefunctions based on simple stellar population
## synthesis models (in astrophysics)

import numpy as np

def sample_salpeter(n, m_min=0.1, m_max=100.0, alpha=2.35):
    """
    Sample n stellar masses from a Salpeter initial mass function (IMF).
    
    The Salpeter IMF is defined as:
        dN/dM ∝ M^(-2.35)
        """
    x = np.random.random(n)
    a = 1.0 - alpha
    C = (m_max**a - m_min**a)
    masses = (x * C + m_min**a)**(1.0 / a)
    return masses  


def sample_metallicity(n, Z_min=0.0001, Z_max=0.03):
    """
    Sample n metallicities uniformly between Z_min and Z_max.
    """
    metallicities = np.random.uniform(Z_min, Z_max, n)
    return metallicities


def ms_lifetimes_years(masses, metallicities):
    """
    Calculate main-sequence lifetimes in years for given stellar masses (in solar masses).
    
    The formula used is:
        t_MS ≈ 10^10 * (M / M_sun)^(-2.5) years
    """
    return 1e10 * (masses ** -2.5)


def stellar_endpoints(masses):
    """
    Determine the stellar endpoints based on mass and metallicity.
    For simplicity, we classify endpoints as:
        - White Dwarf (WD) for M < 8 M_sun
        - Neutron Star (NS) for 8 M_sun ≤ M < 20 M_sun
        - Black Hole (BH) for M ≥ 20 M_sun
    """
    endpoints = []
    for m in masses:
        if m < 8.0:
            endpoints.append('WD')
        elif 8.0 <= m < 20.0:
            endpoints.append('NS')
        else:
            endpoints.append('BH')
    return endpoints