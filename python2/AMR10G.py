for _ in xrange(int(raw_input())):
    n,k=map(int,raw_input().split())
    h=map(int,raw_input().split())
    if k==1:
        print 0
    else:
        h=sorted(h)
        mindiff=h[-1]-h[0]
        for i in xrange(n-k+1):
            mindiff=min(mindiff,h[i+k-1]-h[i])
        print mindiff