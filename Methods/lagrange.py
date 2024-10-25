import numpy as np
import sympy as sp

def lagrange(x, y, decimals, x_sym = sp.symbols('x')):
    n = len(x)
    pol = 0 
    pol_rounded = 0
    
    for i in range(n):
        Li = 1
        den = 1
        
        for j in range(n):
            if j != i:
                Li *= (x_sym - x[j])
                den *= (x[i] - x[j])
        
        pol += y[i] * Li / den
        pol_rounded += np.round(y[i], decimals) * Li / den
    
    # Simplify the resulting polynomials
    pol_sim = sp.simplify(pol)
    pol_rounded_sim = sp.simplify(pol_rounded)
    
    return pol, pol_rounded, pol_sim, pol_rounded_sim