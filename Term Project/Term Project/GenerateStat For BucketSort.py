from BucketSort import*


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
    datafile = "RandomSampleData\S"
    datafile += x[i]
    datafile += '.dat'
    
    with open (datafile) as f:
        data = f.read().splitlines()

    print(len(data))
    data = list(map(int, data))

    data1 = data[:]

    
    ## Test Bucket Sort
    print("Random Bucket Sort")
    start = current_time()
    (data1)
    bucketsort(data1)
    end = current_time()
    print ("Elapse time: %d mil.seconds" % (end - start))
    print()
   


for i in range (0,len(x)):
    datafile = "OrderSampleData\S"
    datafile += x[i]
    datafile += '.dat'
    
    with open (datafile) as f:
        data = f.read().splitlines()

    print(len(data))
    data = list(map(int, data))

    data2 = data[:]

    ## Test Bucket Sort
    print("Order Bucket Sort")
    start = current_time()
    bucketsort(data2)
    end = current_time()
    print ("Elapse time: %d mil.seconds" % (end - start))
    print()


for i in range (0,len(x)):
    datafile = "ReverseSampleData\S"
    datafile += x[i]
    datafile += '.dat'
    
    with open (datafile) as f:
        data = f.read().splitlines()

    print(len(data))
    data = list(map(int, data))

    data3 = data[:]
    ## Test Bucket Sort
    print("Reverse Bucket Sort")
    start = current_time()
    bucketsort(data3)
    end = current_time()
    print ("Elapse time: %d mil.seconds" % (end - start))
    print()







