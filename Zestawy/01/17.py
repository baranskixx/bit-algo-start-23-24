### BIT ALGO START
### Autor: Wiktor Warzecha

# Idea: 
# obliczamy wartości stosunku wyrazów kolejnych ciągów fibbonaciego
# dla dwóch pierwszych par, następnie w pętli, do momentu gdy wynik
# kolej iteracji (curr_fib_ratio) różni się od wcześniejszego 
# (prev_fibb_ratio) o maksymalnie eps

def Fib_ratio(a,b,eps = 10e-3):  # Przy założeniu że a,b mają ten sam znak i są różne od zera
    prev_fib_ratio = b/a
    a,b = b, a+b
    curr_fib_ratio = b/a

    while(abs(prev_fib_ratio - curr_fib_ratio) > eps):
        a,b = b, a+b
        prev_fib_ratio = curr_fib_ratio
        curr_fib_ratio = b/a
    return curr_fib_ratio

def Fib_ratio_v2(a,b,eps = 10e-3):  # Dla dowolnych wartości a,b
    if a == 0 and b == 0:
        print("Wrong data")
        return
    
    while (a * b <= 0): # wykonujemy aż uzyskamy a i b o różnych znakach
        a,b = b, a + b
    
    return(Fib_ratio(a,b,eps))
    

# print(Fib_ratio(1,1))
# print(Fib_ratio(-1,-1))
# print(Fib_ratio_v2(-1,0))
# print(Fib_ratio_v2(-4,3))

