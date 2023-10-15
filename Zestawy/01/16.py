### BIT ALGO START
### Autor: Adam Barański

# Załozenia: 
# A_1 = X ; X - jakaś liczba
# A_n+1 = (An mod 2) ∗ (3 ∗ An + 1) + (1 − An mod 2) ∗ An/2
# Idea: 
# Dla kazdego wyrazu poczatkowego wyznaczamy ilosc kroków przy
# uzyciu liczba_krokow(A) - najwieksza ilosc krokow oraz opdowiadajacy 
# jej wyraz poczatkowy zapisujemy do zmiennych max_steps i max_start

LIM = 1
EPS = 1e-8

def liczba_krokow(A):
    cnt = 0

    while A != LIM:
        cnt += 1 # cnt = cnt + 1
        A = (A % 2) * (3 * A + 1) + (1 - (A % 2)) * (A/2)
    
    return cnt

def zad16():
    max_steps = 0
    max_start = None

    for a in range(10000, 1, -1):
        steps = liczba_krokow(a)
        if steps > max_steps:
            max_steps = steps
            max_start = a

    print("Liczba krokow: " + str(max_steps))
    print("Wyraz poczatkowy: " + str(max_start))

if __name__ == '__main__':
    zad16()