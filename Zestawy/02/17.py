### BIT ALGO START
### Autor: Wiktor Warzecha

# Idea: 
# Przy pomocy wzoru rekurencyjnego (wikipedia) na wyliczanie kolejnych
# przybliżeń wartości x, iteracyjnie wyliczamy x0, do momentu, gdy
# wartość f(x0) jest różna od 2020 o maksymalnie eps

from math import log, e

def f(x):
    return x ** x - 2020

def f_prim(x):
    return (x**x)*(log(x,e)+1)

def Newton(x0, eps = 10e-6):
    while abs(f(x0))>eps:
        x0 = x0 - f(x0)/f_prim(x0)
    return x0, f(x0) + 2020

print(Newton(4))