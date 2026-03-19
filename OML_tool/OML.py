import numpy as np
from numpy.typing import ArrayLike
from typing import Union
pi = np.pi
kb = 1.380649e-23


def I_tot_sphere(
        V: Union[float, ArrayLike], 
        A: float, 
        qs: list, 
        Ts: list, 
        ns: list, 
        ms: list) -> Union[float, ArrayLike]:
    """
    Calculate the total current for a spherical probe.

    Parameters
    ----------
    V : float or numpy.ndarray
        The voltage applied to the probe.
    A : float
        The area of the probe.
    qs : list of float
        List of charges of the particles.
    Ts : list of float
        List of temperatures of the particles.
    ns : list of float
        List of densities of the particles.
    ms : list of float
        List of masses of the particles.

    Returns
    -------
    float or numpy.ndarray
        The total current calculated for the probe.
    """
     
    if type(V) is not np.ndarray:
        V = np.array([V])
    I = np.zeros(V.shape)

    for q, T, n, m in zip(qs, Ts, ns, ms):
        I += I_sphere(V, A, q, T, n, m)
    
    if len(I) == 1:
        return I[0]
    else:
        return I
    
def I_tot_cylinder(
    V: Union[float, ArrayLike], 
    A: float, 
    qs: list, 
    Ts: list, 
    ns: list, 
    ms: list) -> Union[float, ArrayLike]:
    """
    Calculate the total current for a cylindrical probe.

    Parameters
    ----------
    V : float or numpy.ndarray
        The voltage applied to the probe.
    A : float
        The area of the probe.
    qs : list of float
        List of charges of the particles.
    Ts : list of float
        List of temperatures of the particles.
    ns : list of float
        List of densities of the particles.
    ms : list of float
        List of masses of the particles.

    Returns
    -------
    float or numpy.ndarray
    The total current calculated for the probe.
    """
    if type(V) is not np.ndarray:
        V = np.array([V])
    I = np.zeros(V.shape)

    for q, T, n, m in zip(qs, Ts, ns, ms):
        I += I_cylinder(V, A, q, T, n, m)
    
    if len(I) == 1:
        return I[0]
    else:
        return I


def I_sphere(
        V: Union[float, ArrayLike], 
        A: float, 
        q: float, 
        T: float, 
        n: float, 
        m: float) -> Union[float, ArrayLike]:
    """
    Calculate the current for a spherical probe.

    Parameters
    ----------
    V : float or numpy.ndarray
        The voltage applied to the probe.
    A : float
        The area of the probe.
    q : float
        The charge of the particle.
    T : float
        The temperature of the particle.
    n : float
        The density of the particles.
    m : float
        The mass of the particles.

    Returns
    -------
    float or numpy.ndarray
        The current calculated for the probe.
    """
    if type(V) is not np.ndarray:
        V = np.array([V])
    I = np.zeros(V.shape)

    I0 = I0_sphere(A, q, T, n, m)
    X = -q*V /(kb*T)

    mask = V * np.sign(q) >= 0
    I[mask] = I0 * np.exp(X[mask])
    I[~mask] = I0 * (1+X[~mask])

    if len(I) == 1:
        return I[0]
    else:
        return I

def I_cylinder(
    V: Union[float, ArrayLike], 
    A: float, 
    q: float, 
    T: float, 
    n: float, 
    m: float) -> Union[float, ArrayLike]:
    """
    Calculate the current for a cylindrical probe.

    Parameters
    ----------
    V : float or numpy.ndarray
        The voltage applied to the probe.
    A : float
        The area of the probe.
    q : float
        The charge of the particle.
    T : float
        The temperature of the particle.
    n : float
        The density of the particles.
    m : float
        The mass of the particles.

    Returns
    -------
    float or numpy.ndarray
    The current calculated for the probe.
    """

    if type(V) is not np.ndarray:
        V = np.array([V])
    I = np.zeros(V.shape)

    I0 = I0_cylinder(A, q, T, n, m)
    X = -q*V /(kb*T)

    mask = V * np.sign(q) >= 0
    I[mask] = I0 * np.exp(X[mask])
    I[~mask] = I0 *  np.sqrt(np.abs(1+X[~mask]+0j))
    
    if len(I) == 1:
        return I[0]
    else:
        return I
    

def I0_tot_sphere(
    A: float, 
    qs: list, 
    Ts: list, 
    ns: list, 
    ms: list) -> float:
    """
    Calculate the zero-voltage current for a spherical probe.

    Parameters
    ----------
    A : float
        The area of the probe.
    qs : list of float
        List of charges of the particles.
    Ts : list of float
        List of temperatures of the particles.
    ns : list of float
        List of densities of the particles.
    ms : list of float
        List of masses of the particles.

    Returns
    -------
    float
        The zero-voltage current.
    """
    I0 = 0
    for q, T, n, m in zip(qs, Ts, ns, ms):
        I0 += I0_sphere(A, q, T, n, m)
    
    return I0


def I0_tot_cylinder(
    A: float, 
    qs: list, 
    Ts: list, 
    ns: list, 
    ms: list) -> float:
    """
    Calculate the zero-voltage current for a cylindrical probe.

    Parameters
    ----------
    A : float
        The area of the probe.
    qs : list of float
        List of charges of the particles.
    Ts : list of float
        List of temperatures of the particles.
    ns : list of float
        List of densities of the particles.
    ms : list of float
        List of masses of the particles.

    Returns
    -------
    float
        The zero-voltage current.
    """
    I0 = 0
    for q, T, n, m in zip(qs, Ts, ns, ms):
        I0 += I0_cylinder(A, q, T, n, m)
    
    return I0
    
    
def I0_sphere(
    A: float, 
    q: float, 
    T: float, 
    n: float, 
    m: float) -> float:
    """
    Calculate the zero-voltage current for a spherical probe.

    Parameters
    ----------
    A : float
        The area of the probe.
    q : float
        The charge of the particle.
    T : float
        The temperature.
    n : float
        The density of the particles.
    m : float
        The mass of the particles.

    Returns
    -------
    float
        The zero-voltage current.
    """
    return A * n * q * np.sqrt( (kb * T) / (2 * pi * m) )


def I0_cylinder(
    A: float, 
    q: float, 
    T: float, 
    n: float, 
    m: float) -> float:
    """
    Calculate the zero-voltage current for a cylindrical probe.

    Parameters
    ----------
    A : float
        The area of the probe.
    q : float
        The charge of the particle.
    T : float
        The temperature.
    n : float
        The density of the particles.
    m : float
        The mass of the particles.

    Returns
    -------
    float
        The zero-voltage current.
    """
    return 2 /(np.sqrt(pi)) * A * n * q * np.sqrt( (kb * T) / (2 * pi * m) )