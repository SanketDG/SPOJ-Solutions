while True:
    x=int(raw_input())
    if x==0:
        break
    b=[0]*x
    a=map(int,raw_input().split())
    i=0
    while i<len(b):
        j=a[i]
        b[j-1]=i+1
        i+=1
    if b==a:
        print "ambiguous"
    else:
        print "not ambiguous"