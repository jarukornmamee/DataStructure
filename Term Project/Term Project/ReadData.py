from MergeSort import*
from InsertionSort import*
from HeapSort import*
from Selectionsort import*

import time

current_time = lambda: int(round(time.time()*1000))

datafile = "test\SampleData10000.dat"
with open (datafile) as f:
    data = f.read().splitlines()

print(len(data))
data = list(map(int, data))


data1 = data[:]
data2 = data[:]
data3 = data[:]
data4 = data[:]
data5 = data[:]

## Test Merge Sort
print("Merge Sort")
start = current_time()
merge_sort(data1,0,len(data1)-1)
end = current_time()
print ("Elapse time: %d mil.seconds" % (end - start))


## Test Insertion sort
print("Insertion sort")
start = current_time()
insertionsort(data2)
end = current_time()
print ("Elapse time: %d mil.seconds" % (end - start))


## Test Heap sort
print("Heap Sort")
start = current_time()
heapsort(data3)
end = current_time()
print ("Elapse time: %d mil.seconds" % (end - start))


## Test Selection sort
print("Selection sort")
start = current_time()
selectionsort(data4)
end = current_time()
print ("Elapse time: %d mil.seconds" % (end - start))
