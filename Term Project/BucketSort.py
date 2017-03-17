from InsertionSort import*

def bsort(A):
  """Returns A sorted. with A = {x : x such that 0 <= x < 1}."""
    b = [[] for x in range(10)]
    for i, x in enumerate(A):
        buckets[int(x*len(b))].append(x)
    out = []
    for buck in b:
        out += isort(buck)
    return out

a = [10,15,12,13,1,5,9,7,2]
bucketsort(a)
print(a)
