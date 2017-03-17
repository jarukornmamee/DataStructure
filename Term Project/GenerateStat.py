from MergeSort import*
from InsertionSort import*
from HeapSort import*
from Selectionsort import*
from Quicksort import*


import time
current_time = lambda: int(round(time.time()*1000))

x =["ampleData100","ampleData500","ampleData1000","ampleData1500","ampleData2000","ampleData2500","ampleData3000","ampleData3500","ampleData4000","ampleData4500","ampleData5000","ampleData10000","ampleData15000","ampleData20000","ampleData25000","ampleData30000","ampleData35000","ampleData40000","ampleData45000","ampleData50000","ampleData100000","ampleData150000","ampleData200000","ampleData250000","ampleData300000","ampleData350000","ampleData400000","ampleData450000","ampleData500000"]
y =["ampleData200000","ampleData250000","ampleData300000","ampleData350000","ampleData400000","ampleData450000","ampleData500000"]

for i in range (0,len(y)):
    datafile = "test\S"
    datafile += y[i]
    datafile += '.dat'
    
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

    ## Test Quick sort
    print("Quick sort")
    start = current_time()
    quicksort(data5,0,len(data5)-1)
    end = current_time()
    print ("Elapse time: %d mil.seconds" % (end - start))
