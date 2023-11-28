# =================================================================================================
# Author:                   Austin Purvis
# Email Addresse:           atpu225@uky.edu
# Date:                     11/27/23
# Purpose:                  Implements the Romberg method. Further description below.
# =================================================================================================

import numpy as np


def romberg(f, a, b, n):
    
    R = np.zeros((n+1,n+1))

    h = b-a
    R[0,0] = 0.5 * h * (f(a)+f(b))

    for i in range(1, n+1):

        h = (b-a)/2**i
        total = 0

        for k in range(1, 2**(i-1) + 1):
            total = total + f(a + (2*k-1)*h)

        R[i, 0] = 0.5 * R[i-1,0] + h * total

        for j in range(1, i+1):
            R[i,j] = R[i, j-1] + (R[i, j-1] - R[i-1, j-1]) / (4**j - 1)

    return R 

def f(x):
    return np.power(x,2) * np.log(x)

# Define the interval [a, b] and the number of iterations (n)
a = 1
b = 1.5
n = 2

# Compute the Romberg array
result = romberg(f, a, b, n)

# Display the result
print("Romberg array R:")
for x in result:
    print(x)
