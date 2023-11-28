# =================================================================================================
# Author:                   Austin Purvis
# Email Addresse:           atpu225@uky.edu
# Date:                     11/27/23
# Purpose:                  Implements the composite trapezoid method. Further description below.
# =================================================================================================

import numpy as np

def trap_composite(f, a, b, n):

    h = (b-a)/n

    result = 0.5 * (f(a) + f(b))

    for i in range(1,n):
        result = result + f(a + i * h)

    result = result * h

    return result

def f(x):
    return x * np.log(x)

# Define the interval [a, b] and the number of iterations (n)
a = 1
b = 2
n = 4

# Compute the Romberg array
result = trap_composite(f, a, b, n)

# Display the result
print("Result:")
print(result)