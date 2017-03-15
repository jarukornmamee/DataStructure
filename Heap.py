heapsize = 0
def parent(i):
    return int(i/2)
def left(i):
    return int(2*i)

def right(i):
    return int(2*i)+1

def  maxheapify(a,i):
    global heapsize
    l = left(i)
    r = right(i)
    if l < heapsize and a[l] > a[i]:
        largest = l
    else:
        largest = i
    if r < heapsize and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i],a[largest] = a[largest],a[i]
        maxheapify(a,largest)
        
def build_max_heap(a):
    global heapsize
    heapsize = len(a)
    for i in range(int(len(a)/2)-1,-1,-1):
        maxheapify(a,i)
    
def heapsort(a):
    global heapsize
    build_max_heap(a)
    for i in range (len(a)-1,0,-1):
        a[0],a[i] = a[i], a[0]
        heapsize -= 1
        maxheapify(a,0)





a = [45,5,6,7,10,2,1,65]
print(a)
heapsort(a)
print(a)
