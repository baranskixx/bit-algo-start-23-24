### BIT ALGO START
### Autor: Marcin Serafin

# Idea:
# Rozwiązanie tego zadania opiera sie o stworzenie największej potrzebnej tablicy - takiej o rozmiarze równej wartości liczby
# Następnie w pętli rekurencyjnie odejmujemy od niej kolejne liczby wpisując je do tablicy
# Kiedy nasza liczba zmnieszy sie do 0 printujemy Tablice
# Dzięki rekurencji po każdym jej wywołaniu do komórki do której wstawiliśmy składnik wstawiamy ponownie 0 żeby mieć miejsce na inny sposób rozłożenia liczby

def zad13(n):
    T=[0]*n
    def rek(n,i,T):
        if n==0:
            print(T)
        if(i==0):
            mini=1
        else: mini=T[i-1]
        for j in range(mini,n+1):
            T[i]=j
            rek(n-j,i+1,T)
            T[i]=0
    rek(n,0,T)
print(zad13(4))