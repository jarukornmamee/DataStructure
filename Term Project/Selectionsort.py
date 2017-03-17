def findmax(a,i):
    m = 0
    for i in range(1,i+1):
        if a[i] > a[m]:
            m = i
    return m

def selectionsort(a):
    for i in range(len(a)-1,-1,-1):
        j = findmax(a,i)
        a[i],a[j] = a[j],a[i]

