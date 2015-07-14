import math
pow={}
pow[2]=[2,4,8,6]
pow[3]=[3,9,7,1]
pow[4]=[4,6]
pow[7]=[7,9,3,1]
pow[8]=[8,4,2,6]
pow[9]=[9,1]

T=int(raw_input())
for _ in xrange(T):
    num=raw_input()
    b,i=map(int,num.split())
    n=b%10
    if i==0:
        print 1
    elif i==1:
        print n
    elif n==0:
        print 0
    elif n==1:
        print 1
    elif n==5:
        print 5
    elif n==6:
        print 6
    else:
        pos=i%len(pow[n])
        print pow[n][pos-1]