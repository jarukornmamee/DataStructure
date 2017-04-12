import math
def insertionsort(list) :
    for x in range (1,len(list)) :

        value = list[x]

        while x > 0 and list[x - 1] > value:
            list[x] = list[x - 1]
            x = x - 1

        list[x] = value

def bucketsort( A ):
  code = hashing( A )
  buckets = [list() for _ in range( code[1] )]
  for i in A:
    x = re_hashing( i, code )
    buck = buckets[x]
    buck.append( i ) 
  for bucket in buckets:
    insertionsort( bucket )
    index = 0
  for b in range( len( buckets ) ):
    for v in buckets[b]:
      A[index] = v
      index += 1
 

 
def hashing( A ):
  m = A[0]
  for i in range( 1, len( A ) ):
    if ( m < A[i] ):
      m = A[i]
  result = [m, int( math.sqrt( len( A ) ) )]
  return result
 
 
def re_hashing( i, code ):
  return int( i / code[0] * ( code[1] - 1 ) )




