
def czy_samogloska(ch):
    return ch in ['a', 'e', 'y', 'u', 'i', 'o']

def cutting(s):
    n = len(s)

    def rek(i, cnt):
        if i == n:
            return cnt
        
        if czy_samogloska(s[i]):
            cnt += 1
        
        if cnt == 2:
            return 0
        elif cnt == 1:
            return rek(i+1, 0) + rek(i+1, 1)
        return rek(i+1, 0)

    return rek(0, 0)


print(cutting('student')) # wypisze 2 bo stu-dent, stud-ent
print(cutting('sesja')) # wypisze 3 bo se-sja, ses-ja, sesj-a
print(cutting('ocena')) # wypisze 4 bo o-ce-na, o-cen-a, oc-e-na, oc-en-a,
print(cutting('informatyka')) # wypisze 36