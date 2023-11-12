### BIT ALGO START
### Autor: Marcin Serafin

# Idea:
# Przechodzimy przez całą tablice T
# Dla każdego elementu sprawdzamy z kim sąsiaduje
# Robimy to pętlą przez tablice krotek zawierające kierunki sąsiadów (usuwa nam 8 if'ów)
# Sprawdzamy czy sąsiedz są przyjaciółmi
# Tworzymy tablice 10 elementową T2 reprezentującą 10 cyfr
# Przechodzimy przez jedną liczbe i wartość dla indeksu w tablicy jej odpowiadającemu zamieniamy na 1
# Dla drugiej liczby robimy to samo sprawdzając czy spotkamy tylko takie same cyfry (zamieniamy wtedy z 1 na 2)
# Na końcu przechodzimy przez tablice T2 sprawdzając czy nie pozostała jakaś cyfra występująca w liczbie pierwszej ale nie w drugiej
# Dla każdego spełniającego te warunki elementu z tablicy T dodajemy +1 do countera
# Zwracamy counter



def are_friends(a,b):
    T2=[0 for _ in range(10)]
    n=len(T)
    while a>=1:
        num=a%10
        T2[num]=1
        a//=10
    while b>=1:
        num=b%10
        if T2[num]!=0:
            T2[num]=2
        else:
            return False
        b//=10
    for i in range(n):
        if T2[i]==1:
            return False
    return True
def side(T,i,j):
    n=len(T)
    sides=[(-1,0),(-1,-1),(-1,1),(1,-1),(1,0),(1,1),(0,-1),(0,1)]
    for k in sides:
        if 0<=i+k[0]<n and 0<=j+k[1]<n:
            if not are_friends(T[i+k[0]][j+k[1]],T[i][j]):
                return False
    return True          
def zad11(T):
    n=len(T)
    cnt=0
    for i in range(n):
        for j in range(n):
            if side(T,i,j):
                cnt+=1
    return cnt
T=[[12,121,12,4],[12,21,21,4],[21,21,21,4],[5,5,5,5]]
print(zad11(T))










# if i>0:
#         if not are_friends(T[i][j],T[i-1][j]):
#             return False
#         if j>0:
#             if not are_friends(T[i][j],T[i-1][j-1]):
#                 return False  
#         if j<n-1:
#             if not are_friends(T[i][j],T[i-1][j+1]):
#                 return False
#     if i<n-1:
#         if not are_friends(T[i][j],T[i+1][j]):
#             return False
#         if j>0:
#             if not are_friends(T[i][j],T[i+1][j-1]):
#                 return False
#         if j<n-1:
#             if not are_friends(T[i][j],T[i+1][j+1]):
#                 return False
#     if j>0:
#         if not are_friends(T[i][j],T[i][j-1]):
#             return False
#     if j<n-1:
#         if not are_friends(T[i][j],T[i][j+1]):
#             return False