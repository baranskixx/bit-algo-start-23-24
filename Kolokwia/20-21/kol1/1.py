### BIT ALGO START
### Autor: Adam Barański

# Idea:
# Znajdujemy wszystkie wielokrotne napisy - czyli takie, ze istnieje dla nich jakas liczba k, taka
# ze pierwsze k liter w wyrazie (jako sekwencja) powtarza sie jakas liczbe m razy (gdzie m jest naturalne > 1, k jest naturalne)
# Jak jakis wyraz jest wielokrotny to porownujemy jego dlugosc z dlugoscia najdluzszego dotychczas znalezionego

def czy_wielokrotny(s):
    n = len(s)
    
    if len(s) == 1:
        return True

    for fragment_len in range(1, (n//2) + 1):
        if n % fragment_len == 0:
            for fragment_start in range(fragment_len, n, fragment_len):
                fragments_match = True
                for i in range(fragment_len):
                    if s[i] != s[fragment_start + i]:
                        fragments_match = False
                        break

                if not fragments_match:
                    break
            else:
                return True

    return False


def zad2(T):
    n = len(T)

    max_len = 0
    for s in T:
        if (czy_wielokrotny(s)):
            max_len = max(max_len, len(s))
    
    return max_len
