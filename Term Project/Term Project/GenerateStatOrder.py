from MergeSort import*
from InsertionSort import*
from HeapSort import*
from Selectionsort import*
from Bubblesort import*


import time
current_time = lambda: int(round(time.time()*1000))

x =["ampleData100","ampleData500","ampleData1000",
    "ampleData1500","ampleData2000","ampleData2500",
    "ampleData3000","ampleData3500","ampleData4000",
    "ampleData4500","ampleData5000","ampleData5500",
    "ampleData6000","ampleData6500","ampleData7000",
    "ampleData7500","ampleData8000","ampleData8500",
    "ampleData9000","ampleData9500","ampleData10000",
    "ampleData11000","ampleData12000","ampleData13000",
    "ampleData14000","ampleData15000","ampleData16000",
    "ampleData17000","ampleData18000","ampleData19000",
    "ampleData20000","ampleData21000","ampleData22000",
    "ampleData23000","ampleData24000","ampleData25000",
    "ampleData26000","ampleData27000","ampleData28000",
    "ampleData29000","ampleData30000"]

for i in range (0,len(x)):
    datafile = "OrderSampleData\S"
    datafile += x[i]
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

    ## Test Bubble sort
    print("Bubble sort")
    start = current_time()
    bubbleSort(data5)
    end = current_time()
    print ("Elapse time: %d mil.seconds" % (end - start))
