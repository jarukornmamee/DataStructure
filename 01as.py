import turtle as t

##for x in range(4):
## t.forward(100)
## t.left(90)
##
##
##for x in range(4):
## t.right(90)
## t.forward(100)
##
##for x in range(6):
## t.circle(50)
## t.circle(80)
## t.circle(100)
## t.rt(60)
##

def insertionsort(list) :
    for x in range (1,len(list)) :

        ivalue = list[x]

        while x > 0 and list[x - 1] > ivalue:
            list[x] = list[x - 1]
            x = x - 1

        list[x] = ivalue





list = [5,4,6,8,7,1,0]
insertionsort(list)
print(list)


