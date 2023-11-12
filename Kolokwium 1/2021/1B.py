### BIT ALGO START
### Autor: Marcin Serafin

# Idea:
# Sposobem na rozwiązanie tego zadania jest jednokrotne przejście przez tablice
# Jeżeli spotkamy liczbe pierwszą to mnożymy ją przez nasz iloczyn (na początku równy 1)
# Jeżeli spotkamy liczbe złożoną to porównujemy ją do iloczynu
# Jeżeli są sobie równe to sprawdzamy czy ta liczba jest większa od maxa i w takim wypadku maxa zamieniamy na tą liczbe
# A pod zmienną przechowującą indeks podstawiamy indeks tej liczby
# Na koniec zwaracamy indeks największej liczby spełniającej warunki zadania


def is_prime(num):
    if num> 1:  
        for n in range(2,num):  
            if (num % n) == 0:  
                return False
        return True
    else:
        return False



def zad1(T):
    n=len(T)
    maxi=0
    ind=None
    ilo=1
    for i in range(n):
        if is_prime(T[i]):
            ilo*=T[i]
        if T[i]==ilo:
            if T[i]>maxi:
                maxi=T[i]
                ind=i
    return ind



T=[2,4,5,7,70,7,2,980,1000] #7

print(zad1(T))