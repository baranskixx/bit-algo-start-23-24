### BIT ALGO START
### Autor: Adam Barański

# Idea:
# Mamy funkcje, ktora sprawdza wspolnoczynnikowosc dwoch liczb.
# Korzystamy z niej, wywolujac ja dla kazdego elementu w tablicy, ktory posiada 4 sasiadow
# Wywolujemy ja oczywiscie 4 razy - dla relacji ten badany element - sąsiąd


def wspolno_czynnikowe(a, b):
    cnt = 0

    i = 2
    while a != 1 and b != 1:
        cnt_a = 0
        while a % i == 0:
            a /= i
            cnt_a += 1
        
        cnt_b = 0
        while b % i == 0:
            b /= i
            cnt_b += 1
        
        cnt += min(cnt_a, cnt_b)
        
        i += 1

        if cnt > 1:
            return False
    
    return cnt == 1


def four(T):
    N = len(T)

    cnt = 0

    for y in range(1, N-1):
        for x in range(1, N-1):
            if wspolno_czynnikowe(T[y][x], T[y-1][x]) and wspolno_czynnikowe(T[y][x], T[y+1][x]) and \
            wspolno_czynnikowe(T[y][x], T[y][x-1]) and wspolno_czynnikowe(T[y][x], T[y][x+1]):
                cnt += 1
    
    return cnt
