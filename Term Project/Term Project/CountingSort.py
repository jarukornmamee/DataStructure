def countingsort( A, k ):
    counter = [0] * ( k + 1 )
    for i in A:
      counter[i] += 1
 
    index = 0;
    for i in range( len( counter ) ):
      while 0 < counter[i]:
        A[index] = i
        index += 1
        counter[i] -= 1

