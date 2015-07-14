def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
for _ in xrange(int(raw_input())):
    a,b=map(int,raw_input().split())
    g=gcd(a,b)

    if g==1:
        print b,a,"\n"
    else:
        bp=a/g
        ap=b/g
        print ap,bp,"\n"