from math import sqrt
for _ in xrange(int(raw_input())):
        a,b,c,d=map(float,raw_input().split())
        s=(a+b+c+d)/2.0
        print sqrt((s-a)*(s-b)*(s-c)*(s-d))