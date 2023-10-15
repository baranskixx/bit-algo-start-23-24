### BIT ALGO START
### Autor: Adam Barański

# Idea: 
# Dla kazdego kolejnego wyrazu przemnazamy obliczona silnie (zmienna fact)
# razy kolejna liczbe. Pozwala to uniknac obliczania całej silni dla kazdego wyrazu
# Przy kazdym kolejnym obliczonym wyrazie sprawdzamy, czy jest on wiekszy od EPS 
# Jeśli jest, kończymy obliczenia i zwracamy wynik

EPS = 1e-12

def wyznacz_e():
    e = 2
    fact = 1
    i = 2

    while True:
        fact *= i
        i += 1
        next_elem = 1 / fact
        if next_elem < EPS:
            break
        e += next_elem
    
    return e


if __name__ == '__main__':
    print(wyznacz_e())