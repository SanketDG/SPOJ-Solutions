def sumsq(n):
    n=str(n)
    s=0
    for i in n:
        s+=int(i)**2
    return s

x=int(raw_input())
prev=[x]
c=0
while x!=1:
    tmp=0
    tmp=sumsq(x)
    c+=1
    x=tmp
    if x in prev:   break
    else: prev.append(x)

if x==1:
    print c
else:
    print -1