### BIT ALGO START
### Autor: Adam Barański

# Idea:
# Jeśli mamy dwie rózne liczby w zapisie binarnym, to większą jest ta, która 
# w pierwszym miejscu od lewej (zakładamy, ze obie liczby są zapisane na np 1000 bitach)
# gdzie róznią się bity, to większa jest ta liczba, która w miejscu tej pierwszej róznicy ma bit '1'
#
# Jak mamy zbiór liczb, i znamy w tym zbiorze maksimum to gdy dokładamy do zbioru kolejną liczbę
# to sprawdzamy, czy nasz nowo dodany element nie jest nowym minimum lub maksimum. Zachowujemy tylko pozycje
# największej i najmniejszej liczby, porównujemy je funkcją compare:
#
# 0 - równe
# 1 - A > B
# -1 - B > A    - dziala to na takiej zasadzie jak comparatory w Javie, moze ktos sie spotkal
# 
#

def compare(A, B):
    n = len(A)

    for i in range(n):
        if A[i] != B[i]:
            return 1 if A[i] == 1 else -1
    return 0

def distance(T):
    n = len(T)

    max_index = 0
    min_index = 0

    for i in range(1, n):
        if compare(T[i], T[max_index]) == 1:
            max_index = i
        elif compare(T[min_index], T[i]) == 1:
            min_index = i
    
    return abs(max_index - min_index)