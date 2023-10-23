def diff_dig(a,b,system):
    dig=[False for _ in range(system)]
    while a>0:
        dig[a%system]=True
        a//=system
    while b>0:
        if dig[b%system]:
            return False
        b//=system
    return True
def zad20(a,b):
    for i in range(2,16+1):
        if diff_dig(a,b,i):
            return i
    return "Non-existance"

print(zad20(123,522))