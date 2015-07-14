m=[]
frf=[]
for _ in xrange(int(raw_input())):
    x=map(int,raw_input().split())
    id,fn,f=x[0],x[1],x[2:]
    m.append(id)
    frf+=f

for i in range(len(m)):
    d=m[i]
    s=frf.count(d)
    for j in range(s):
        frf.remove(d)

print len(set(frf))
