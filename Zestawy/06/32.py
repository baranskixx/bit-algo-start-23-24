### BIT ALGO START
### Autor: Wiktor Warzecha

# Zadanie 32. Dana jest tablica T[N] zawierająca liczby naturalne. 
# Proszę napisać funkcję, która odpowiada na pytanie, czy spośród 
# (niekoniecznie wszystkich) elementów tablicy można utworzyć dwa 
# podzbiory o jednakowej sumie elementów, tak aby suma mocy obu 
# podzbiorów wynosiła k. Do funkcji należy przekazać
# wyłącznie tablicę T oraz liczbę naturalną k, 
# funkcja powinna zwrócić wartość typu bool.

# Idea:
# Przy pomocy funkcji rekurencyjne rozważamy wszystkie możliwe podzbiory,
# warunek końcowy sprawdza czy dana kombinacja spełnia założenia, jeśli
# tak zwraca True, w przeciwnym wypadku, jeżeli jesteśmy poza tablicą,
# zwraca False. Funkcja zawiera 3-krotne wywołanie samej siebie, dla
# dołożenia liczby do zbioru 1-wszego, do zbioru 2-giego i sytuacji w której
# pomijamy liczbę na danym indeksie. Są one połączone or'ami, ponieważ
# wystarczy że którakolwiek z kombinacji spełnia założenia, aby funkcja
# zwróciła True.

def zad32(T,k):
    def rec(k,i,fir,fi,sec,si):
        if fi != 0 and fi == si and fir == sec == k:
            return True
        elif i == len(T):
            return False
        else:
            return rec(k,i+1,fir,fi,sec,si) or rec(k,i+1,fir+T[i],fi+1,sec,si) or rec(k,i+1,fir,fi,sec+T[i],si+1)
    
    return rec(k,0,0,0,0,0)

print(zad32([2,1,3,7,0],4))