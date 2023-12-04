### BIT ALGO START
### Autor: Marcin Serafin

# Idea:
# Tworze funkcje rek którą bede rekurencyjnie wyknywał
# Jak zawsze najpierw pisze warunki końca tj.
# Jeżeli zbiore odpowiednia mase zwracam True
# Jeżeli przejde przez całą tablice a masa dalej nie jest równa 0 zwracam False
# Case zad 7: 
#   Odpalam Funkcje i albo biore odważnik odejmując go od całej masy i przesuwam indeks +1
#   albo nie biore i przesuwam indeks +1
#
# Case zad 8:
# Jak wyżej ale dodaje kolejną możliwość wywowania rek
# Tym razem kładąc na drugą X co oznacza dodanie wagi odważnika do masy
#
# Case zad 9:
# Jak wyżej ale jeżeli dojde do masy równej 0 do printuje tablice którą przekazuje rekurencyjnie w rek
# Dodaje do tej tablicy za pomocą łączenia tablic
# Do już stworzonej dodaje jednoelemntową z wagą odważnika (Bo nie wolno appenda)

def zad7(T,m):
    def rek(T,i,m):
        if m==0:
            return True
        if i>=len(T):
            return False
        return rek(T,i+1,m-T[i]) or rek(T,i+1,m)
    return rek(T,0,m)



def zad8(T,m):
    def rek(T,i,m):
        if m==0:
            return True
        if i>=len(T):
            return False
        return rek(T,i+1,m-T[i]) or rek(T,i+1,m) or rek(T,i+1,m+T[i])
    return rek(T,0,m)



def zad9(T,m):
    def rek(T,i,m,chosen):
        if m==0:
            print(chosen)
            return True
        if i>=len(T):
            return False
        return rek(T,i+1,m-T[i],chosen+[T[i]]) or rek(T,i+1,m+T[i],chosen+[T[i]]) or rek(T,i+1,m,chosen)
            
    return rek(T,0,m,[])
    

T=[2,3,7,2]
print(zad7(T,6)) #False
print(zad8(T,6)) #True
print(zad9(T,6)) #[2,3,7] True