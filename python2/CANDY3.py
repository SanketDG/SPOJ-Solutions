T=int(raw_input())
for _ in xrange(T):
    x=raw_input()
    n=int(raw_input())
    arr=[]
    for _ in xrange(n):
        s=int(raw_input())
        arr.append(s)
    if (sum(arr))%n==0:
        print "YES"
    else:
        print "NO"