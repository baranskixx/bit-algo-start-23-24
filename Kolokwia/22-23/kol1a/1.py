### BIT ALGO START
### Autor: Wiktor Warzecha

# Dana jest tablica T zawierająca liczby naturalne. W tablicy na kolejnych pozycjach ukryto pewien ciąg liczb
# o długości co najmniej 3 elementów. Aby ułatwić odnalezienie tego ciągu, zaraz za nim umieszczono ten sam
# ciąg ale każdy z jego elementów pomnożono przez pewną liczbę. Proszę napisać funkcję sequence(T) która odnajdzie 
# ukryty ciąg. Funkcja powinna zwrócić indeksy pierwszego i ostatniego elementu ukrytego ciągu.
# Przykłady:
# sequence( [2,5,7,3,2,3,5,7,6,9,15,21,17,19,23,2,6,4,8,3,5,7,1,3,2] ) zwróci 4,7
# Uwagi:
# • Można założyć, że tablica wejściowa zawiera więcej niż 2 elementy.

# Idea:
# Sprawdzamy wszystkie możliwe ciągi od najdłuższych, aż znajdziemy spełniający założenie.

def check_seq(beg, end, T):
    if end >= len(T)-1:
        return False
    
    mult = T[end+1]/T[beg]

    for i in range(end-beg+1):
        if end + i + 1 >= len(T) or T[end+i+1]/T[beg+i] != mult:
            return False
    return True

def sequence(T):
    n = len(T)

    for beg in range(n):
        for length in range(n,2,-1):
            if check_seq(beg,beg+length-1,T):
                return beg,beg+length-1
    return 0

T = [2,5,7,3,2,3,5,7,6,9,15,21,17,19,23,2,6,4,8,3,5,7,1,3,2]

print (sequence(T))
