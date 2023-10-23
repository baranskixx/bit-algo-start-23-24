from math import sqrt
def zad15(accuracy):
    pi=2
    x=sqrt(0.5)
    for _ in range(accuracy):
        pi/=x
        x=(sqrt(0.5+0.5*x))
    return pi

print(zad15(1000))