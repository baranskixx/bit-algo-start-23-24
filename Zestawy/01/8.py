### BIT ALGO START
### Autor: Adam Barański

# Idea: 
# Kazda funkcja zwraca informacje, czy przekazana w 
# argumencie funkcji liczba jest pierwsza
# 1) Najprostszy program - is_prime(x)
# Sprawdza kazda liczbe z zakresu [2, sqrt(x)] 
# Jeśli jakaś liczba z tego zakresu dzieli bez reszty x 
# zwraca False - no bo wtedy x nie moze byc pierwsza
# Początkowy if sprawia, ze zgodnie z prawda dla liczby 1 wynik bedzie True
# # # # # # # # # # # # # # # # # # # # # # # # # 
# 2) is_prime_v2 i v3 
# W obu przypadkach korzystamy z sita Erastotenesa, 
# w przypadku v3 ten koncept jest trochę bardziej rozwinięty - tam eleminujemy ze 
# sprawdzania nie tylko liczby, które sa wielokrotnością 2 ale równiez i 3

from math import sqrt

def is_prime(a):
    if a <= 1:
        return False
    i = 2

    while i <= sqrt(a):
        if a % i == 0:
            return False
        i += 1

    return True

def is_prime_v2(a):
    if a == 2:
        return True
    if a % 2 == 0 or a == 1:
        return False
    
    i = 3
    while i <= sqrt(a):
        if a % i == 0:
            return False
        i += 2

    return True

def is_prime_v3(a):
    if a == 2 or a == 3:
        return True
    if a % 2 == 0 or a % 3 == 0 or a == 1:
        return False
    
    i = 6
    while i <= sqrt(a):
        if a % (i-1) == 0 or a % (i+1) == 0:
            return False
        i += 6

    return True