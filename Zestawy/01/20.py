### BIT ALGO START
### Autor: Adam Barański

# Idea: 
# Obliczamy kolejne wyrazy ciagu korzystajac z podanych w tresci zadania wzorow
# W momencie, gdy roznica miedzy n-tym wyrazem ciagu A i B jest mniejsza niz 
# ustawiony EPS przerywamy obliczenia
from math import sqrt

EPS = 1e-12

def zad20(A, B):
    while abs(A - B) > EPS:
        A, B = sqrt(A * B), (A + B) / 2
    return A

if __name__ == '__main__':
    x = 1
    y = 5
    print("Średnia geometryczno-arytmetyczna z liczb {} oraz {} wynosi {}"
          .format(x, y, zad20(1, 5)))