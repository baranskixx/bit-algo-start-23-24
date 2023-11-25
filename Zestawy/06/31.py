### BIT ALGO START
### Autor: Wiktor Warzecha

# Zadanie 31. Proszę napisać funkcję, która jako parametr otrzymuje
# liczbę naturalną i zwraca sumę iloczynów elementów wszystkich 
# niepustych podzbiorów zbioru podzielników pierwszych tej liczby. 
# Można założyć, że liczba podzielników pierwszych nie przekracza 20,
# zatem w pierwszym etapie funkcja powinna wpisać podzielniki do 
# tablicy pomocniczej. 
# Przykład: 60 → [2, 3, 5] → 2 + 3 + 5 + 2 ∗ 3 + 2 ∗ 5 + 3 ∗ 5 + 2 ∗ 3 ∗ 5 = 71

# Idea:
# Tworzymy tablicę divs reprezentującą zbiór podzielników liczby n. Następnie
# przy pomocy funkcji rekurencyjnej generujemy wszystkie możliwe iloczyny
# podzbiorów tablicy divs.
# Argumenty funkcji rec to prod - przekazywany wgłąb rekurencji iloczyn podzbioru
# oraz i który mówi który element jest rozpatrywany. Funkcja rec wywołuje siebie
# dwukrotnie, w jednym przypadku dla pominięcia liczby pod indeksem i - liczba ta 
# nie trafia do podzbioru, w drugim z jej uwzględnieniem - liczba trafia do podzbioru.
# Warunkiem końcowym jest i == len(T) - wyszliśmy z tablicy - oznacza to, że 
# rozpatrzyliśmy wszystkie liczby, zatem możemy dodać nasz iloczyn do sumy.
# Sum jest zdefiniowane poza funkcją rec, dlatego we wnętrzu funkcji rekurencyjnej użyliśmy
# nonlocal Sum, co pozwala odwoływać się do Sum wewnątrz rec.


from math import sqrt

def dividers(n):
    i = 2
    divs = []
    for i in range(2,int(sqrt(n)+1)):
        if n % i == 0:
            divs.append(i)
            while n % i == 0:
                n //= i
    if n != 1:
        divs.append(n)
    return divs

def zad31(n):
    divs = dividers(n)
    Sum = 0
    
    def rec(prod, i):
        nonlocal Sum
        if i == len(divs):
            Sum += prod
        else:
            rec(prod*divs[i],i+1)
            rec(prod,i+1)
    rec(1,0)

    return Sum-1

print(zad31(60))


