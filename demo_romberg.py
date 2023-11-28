# =================================================================================================
# Author:                   Austin Purvis
# Email Addresse:           atpu225@uky.edu
# Date:                     11/27/23
# Purpose:                  
# =================================================================================================

import numpy as np
from romberg import romberg


def f(x):
    return np.power(x,2) * np.log(x)

def f_a(x):
    return 1/(1+x)

def f_b(x):
    return np.exp(x)

def f_c(x):
    return 4/(1+np.power(x,2))

a = 1
b = 1.5
n = 2

# Compute the Romberg array
result = romberg(f, a, b, n)

# Display the result
print("Romberg array R:")
for x in result:
    print(x)