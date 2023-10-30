### BIT ALGO START
### Autor: Marcin Serafin

# Idea:
# Szukamy palidromu poprzez znalezienie "Pivota"
# Dla Nieparzystej długości palindromu:
### Szukamy liczby nieparzystej która na lewo i prawo ma równe sobie liczby nieparzyste
### Rozchodzimy sie na boki sprawdzając czy kolejne liczby są sobie równe - jeżeli tak dodajemy 2 do countera
# Dla parzystych 
### Szukamy liczby nieparzystej która na lewo LUB prawo ma liczbe sobie równą
### Rozchodzimy sie na boki sprawdzając czy kolejne liczby są sobie równe - jeżeli tak dodajemy 2 do countera
# Zwarcamy największą długość


def is_odd(a):
    return a%2==1
def pali(T,a,b):
    n=len(T)
    i=0
    cnt=0
    while b+i<n and a-i>=0:
        if not T[b+i]==T[a-i]:
            return cnt
        if is_odd(T[b+i]) and is_odd(T[a-i]):
            cnt+=2
            i+=1
        else:
            return cnt
    return cnt

def zad18(T):
    n=len(T)
    maxi=0
    for i in range(1,n-1):
        if is_odd(T[i]):
            if is_odd(T[i+1]) and T[i]==T[i+1]:
                maxi=max(maxi,pali(T,i,i+1))
            maxi=max(maxi,pali(T,i-1,i+1)+1)

    return maxi
# T1=[1,3,5,7,7,5,3,1]
# T2=[1,3,5,7,5,3,1]
# T3=[1,3,5,7,2,5,3,1]
# print(zad18(T1))
# print(zad18(T2))
# print(zad18(T3))