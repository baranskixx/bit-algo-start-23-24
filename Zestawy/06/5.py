from math import sqrt
def is_prime(n):
    if n<2:
        return False
    if n==2 or n==3 or n==5:
        return True
    if not n%2 or not n%3 or not n%5:
        return False
    i=7
    while i<sqrt(n):
        if not n%i:
            return False
        i+=4
        if not n%i:
            return False
        i+=2
    return True

def to_decimal(T):
    res=0
    n=len(T)
    for i in range(n):
        res+=T[i]*(2**(n-i-1))
    return res

def zad6(T):
    def rek(T,i,j):
        if j>=len(T):
            return False
        if j==len(T)-1 and is_prime(to_decimal(T[i:j+1])):
            return True
        if is_prime(to_decimal(T[i:j+1])):
            return rek(T,j+1,j+2) or rek(T,i,j+1)
        else:
            return rek(T,i,j+1)
    return rek(T,0,1)

T=[1,1,1,0,1,1]
print(zad6(T))
