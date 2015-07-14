while True:
    b,n=map(int,raw_input().split())
    if b==0 and n==0:
        break
    b2=[]
    n2=[]
    for i in range(n):
        b1,n1=map(int,raw_input().split())
        b2.append(b1)
        n2.append(n1)
    d={}
    for i in range(0,n+1):
        for w in range(b+1):
            if i==0 or w==0:
                d[i,w]=0
            elif b2[i-1] <= w:
                d[i,w]=max(n2[i-1]+d[i-1,w-b2[i-1]], d[i-1,w])
            else:
                d[i,w]=d[i-1,w]
    cost=0
    for c in range(0,b+1):
        if d[n,c] == d[n,b]:
            cost=c
            break
    m=cost,d[n,b]
    c,p=map(str,m)
    print c+" "+p
    raw_input()
