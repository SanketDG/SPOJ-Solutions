while True:
    n=int(raw_input())
    if n==-1:
        break
    else:
        p=[]
        for _ in xrange(n):
            p.append(int(raw_input()))
        p.sort()
        avg=sum(p)/n
        if sum(p)%n==0 and avg>0:
            i=0
            c=0
            while p[i]<avg:
                    c=c+avg-p[i]
                    i+=1
            print c
        else:
            print "-1"