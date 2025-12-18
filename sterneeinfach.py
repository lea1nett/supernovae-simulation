import numpy as np
import matplotlib.pyplot as plt

# Einfache Annahmen (sehr grob):
# - Masseverteilung: Salpeter-IMF ~ M^-2.35 between 0.1 and 50 Msun
# - Hauptreihenlebensdauer (yrs) ~ 1e10 * (M/Msun)^-2.5

def sample_salpeter(n, m_min=0.1, m_max=50, alpha=2.35):
    # inversesampling
    x = np.random.random(n)
    a = 1.0 - alpha
    C = (m_max**a - m_min**a)
    return (m_min**a + x*C)**(1.0/a)

def ms_lifetime_years(m):
    return 1e10 * (m**-2.5)

N = 20000
masses = sample_salpeter(N)
lifetimes = ms_lifetime_years(masses)

# einfache Auswertung
print("Median Masse:", np.median(masses))
print("Median MS-Lebensdauer (Jahre):", np.median(lifetimes))

# Histogramm der Lebensdauern
plt.hist(np.log10(lifetimes), bins=60)
plt.xlabel("log10(Hauptreihenlebensdauer [yr])")
plt.show()
