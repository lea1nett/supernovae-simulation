## Supernova Models source file

import numpy as np

def core_collapse_SN_type(masses):
    """
    (single star layer function)
    Classify supernova types based on progenitor masses.
    """
    if masses < 8.0:
        return None
    elif 8.0 <= masses < 20.0:
        return 'Type II'    
    elif 20.0 <= masses < 40.0:
        return 'Type Ib'
    else:
        return 'Type Ic'
    
def is_type_ia(masses, binary_fraction=0.5, ia_efficiency=0.02):
    """
    (single star layer function)
    Determine if a star will undergo a Type Ia supernova.
    Type Ia supernovae are thought to originate from white dwarfs in binary systems.
    type Ia needs: low mass star + binary system + some efficiency factor
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
    
