### BIT ALGO START
### Autor: Wiktor Warzecha

# Zadanie 18. Dana jest tablica T[N][N] wypełniona liczbami całkowitymi. Proszę napisać funkcję, która
# wyszuka spójny podciąg elementów leżący poziomo lub pionowo o największej sumie. Maksymalna długość
# podciągu może wynosić 10 elementów. Do funkcji należy przekazać tablicę T, funkcja powinna zwrócić sumę
# maksymalnego podciągu.

# Idea:
# Sprawdzamy wszystkie podciągi, ale żeby nie powtarzać obliczeń robimy to tylko do prawej i do dołu.

def zad18(T):
    for e in T:
        print(e)
    
    n = len(T)
    biggest_sum = -float('inf')
    for r in range(n):
        for c in range(n):
            # Suma podciągu w poziomie
            i = 0
            sum = 0
            while c + i < n and i < 10:
                sum += T[r][c + i]
                if sum > biggest_sum:
                    biggest_sum = sum
                i += 1
            # Suma podciągu w pionie
            i = 0
            sum = 0
            while r + i < n and i < 10:
                sum += T[r + i][c]
                biggest_sum = max(biggest_sum, sum)
                i += 1
    return biggest_sum

T = [
    [1,2,-1,4],
    [2,4,-3,0],
    [3,2,4,5],
    [-1,-2,-3,-4]
]
print(zad18(T))
            