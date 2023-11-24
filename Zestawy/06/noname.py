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
T=[[1,1,1],[1,2,1],[1,3,1]]
print(zad(T,P))
