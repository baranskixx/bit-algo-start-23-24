### BIT ALGO START
### Autor: Adam Barański

# Idea: 
# Funkcja rekurencyjna rek odpowiada na następujące pytanie:
# Zakładając, ze kazdy z 3 zbiorow ma wagę elementów odpowiednio a, b i c
# Oraz analizujemy elementy od i do n-1 włącznie, 
# czy mozliwe jest rozdzielenie pozostałych elementów tak, by zbiory posiadały elementy o sumarycznie równych wagach (a == b == c)
# Zakładamy, ze kazdy element trafi do jakiegoś zbioru (zaden nie jest pomijany)
# Warunki końcowe:
# Rekurencje kończymy w momencie gdy skończyły nam się liczby do przeanalizowania


def waga(num):
    cnt = 0
    i = 2

    while num != 1:
        if num % i == 0:
            cnt += 1
        while num % i == 0:
            num //= i
        
        i += 1
        
    return cnt
            

def zad6(T):
    n = len(T)
    def rek(i, a, b, c):
        if i == n:
            return a == b and b == c
        
        return rek(i+1, a + waga(T[i]), b, c) or rek(i+1, a , b + waga(T[i]), c) or rek(i+1, a , b, c + waga(T[i]))
    
    return rek(0, 0, 0, 0)

