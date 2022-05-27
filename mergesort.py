
tab = [36, 7, 82, 4, 93, 18, 70]

def sortowanie(tab):

    if len(tab) > 1:
        m = len(tab)//2
        L = tab[:m]
        R = tab[m:]
        sortowanie(L)
        sortowanie(R)
        
        i = 0
        j = 0
        k = 0

        while i < len(L) and j < len(R) :
            if L[i] < R[j]:
                tab[k] = L[i]
                k = k + 1
                i = i + 1
            else:
                tab[k] = R[j]
                k = k + 1
                j = j + 1

        while i < len(L):
            tab[k] = L[i]
            i = i + 1

        while j < len(R):
            tab[k] = R[j]
            j = j + 1

    
        
sortowanie(tab)
print(tab)
    



