def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

for _ in xrange(int(raw_input())):
    a,b=map(int,raw_input().split())
    print abs((a-b)/gcd(a,b))