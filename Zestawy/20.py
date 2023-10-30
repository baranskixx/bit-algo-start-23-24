### BIT ALGO START
### Autor: Marcin Serafin

# Idea:
# Mamy 2 liczby a i b
# Tworzymy tablice (w funkcji diff_dig) False rozmiaru równą naszemu systemowi
# Zamieniamy na True komórki odpowiadające cyfrom z których składa sie liczba a w naszym systemie
# Sprawdzamy czy w liczbie b wystąpi taka sama cyfra
# Jeżeli nie - Zwracamy True
# Robimy tak dla każdego systemu zwracając ten dla którego diff_dig zwróci True jeżeli w ogóle taki istnieje

def diff_dig(a,b,system):
    dig=[False for _ in range(system)]
    while a>0: # Zamiana liczby na inny system (modulo i dzielenie)
        dig[a%system]=True
        a//=system
    while b>0: # Zamiana drugiej liczby ale tym razem tylko porównujemy już nie zamieniając na True
        if dig[b%system]:
            return False
        b//=system
    return True
def zad20(a,b):
    for i in range(2,16+1):
        if diff_dig(a,b,i):
            return i
    return "Non-existance"

# print(zad20(123,522))
