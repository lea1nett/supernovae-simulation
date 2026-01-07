# supernovae.py
# this module contains functions to classify supernova types based on progenitor star properties.
# currently only core-collapse supernovae (type II, Ib, Ic) and type Ia supernovae are considered.

import numpy as np

def core_collapse_SN_type(masses):
    """
    Classify supernova types based on progenitor masses.
    (single star layer function)

    Parameters:
    masses (float): 
        Mass of the progenitor star in solar masses.

    Returns:
    str or None: 
        Type of supernova ('Type II', 'Type Ib', 'Type Ic') or None if no supernova occurs.
    """
    if masses < 8.0:
        return None
    elif 8.0 <= masses < 20.0:
        return 'Type II'    
    elif 20.0 <= masses < 40.0:
        return 'Type Ib'
    else:
        return 'Type Ic'
    
def is_type_ia(masses, binary_fraction=0.5, ia_efficiency=0.01):
    """
    Determine if a star will undergo a Type Ia supernova.
    (single star layer function)

    annotation:
    Type Ia supernovae need: low mass star + binary system + some efficiency factor
    assumption: a small but non-zero fraction of white dwarfs will eventually lead to a type Ia SN.

    Parameters:
    masses (float):
        Mass of the progenitor star in solar masses.
    binary_fraction (float, optional): 
        Fraction of stars in binary systems (default: 0.5).
    ia_efficiency (float, optional):
        Efficiency factor for Type Ia supernova occurrence (default: 0.01).

    Returns:
    bool:
        True if the star will undergo a Type Ia supernova, False otherwise.
    """
    try:
        masses = float(masses)
    except ValueError:
        return False
    if masses >= 8:
        return False
    if np.random.random() > binary_fraction:
        return False
    return np.random.random() < ia_efficiency
    
