def insertsort(tab):
    n = len(tab)
    for i in range(1, n):
        a = tab[i]

        j= i - 1
        while j >= 0 and a < tab[j]:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = a


tab = [78, 92, 33, 2, 76, 43]

insertsort(tab)

print("sorted array is: ")
for i in range(len(tab)):
    print (f"number {tab[i]}")