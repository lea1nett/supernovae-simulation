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
