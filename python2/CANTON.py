import math
for _ in xrange(int(raw_input())):
    n=int(raw_input())
    d = math.floor((-1 + (math.sqrt(1 + 8 * n))) / 2)  #Diagonals to skip
    e = n - d * (d + 1) / 2         #Extra steps after the skip.
    v1 = d + e if (e <= 1) else (d + 2 - e)
    v2 = 1 if (e <= 1) else e
    print "TERM %d IS %d/%d" %(n, v1 if d % 2 == 0 else v2, v2 if d % 2 == 0 else v1)