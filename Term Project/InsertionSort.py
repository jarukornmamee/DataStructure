
def insertionsort(list) :
    for x in range (1,len(list)) :

        ivalue = list[x]

        while x > 0 and list[x - 1] > ivalue:
            list[x] = list[x - 1]
            x = x - 1

        list[x] = ivalue

if __name__== '__main__' :
    
    list = [5,4,6,8,7,1,0]
    insertionsort(list)
    print(list)


