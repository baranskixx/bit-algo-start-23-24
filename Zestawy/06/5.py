### BIT ALGO START
### Autor: Marcin Serafin

# Idea:
# Rozwiązanie tego zadania będzie polegało na stworzeniu sobie klasycznych funkcji to_decimal i is_prime
# Następnie rekurencyjnie wywołujemy funkcje która albo bierze albo nie bierze indeksu na którym jesteśmy
# Jeżeli nie bierze to sprawdza czy już wzięte indeksy składają sie na liczbe pierwszą
# Jeżeli tak to funkcja uruchamia sie dalej
# Jeżeli nie to zwraca False
# Robimy tak aż do ostatniego indeksu dla którego ponownie sprawdzamy czy wzięte indeksy tworzą liczbe pierwszą
# Dodatkowo przed sprawdziem "pierwszości" liczby możemy sprawdzić czy kończy sie 0 mając więcej niż 2 cyfry
# (na 0 kończą sie parzyste a 10 czyli 2 w dziesiętnym jako jedyna pierwsza jest parzysta)


from math import sqrt
def is_prime(n):
    if n<2:
        return False
    if n==2 or n==3 or n==5:
        return True
    if not n%2 or not n%3 or not n%5:
        return False
    i=7
    while i<sqrt(n):
        if not n%i:
            return False
        i+=4
        if not n%i:
            return False
        i+=2
    return True
def decimal(T):
    res=0
    n=len(T)
    for i in range(n):
        res+=T[i]*(2**(n-i-1))
    return res
def zad5(T):
    def rek(i,j,T):
        if j>len(T)-1:
            return False
        if j==len(T)-1:
            if T[j-1]==0 and j-i+1!=2:
                return False
            return is_prime(decimal(T[i:j+1]))
        if is_prime(decimal(T[i:j+1])):
            return rek(j+1,j+2,T)
        return rek(i,j+1,T)  
    return rek(0,1,T) if len(T)>1 else False
T=[1,1,0,1,0,0]
print(zad5(T))