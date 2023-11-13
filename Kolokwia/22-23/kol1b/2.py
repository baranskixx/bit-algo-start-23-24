### BIT ALGO START
### Autor: Wiktor Warzecha

# Dana jest kwadratowa tablica T wypełniona liczbami naturalnymi. Proszę napisać funkcję square(T), która
# znajdzie najmniejszy kwadratowy fragment tablicy, mniejszy niż cała tablica, taki że liczba będąca iloczynem
# czterech narożnych pól tego fragmentu w rozkładzie na czynniki pierwsze posiada tylko dwa różne czynniki.
# Funkcja powinna zwrócić rozmiar (bok) znalezionego kwadratu. Jeżeli kwadrat taki nie istnieje funkcja powinna zwrócić 
# wartość 0.
# Uwagi:
# • Można założyć, że tablica wejściowa ma rozmiar co najmniej 3x3.

# Idea:
# Dla każdej długości kwadratu w kolejności rosnącej sprawdzamy wszystkie możliwe kwadraty tak długo,
# aż spełnią wymagany warunek.

def is_correct(n):
    count = 0
    i = 2
    while n > 1:
        if n % i == 0:
            count += 1
            if count > 2:
                return False
            else:
                while n % i == 0:
                    n //= i
        i += 1
    if count == 2:
        return True
    return False

def square(T):
    n = len(T)
    for a in range(2,n):
        for i in range(n - a + 1):
            for j in range(n - a + 1):
                if is_correct(T[i][j] * T[i+a-1][j] * T[i][j+a-1] * T[i+a-1][j+a-1]):
                    return a
    return 0




T = [
    [   30, 30, 30, 30, 30],
    [   30, 2,  30, 3,  30],
    [   30, 30, 2,  30, 3],
    [   30, 5,  30, 3,  30],
    [   30, 30, 2,  30, 2]
]
print(square(T))