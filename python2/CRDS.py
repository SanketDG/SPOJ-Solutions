import sys
for _ in xrange(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    print (n*(3*n+1)/2)%1000007