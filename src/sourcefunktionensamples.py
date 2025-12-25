## sourcefunctions based on simple stellar population
## synthesis models (in astrophysics)


import numpy as np

def sample_salpeter(n, m_min=0.1, m_max=100.0, alpha=2.35):
    """
    (population layer function)
    Sample n stellar masses from a Salpeter initial mass function (IMF).
    
    The Salpeter IMF is defined as:
        dN/dM ∝ M^(-2.35)
        """
    n = int(n)
    x = np.random.random(n)
    a = 1.0 - alpha
    C = (m_max**a - m_min**a)
    masses = (x * C + m_min**a)**(1.0 / a)
    return masses  


def sample_metallicity(n, Z_min=0.0001, Z_max=0.03):
    """
    (population layer function)
    Sample n metallicities uniformly between Z_min and Z_max.
    """
    n = int(n)
    metallicities = np.random.uniform(Z_min, Z_max, n)
    return metallicities


def ms_lifetime_years(masses, metallicities):
    """
    (single star layer function)
    Calculate main-sequence lifetime in years for given stellar masses (in solar masses).
    
    The formula used is:
        t_MS ∝ M^(-2.5) * (Z / Z_sun)^0.2
    where Z_sun = 0.014 (solar metallicity)
    """
    return 1e10 * (masses**-2.5)*(metallicities/0.014)**0.2


def stellar_endpoint(masses):
    """
    (single star layer function)
    Determine the stellar endpoint based on mass and metallicity.
    For simplicity, we classify endpoints as:
        - White Dwarf (WD) for M < 8 M_sun
        - Neutron Star (NS) for 8 M_sun ≤ M < 20 M_sun
        - Black Hole (BH) for M ≥ 20 M_sun
    """
     if masses < 8.0:
         return('WD')
    elif 8.0 <= masses < 20.0:
        return('NS')
    else:
        return('BH')    