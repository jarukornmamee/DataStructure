top_S = 0

def Stack_empty(S):
    global top_S
    if top_S == 0:
        return True
    else :
        return False

def push(S,w):
    global top_S
    top_S += 1
    S[top_S] = w

def pop (S):
    global top_S
    if Stack_empty(S):
        raise IndexError("UnderFlow")
    else:
        top_S -= 1
        return S[top_S + 1]

S = [0 for x in range(100)]

push(S,1)
push(S,2)
print(pop(S))
print(pop(S))
print(pop(S))
