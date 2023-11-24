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

def king(N,L):
    def rek(N,L,y,x,cnt,prev):
        maxi=0
        if y==N-1 and x==N-1:
            return cnt
        
        if x<N-1 and (y,x+1) not in L:
            maxi=max(maxi,rek(N,L,y,x+1,cnt+1,None))

        if y<N-1 and (y+1,x) not in L:
             if prev!="down":
                maxi=max(maxi,rek(N,L,y+1,x,cnt+1,"up"))

        if y>0 and (y-1,x) not in L:
            if prev!="up":
                maxi=max(maxi, rek(N,L,y-1,x,cnt+1,"down"))
                
        return maxi
    return(rek(N,L,0,0,0,None))
L=[(0,1)]
N=3
print(king(N,L))
