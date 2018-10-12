"""
Evaluate a polynomial
"""
import random

def polyval(x, poly):
    '''
    x value at which to evaluate a polynomial at
    poly a list of coefficients starting from constant,
    ending at the highest degree
    '''
    output = 0

    for degree, coefficient in enumerate(poly):

        output = output + pow(x,degree)*coefficient

    return output


def polyderiv(x, poly):
    '''
    x value at which to evaluate the derivative of the
    polynomial at poly a list of coefficients 
    starting from constant,
    ending at the highest degree
    '''
    output = 0

    for degree, coefficient in enumerate(poly):

        if degree-1 < 0:
            continue

        output = output + degree*pow(x,degree-1)*coefficient

    return output


def netwon_raphson(iters, poly):
    x = random.random()
    
    for i in range(iters):
        x = x - polyval(x,poly)/polyderiv(x,poly)

    return (x, polyval(x,poly))

print(netwon_raphson(100, [0, -.5, 1]))
