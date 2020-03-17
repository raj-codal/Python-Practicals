L = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

def bsearch(L,e):
    l,r = 0,len(L)-1
    while True :
        if L[l] == e :
            return l
        elif L[r] == e :
            return r 
        else :
            m = (l + r)//2
            if L[m] == e :
                return m
            else :
                if l == m or r == m :
                    return -1
                if e < L[m] :
                    r = m
                else :
                    l = m
                    
print(bsearch(L,13))
