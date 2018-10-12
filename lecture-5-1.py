"""
Example of functions using Newton-Raphon
"""
import random

def f(x):
    return x*x*x - 2*x*x + 4*x + 1

def df(x):
    return 3*x*x - 4*x + 4

def netwon_raphson(iters):
    x = random.random()
    
    for i in range(iters):
        x = x - f(x)/df(x)

    return (x, f(x))

print(netwon_raphson(10))