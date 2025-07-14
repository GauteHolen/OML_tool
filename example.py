import numpy as np
from OML_tool import I_cylinder, I_sphere, I0_cylinder, I0_sphere
import matplotlib.pyplot as plt


# Example usage
V = np.linspace(-10, 10, 100)  # Voltage array for testing
dx = 0.5 * 1e-2  # Grid spacing in meters
r = 0.25*1e-2   # Radius in meters
l = 40 * 1e-2  # Length in meters
Te = 1000 # Electron temperature in Kelvin
Ti = 750 # Ion temperature in Kelvin
qe = -1.602176634e-19  # Electron charge in coulombs
qi = -qe
n = 1e11 # Electron density in m^-3
ne = 0.5 * n  # Assuming electron density is half of total density
ni = 0.5 * n  # Assuming ion density is half of total density
Ac =  np.pi * r*l  # Cross-sectional area of the probe
me = 9.10938356e-31  # Electron mass in kg
mi = 1800*me

Ie_c = I_cylinder(V, Ac, qe, Te, ne, me)
Ii_c = I_cylinder(V, Ac, qi, Ti, ni, mi)
Ie_s = I_sphere(V, Ac, qe, Te, ne, me)
Ii_s = I_sphere(V, Ac, qi, Ti, ni, mi)
I_tot_c = Ie_c + Ii_c
I_tot_s = Ie_s + Ii_s

I0s = I0_sphere(Ac, qe, Te, ne, me)
I0c = I0_cylinder(Ac, qe, Te, ne, me)

fig, ax = plt.subplots(1, 2, figsize=(7, 3))
ax[0].plot(V, I_tot_c/I0c, label='Cylinder Model')
ax[1].plot(V, I_tot_s/I0s, label='Sphere Model')
fig.suptitle('IV Characteristics')
ax[0].set_title('Cylinder')
ax[1].set_title('Sphere')
ax[0].set_xlabel(r'$\varphi$ (V)')
ax[0].set_ylabel(r'$I / I_0$')
ax[1].set_xlabel(r'$\varphi$ (V)')
ax[1].set_ylabel(r'$I / I_0$')
plt.tight_layout()
fig.savefig('IV_characteristics.png', dpi=300)
plt.show()