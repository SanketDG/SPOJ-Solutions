import math
while True:
    s=raw_input()
    if "-1 -1" in s:
        break
    g,b=map(int,s.split())
    m1=max(g,b)
    m2=min(g,b)
    if g==0 and b==0:
        print 0
    elif g==0 or b==0:
        print m1
    elif g==1 or b==1:
        if g==1 and b==1:
            print 1
        elif m1%2==0:
            print m1/2
        else:
            print (m1+1)/2
    elif m1-m2==1:
        print 1
    elif m1-m2==2:
        print 2
    elif b==g:
        print 1
    else:
        print int(math.ceil(m1/float(m2+1)))
