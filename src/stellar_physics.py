# stellar_physics.py
# This module contains functions related to stellar physics,
# specifically for calculating main-sequence lifetimes and
# determining stellar endpoints based on mass and metallicity.

import numpy as np

def ms_lifetime_years(masses, metallicities):
    """
    Calculate main-sequence lifetime in years for given stellar masses.
    (single star layer function)

    The formula used is:
        t_MS ∝ M^(-2.5) * (Z / Z_sun)^0.2
        where Z_sun = 0.014 (solar metallicity)
    
    Parameters:
    masses : float or np.ndarray
        Stellar masses in solar masses.
    metallicities : float or np.ndarray
        Metallicities in solar units.

    Returns:
    float or np.ndarray
        Main-sequence lifetimes in years.
    """
    return 1e10 * (masses**-2.5)*(metallicities/0.014)**0.2


def stellar_endpoint(masses):
    """
    Determine the stellar endpoint based on mass and metallicity.
    (single star layer function)

    For simplicity, we classify endpoints as:
        - White Dwarf (WD) for M < 8 M_sun
        - Neutron Star (NS) for 8 M_sun ≤ M < 20 M_sun
        - Black Hole (BH) for M ≥ 20 M_sun
    
    Parameters:
    masses : float
        Stellar mass in solar masses.

    Returns:
    str
        Stellar endpoint type: 'WD', 'NS', or 'BH'.
    """
    if masses < 8.0:
         return('WD')
    elif 8.0 <= masses < 20.0:
         return('NS')
    else:
        return('BH')    