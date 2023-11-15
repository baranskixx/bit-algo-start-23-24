### BIT ALGO START
### Autor: Wiktor Warzecha

# Zadanie 19. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# zwraca liczbę par elementów, o określonym iloczynie, takich że elementy są odległe o jeden ruch skoczka
# szachowego.

# Idea:
# Dla każdego pola sprawdzamy czy wartość pola na którym stoi skoczek i wartość pola szachowanego są
# równe zadanemu iloczynowi. Żeby nie powtarzać powtórzeń sprawdzamy pola tylko dla połowy możliwych
# ruchów skoczka. Ruchy te nie mogą być "przeciwne".

def zad19(T, x):
    n = len(T)
    moves = [(2,1),(2,-1),(1,-2),(-1,-2)]
    counter = 0
    for r in range(n):
        for c in range(n):
            for move in moves:
                if -1 < r + move[1] < n and -1 < c + move[0] < n and T[r + move[1]][c + move[0]]*T[r][c] == x:
                    counter += 1
    return counter

T = [
    [1,0,0,0],
    [1,0,1,0],
    [0,0,0,0],
    [0,1,0,0]
]
print(zad19(T,1))