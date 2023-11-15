### BIT ALGO START
### Autor: Marcin Serafn

# Idea:
# Przechodzimy przez całą tablice(poza dwoma ostatnimi indeksami bo długość ciągu musi być >2) 
# i dla każdego elementu sprawdzamy czy należy on do ciągu podanego w zadaniu
# jeżeli należy to sprawdzamy czy kolejne liczby na ukos od niego są równe sumie dwóch poprzednich pomniejszonej o 1
# Zliczamy długość aż nie dojdziemy do końca tablicy lub warunek przestanie być spełniony
# Następnie porównujemy do maxa i robimy tak dla każdego elementu w tablicy
# Na końcu zwracamy max



def ciong(n):
    first=1
    sec=2
    while first<n:
        first,sec=sec,first+sec-1
    if first==n:
        return True
    return False



def seq(T):
    n=len(T)
    maxi=0
    for i in range(n-2):
        for j in range(n-2):
            leng=2
            k=2
            first=T[i][j]
            if ciong(first):
                sec=T[i+1][j+1]
                while i+k<n and j+k<n:
                    if T[i+k][j+k]==first+sec-1:
                        leng+=1
                        first,sec=sec,T[i+k][j+k]
                    else:
                        break
                    k+=1
                maxi=max(maxi,leng)
    return maxi if maxi>2 else 0
