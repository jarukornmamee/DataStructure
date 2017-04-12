
def insertionsort(list) :
    for x in range (1,len(list)) :

        value = list[x]

        while x > 0 and list[x - 1] > value:
            list[x] = list[x - 1]
            x = x - 1

        list[x] = value


