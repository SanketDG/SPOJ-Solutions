def isPowerOfTwo (x):
  return ((x != 0) and ((x & (~x + 1)) == x))

n=int(raw_input())
if isPowerOfTwo(n):
    print "TAK"
else:
    print "NIE"