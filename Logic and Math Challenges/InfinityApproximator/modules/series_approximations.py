# series_approximations.py
# Contains all infinite series approximation functions

import math

def e_approx(n_terms):
    return sum(1 / math.factorial(i) for i in range(n_terms))

def pi_approx(n_terms):
    return 4 * sum((-1)**i / (2*i + 1) for i in range(n_terms))

def sin_approx(x, n_terms):
    return sum(((-1)**i * x**(2*i + 1)) / math.factorial(2*i + 1) for i in range(n_terms))

def ln1p_approx(x, n_terms):
    if x <= -1:
        raise ValueError("x must be greater than -1 for ln(1+x)")
    return sum(((-1)**(i+1)) * (x**i) / i for i in range(1, n_terms + 1))
