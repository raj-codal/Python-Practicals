def selection_sort(L):
    
    for i in range(len(L)):
        z = L[i:]
        t = min(z)
        j = i + z.index(t)
        L[i],L[j] = L[j],L[i]
    return L

print(selection_sort([1,9,2,4,1]))
