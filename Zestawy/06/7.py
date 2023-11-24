def zad7(T,m):
    def rek(T,i,m):
        if m==0:
            return True
        if m<0 or i>=len(T):
            return False
        return rek(T,i+1,m-T[i]) or rek(T,i+1,m)
    return rek(T,0,m)

def zad8(T,m):
    def rek(T,i,m):
        if m==0:
            return True
        if m<0 or i>=len(T):
            return False
        return rek(T,i+1,m-T[i]) or rek(T,i+1,m) or rek(T,i+1,m+T[i])
    return rek(T,0,m)
def zad9(T,m):
    def rek(T,i,m,chosen):
        if m==0:
            print(chosen)
            return True
        if m<0 or i>=len(T):
            return False
        if(rek(T,i+1,m-T[i],chosen+[T[i]]) or rek(T,i+1,m+T[i],chosen+[T[i]]) or rek(T,i+1,m,chosen)):
            return True
    return rek(T,0,m,[])
    

T=[2,3,7,2]
print(zad7(T,6))
print(zad8(T,6))
print(zad9(T,6))