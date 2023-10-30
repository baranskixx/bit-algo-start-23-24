### BIT ALGO START
### Autor: Marcin Serafin

# Idea:
# Tworzymy zmienną PI równą 2
# W pętli tworzymy kolejne elementy ciągu postaci x(n+1)=(sqrt(0.5+0.5*x(n)))
# Następnie dzielimy nasze pi przez nasze x
# Robimy tak tyle razy ile chcemy (tutaj tyle ile równa jest zmienna accuracy)


from math import sqrt
def zad15(accuracy):
    pi=2
    x=sqrt(0.5)
    for _ in range(accuracy):
        pi/=x
        x=(sqrt(0.5+0.5*x))
    return pi

# print(zad15(1000))