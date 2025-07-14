import numpy as np

pi = np.pi
kb = 1.380649e-23


def I_sphere(V,A,q,T,n,m):
        if type(V) is not np.ndarray:
            V = np.array([V])
        I = np.zeros(V.shape)
    
        I0 = I0_sphere(A, q, T, n, m)
        X = -q*V /(kb*T)

        mask = q*V >= 0
        I[mask] = I0 * np.exp(X[mask])
        I[~mask] = I0 * (1+X[~mask])

        if len(I) == 1:
            return I[0]
        else:
            return I

def I_cylinder(V,A,q,T,n,m):
        if type(V) is not np.ndarray:
            V = np.array([V])
        I = np.zeros(V.shape)


        I0 = I0_cylinder(A, q, T, n, m)
        X = -q*V /(kb*T)

        mask = q*V >= 0
        I[mask] = I0 * np.exp(X[mask])
        I[~mask] = I0 *  np.sqrt(np.abs(1+X[~mask]+0j))
        
        if len(I) == 1:
            return I[0]
        else:
            return I
        
def I0_sphere(A, q, T, n, m):

    return A * n * q * np.sqrt( (kb * T) / (2 * pi * m) )

def I0_cylinder(A, q, T, n, m):
     
     return 2 /(np.sqrt(pi)) * A * n * q * np.sqrt( (kb * T) / (2 * pi * m) )