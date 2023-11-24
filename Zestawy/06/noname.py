### BIT ALGO START
### Autor: Marcin Serafin

# Idea:
# Klasycznie tworze funkcje rek zawierającą obie tablice, współrzedne figury, licznik oraz poprzedni ruch
# Poprzedni ruch potrzebny jest zeby nie zapętlić sie chodząc góra dół
# Jako warunki końca wybieram dojście do prawego górnego rogu
# Jak dojde to zwracam licznik
# Sprawdzam gdzie moge sie ruszyć nie wypadając poza tablice i nie wchodząc na pionka (not in)
# Porównuje maksymalny licznik(zmienna maxi) z kolejny wywołaniem (ruchem)
# Nie bierzemy pod uwage czy w ogóle da sie dojść do prawego dolnego rogu

def zad(T,P):
    def rek(T,P,y,x,cnt,prev):
        maxi=0
        if y==len(T)-1 and x==len(T)-1:
            return cnt
        if x<len(T)-1 and (x+1,y) not in P:
            maxi=max(maxi,rek(T,P,y,x+1,cnt+T[y][x+1],None))
        if y<len(T)-1 and (x,y+1) not in P:
             if prev!="down":
                maxi=max(maxi,rek(T,P,y+1,x,cnt+T[y+1][x],"up"))
        if y>0 and (x,y-1) not in P:
            if prev!="up":
                maxi=max(maxi, rek(T,P,y-1,x,cnt+T[y-1][x],"down"))
        return maxi
    return(rek(T,P,0,0,T[0][0],None))
P=[(1,1)]
T=[[1,1,1],[1,2,13],[1,3,1]]
print(zad(T,P))
