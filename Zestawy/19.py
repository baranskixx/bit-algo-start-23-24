### BIT ALGO START
### Autor: Marcin Serafin

# Idea:
# Tworzymy zmienne liczące długość, sume, i sume indeksów ciagu
# W pętli Szukamy libczy dla której liczba kolejna jest większa
# W kolejnej pętli szukamy kolejnych takich liczb cały czas zwiększając counter
# Jednocześnie porównując sume i sume indeksów - kiedy są równe porównujemy je z maximum
# Jeżeli kolejna liczba będzie mniejsza to przerywamy i szukamy nowego początku ciągu


T=[1,2,1,5,6,7,7,8,4]
def zad19(T):
    n=len(T)
    maxi=0
    for i in range(n-1):
        suma=T[i]
        cnt=1
        sum_ind=i
        if T[i]<T[i+1]:
            for j in range(i+1,n):
                if not T[j-1]<T[j]:
                    break
                else:
                    suma+=T[j]
                    sum_ind+=j
                    cnt+=1
                    if suma==sum_ind:
                        maxi=max(maxi,cnt)
    return maxi
# T=[1,2,1,5,6,7,7,8,4]
# print(zad19(T))